from olympus.account import Account
from olympus.fixtures import abis, addresses
from olympus.web3_init import w3

class ERC20Token(Account):
    def __init__(self, address, *args, **kwargs):
        super().__init__(address, abis['IERC20.json']['abi'], *args, **kwargs)


class OHM(ERC20Token):
    def __init__(self, *args, **kwargs):
        super().__init__(addresses['ohm_address'], *args, **kwargs)


class DAI(ERC20Token):
    def __init__(self, *args, **kwargs):
        super().__init__(addresses['dai_address'], *args, **kwargs)