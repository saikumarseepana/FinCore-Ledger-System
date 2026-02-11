import os
import pytest
from src.bank_account import BankAccount

TEST_USER = "pytestdummyuser"
# Your code strips non-alphanumeric, so we match that logic for the file path
TEST_FILE_PATH = f"data/{TEST_USER}_transactions.json"

def setup_function():
    """Runs BEFORE every test. Destroys old test data."""
    if os.path.exists(TEST_FILE_PATH):
        os.remove(TEST_FILE_PATH)

def teardown_function():
    """Runs AFTER every test. Cleans up the mess."""
    if os.path.exists(TEST_FILE_PATH):
        os.remove(TEST_FILE_PATH)

def test_initial_balance_is_zero():
    # 1. ARRANGE (Because of setup_function, we know no file exists)
    account = BankAccount(username=TEST_USER)
    
    # 2. ACT
    current_balance = account.get_balance()
    
    # 3. ASSERT
    assert current_balance == 0.0, f"Expected 0.0, got {current_balance}"

def test_deposit_increases_balance():
    account = BankAccount(username=TEST_USER)

    account.deposit(100.0)
    current_balance = account.get_balance()

    assert current_balance == 100.0, f"Expected 100.0, got {current_balance}"

def test_withdraw_decreases_balance():
    account = BankAccount(username=TEST_USER)

    account.deposit(200.0)

    account.withdraw(50.0)
    current_balance = account.get_balance()

    assert current_balance == 150.0, f"Expected 150.0, got {current_balance}"

def test_withdraw_insufficient_funds():
    account = BankAccount(username=TEST_USER)

    account.deposit(50.0)

    with pytest.raises(ValueError, match="Insufficient Funds"):
        account.withdraw(200.0)

def test_receive_transfer_increases_balance():
    account = BankAccount(username=TEST_USER)

    account.receive_transfer(100.0, sender="TestSender")
    current_balance = account.get_balance()

    assert current_balance == 100.0, f"Expected 100.0, got {current_balance}"

def test_negative_deposit_raises_error():
    account = BankAccount(username=TEST_USER)

    with pytest.raises(ValueError, match="Deposit amount must be Positive"):
        account.deposit(-50.0)

def test_negative_wihdrawl_raises_error():
    account = BankAccount(username=TEST_USER)

    with pytest.raises(ValueError, match="Withdraw amount must be Positive"):
        account.withdraw(-30.0)

def test_receive_transfer_negative_amount_raises_error():
    account = BankAccount(username=TEST_USER)

    with pytest.raises(ValueError, match="Transfer amount must be positive."):
        account.receive_transfer(-20.0, sender="TestSender")