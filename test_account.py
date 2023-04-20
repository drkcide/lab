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

    def test_deposit(self):
        assert self.account1.deposit(10) is True
        assert self.account1.get_balance() == 10
        assert self.account1.deposit(10.00) is True
        assert self.account1.get_balance() == pytest.approx(20.00, abs=0.001)
        assert self.account1.deposit(-10.00) is False
        assert self.account1.deposit(0.00) is False

        assert self.account2.deposit(10) is True
        assert self.account2.get_balance() == 10
        assert self.account2.deposit(10.00) is True
        assert self.account2.get_balance() == pytest.approx(20.00, abs=0.001)
        assert self.account2.deposit(-10.00) is False
        assert self.account2.deposit(0.00) is False

    def test_withdraw(self):
        assert self.account1.deposit(10.00) is True
        assert self.account1.withdraw(-10.00) is False
        assert self.account1.withdraw(0) is False
        assert self.account1.withdraw(5.00) is True
        assert self.account1.get_balance() == pytest.approx(5.00, abs=0.001)
        assert self.account1.withdraw(15.00) is False
        assert self.account1.withdraw(5) is True
        assert self.account1.get_balance() == pytest.approx(0.00, abs=0.001)

        assert self.account2.deposit(10.00) is True
        assert self.account2.withdraw(-10.00) is False
        assert self.account2.withdraw(0) is False
        assert self.account2.withdraw(5.00) is True
        assert self.account2.get_balance() == pytest.approx(5.00, abs=0.001)
        assert self.account2.withdraw(15.00) is False
        assert self.account2.withdraw(5) is True
        assert self.account2.get_balance() == pytest.approx(0.00, abs=0.001)