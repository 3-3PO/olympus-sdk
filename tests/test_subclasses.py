import pytest

from olympus.router import UniswapV2Router02
from olympus.consts import ZERO_ACCOUNT

class AccountWithClashingNameSpace(UniswapV2Router02):
    # Router has an on-chain function with this name
    def WETH(self):
        pass 

def test_clashing_namespace_warns():
    with pytest.warns(
        UserWarning, 
        match="WETH already in namespace of <class 'tests.test_subclasses.AccountWithClashingNameSpace'> object."
    ):
        AccountWithClashingNameSpace()