import os 

import pytest

from olympus.account import Account
from olympus.consts import ZERO_ACCOUNT
from olympus.exceptions import AccountException

class DummyTransactable:
    """Dummy transactable.

    Similar api to an on-chain func from web3 so we don't call the
    live stuff when testing.
    """
    def call(self):
        return

    def buildTransaction(self, *args, **kwargs):
        return

class RemovePK:
    def __enter__(self):
        if 'WALLET_PK' in os.environ:
            self.tmp_pk = os.getenv('WALLET_PK')
            del os.environ['WALLET_PK']

    def __exit__(self, type, value, traceback):
        if hasattr(self, 'tmp_pk'):
            os.environ['WALLET_PK'] = self.tmp_pk

def test_transact_without_pk_raises():
    with RemovePK():
        with pytest.raises(AccountException):
            Account(ZERO_ACCOUNT).transact(DummyTransactable())