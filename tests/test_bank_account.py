import pytest
import os
from src.bank_account import BankAccount

TEST_FILE = 'data/test_transactions.json'


@pytest.fixture(autouse=True)
def clean_up_file():
    """ Runs before and after each test"""
    file_name = TEST_FILE
    # Before test: Clear the file
    if os.path.exists(file_name):
        os.remove(file_name)

    yield # run the tests

    # After test: Clear the file
    # if os.path.exists(file_name):
    #     os.remove(file_name)

@pytest.fixture
def create_account():

    def _maker(initial_balance):
        return BankAccount(initial_balance, file_path=TEST_FILE)
    return _maker



def test_initial_balance(create_account):
    account = create_account(350)
    assert account.get_balance() == 350

def test_deposit(create_account):
    account = create_account(50)
    account.deposit(100)
    assert account.get_balance() == 150

def test_withdraw(create_account):
    account = create_account(500)
    account.withdraw(57)
    assert account.get_balance() == 443

def test_deposit_negative_amount_error(create_account):
    account = create_account(125)

    with pytest.raises(ValueError):
        account.deposit(-20)

def test_withdraw_negative_amount_error(create_account):
    account = create_account(1000)

    with pytest.raises(ValueError):
        account.withdraw(-1500)

def test_withdraw_insufficient_funds_error(create_account):
    account = create_account(250)

    with pytest.raises(ValueError):
        account.withdraw(300)

def test_initial_balance_negative_error():

    with pytest.raises(ValueError):
        BankAccount(-100)