import logging
from src.file_handler import FileHandler
# from datetime import datetime
# import uuid

logger = logging.getLogger(__name__)

class BankAccount:
    def __init__(self, balance, file_path='data/bank_accounts.json'):
        if balance < 0:
            logger.error(f"Failed Account Creation: Negative initial balance {balance}")
            raise ValueError("Initial balance cannot be Negative")
        
        self.file_handler = FileHandler(file_path) # File Handler

        self.transactions = self.file_handler.load_data() # Loading history

        #Balance
        if self.transactions:
            self.__balance = 0.0 # This will rest the balance as transactions exist so we ignore the initial balance here otherwise it will be a bug
            self._recalculate_balance()
            logger.info(f"Account loaded with existing transactions, balance recalculated to: {self.__balance}")
        else:
            self.__balance = balance
            logger.info(f"Account created with balance: {balance}")

    def deposit(self, amount):
        if amount <= 0:
            logger.error(f"Failed Deposit: Negative amount {amount}")
            raise ValueError("Deposit amount must be Positive")
        self.__balance += amount

        self.transactions.append({
            'type': 'deposit',
            'amount': amount
        })
        logger.info(f"Deposited {amount}, new balance: {self.__balance}")
        self._save_transaction()

        return self.__balance
    
    def withdraw(self, amount):
        if amount <= 0:
            logger.error(f"Failed Withdrawl: Negative amount {amount}")
            raise ValueError("Withdraw amount must be Positive")
        if amount > self.__balance:
            logger.error(f"Failed Withdrawl: Insufficient funds {amount} requested")
            raise ValueError("Insufficient Funds")
        self.__balance -= amount

        self.transactions.append({
            'type': 'withdraw',
            'amount': amount
        })

        logger.info(f"Withdrew {amount}, new balance: {self.__balance}")
        self._save_transaction()
        return self.__balance
    
    def get_balance(self):
        logger.info(f"Balance Checked: {self.__balance}")
        return self.__balance
    
    def _recalculate_balance(self):
        """ Recalculates balance from transaction history."""
        for transaction in self.transactions:
            if transaction['type'] == 'deposit':
                self.__balance += transaction['amount']
            elif transaction['type'] == 'withdraw':
                self.__balance -= transaction['amount']

    def _save_transaction(self):
        """ Saves current transaction to file."""
        self.file_handler.save_data(self.transactions)