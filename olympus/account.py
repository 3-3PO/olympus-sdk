import os
import warnings

from olympus import config
from olympus.consts import ZERO_ACCOUNT
from olympus.exceptions import AccountException
from olympus.web3_init import w3

class Account:
    """Class for an Ethereum account.

    args:
        address (str): account address
        abi (dict, optional): abi of a contract. 
            If given, self.contract will have a web3.contract.Contract.
        pk (str, optional): private key. If not given, cannot .transact.

    attributes:
        contract (web3.contract.Contract or None): contract
        contract_funcs (dict): dict of {
            anything in abi that had type 'function': web3.contract.ContractFunction
        }

        
        Any functions in contract_funcs will also be exposed as object attributes.

    methods:
        transact: transact a web3.contract.ContractFunction. 
    """
    def __init__(self, address, abi=None, pk=None):
        self.address = address
        if abi is not None:
            self.contract = w3.eth.contract(
                abi=abi,
                address=address
            )    
            self.contract_funcs = {a['name']: a for a in abi if a['type'] == 'function'}
        else:
            self.contract = None
            self.contract_funcs = {}

        self.pk = pk

        for f in self.contract_funcs:
            try:
                self.__getattribute__(f)
                warnings.warn(
                    f"{f} already in namespace of {self.__class__} object. If you'd"
                    f" like to call the on-chain contract function use o.contract.functions.{f} instead."
                )
            except AttributeError:
                pass

    def __getattr__(self, name):
        if name in self.contract_funcs:
            return getattr(self.contract.functions, name)
        return self.__getattribute__(name)

    def transact(self, function, wait=True, check=True, **kwargs):
        """Transact a contract function.

        Args:
            function (web3.contract.ContractFunction): contract function to transact. 
            wait (bool): whether to wait for transaction to be mined before returning.
            check (bool): whether to check function before transacting, i.e. if True, function.call()
                will be called before function.transact().
            kwargs: will be passed to 
        """
        if self.pk is None:
            raise AccountException(
                f'{self}: Cannot transact without a private key to sign with'
            )
        if check:
            # Just call the thing before spending gas
            function.call()
        t = function.buildTransaction(
            {
                **{
                    'chainId': config.CHAIN_ID,
                    'nonce': w3.eth.get_transaction_count(self.address)
                }, 
                **kwargs
            }
        )
        signed = w3.eth.account.sign_transaction(t, private_key=self.pk)
        tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
        if not wait:
            # Other case returns dict with this key so just similarize
            return {'transactionHash': tx_hash}
        return w3.eth.wait_for_transaction_receipt(tx_hash)