import time

from olympus.account import Account
from olympus.fixtures import abis, addresses
from olympus.web3_init import w3

class UniswapV2Router02(Account):
    """Class for a Uniswap V2 Router02.
    
    Exposes https://uniswap.org/docs/v2/smart-contracts/router02/.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(
            addresses['router_address'], 
            abi=abis['UniswapV2Router02.json'],
            *args, **kwargs
        )
