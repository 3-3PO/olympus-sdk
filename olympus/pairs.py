from olympus.account import Account
from olympus.fixtures import abis, addresses
from olympus.tokens import OHM, DAI

class UniswapV2Pair(Account):
    """Class for a Uniswap V2 pair.

    Args:
        zero: zeroeth Account (i.e. token) in the pair
        one: oneth Account in the pair
        address: address of pair contract

    Exposes https://uniswap.org/docs/v2/smart-contracts/pair/.
    """
    def __init__(self, zero, one, address, *args, **kwargs):
        for k, v in {'zero': zero, 'one': one}.items():
            if not isinstance(v, Account):
                raise ValueError(
                    f"Expected '{k}' to be instance of subclass of {Account}, instead got {type(v)}: {v}"
                )
            
        self.zero = zero
        self.one = one
        super().__init__(address, *args, abi=abis['PairContract.json']['abi'], **kwargs)

class OHM_DAI(UniswapV2Pair):
    """Convenience class for OHM-DAI Uniswap V2 pair."""
    def __init__(self, *args, **kwargs):
        super().__init__(
            OHM(), DAI(), addresses['ohm_dai_pair_address']
        )