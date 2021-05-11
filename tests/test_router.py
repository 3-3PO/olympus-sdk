from olympus.router import UniswapV2Router02

def test_router_inits():
    UniswapV2Router02()

def test_on_chain_funcs_loaded():
    UniswapV2Router02().WETH
    