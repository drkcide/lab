import pytest
from account import *

class Test:
    def setup_method(self):
        self.account1 = Account('John')
        self.account2 = Account('Jane')

    def teardown_method(self):
        del self.account1
        del self.account2


    def test_init(self):
        assert self.account1.get_name() == 'John'
        assert self.account2.get_name() == 'Jane'
        assert self.account1.get_balance() == 0
        assert self.account2.get_balance() == 0