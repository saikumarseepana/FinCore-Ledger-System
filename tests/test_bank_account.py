import pytest
from src.bank_account import BankAccount

def test_initial_balance():
    account = BankAccount(350)
    assert account.get_balance() == 350

def test_deposit():
    account = BankAccount(50)
    account.deposit(100)
    assert account.get_balance() == 150

def test_withdraw():
    account = BankAccount(500)
    account.withdraw(57)
    assert account.get_balance() == 443

def test_deposit_negative_amount_error():
    account = BankAccount(125)

    with pytest.raises(ValueError):
        account.deposit(-20)

def test_withdraw_negative_amount_error():
    account = BankAccount(1000)

    with pytest.raises(ValueError):
        account.withdraw(-1500)

def test_withdraw_insufficient_funds_error():
    account = BankAccount(250)

    with pytest.raises(ValueError):
        account.withdraw(300)

def test_initial_balance_negative_error():

    with pytest.raises(ValueError):
        BankAccount(-100)