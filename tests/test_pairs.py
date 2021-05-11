import pytest

from olympus.consts import ZERO_ACCOUNT
from olympus.pairs import UniswapV2Pair, OHM_DAI
from olympus.tokens import OHM, DAI

def test_uniswap_pair_inits():
    UniswapV2Pair(OHM(), DAI(), ZERO_ACCOUNT)

def test_uniswap_raises_on_invalid_constituent_type():
    with pytest.raises(ValueError, match="Expected 'one' to be instance of subclass of "):
        UniswapV2Pair(OHM(), 'test', ZERO_ACCOUNT)

def test_ohm_dai_call_works():
    # Random on-chain function
    OHM_DAI().totalSupply().call()