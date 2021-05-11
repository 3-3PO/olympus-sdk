import json
import os

THIS_DIR = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

def load_abis():
    abis = {}
    abi_dir = os.path.join(THIS_DIR, 'abi')
    for fname in os.listdir(abi_dir):
        fpath = os.path.join(abi_dir, fname)
        with open(fpath, 'r') as f:
            abis[fname] = json.loads(f.read())
    return abis

def load_addresses():
    fname = 'addresses-mainnet.json'
    with open(os.path.join(THIS_DIR, fname), 'r') as f:
        addresses = json.loads(f.read())
    return addresses

abis = load_abis()
addresses = load_addresses()
