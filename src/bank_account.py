import logging
from src.file_handler import FileHandler
from datetime import datetime
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
            self.__balance = self.transactions[-1]['balance']
            # self._recalculate_balance(). # Recalculating balance from transactions to ensure accuracy, in case of any manual file edits or discrepancies.
            logger.info(f"Account loaded with existing transactions, balance recalculated to: {self.__balance}")
        else:
            self.__balance = balance
            logger.info(f"Account created with balance: {balance}")

    def deposit(self, amount):
        if amount <= 0:
            logger.error(f"Failed Deposit: Negative amount {amount}")
            raise ValueError("Deposit amount must be Positive")
        self.__balance += amount

        logger.info(f"Deposited {amount}, new balance: {self.__balance}")
        self._record_transaction('Deposit', amount)

        return self.__balance
    
    def withdraw(self, amount):
        if amount <= 0:
            logger.error(f"Failed Withdrawl: Negative amount {amount}")
            raise ValueError("Withdraw amount must be Positive")
        if amount > self.__balance:
            logger.error(f"Failed Withdrawl: Insufficient funds {amount} requested")
            raise ValueError("Insufficient Funds")
        self.__balance -= amount

        logger.info(f"Withdrew {amount}, new balance: {self.__balance}")
        self._record_transaction('Withdraw', amount)
        return self.__balance
    
    def get_balance(self):
        logger.info(f"Balance Checked: {self.__balance}")
        return self.__balance
    
    def _record_transaction(self, type, amount):
        """ Records and saves the transaction to file."""
        transaction = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": type,
            "amount": amount,
            "balance": self.__balance
        }
        self.transactions.append(transaction)
        self.file_handler.save_data(self.transactions)

    def print_statement(self):
        """ Prints the transaction history in a readable format."""
        print(f"\n{'DATE':<20} | {'TYPE':<10} | {'AMOUNT':<10} | {'BALANCE':<10}")
        print("-" * 60)

        for transaction in self.transactions:
            print(f"{transaction['date']:<20} | {transaction['type']:<10} | {transaction['amount']:<10.2f} | {transaction['balance']:<10.2f}")
    
    # def _recalculate_balance(self):
    #     """ Recalculates balance from transaction history."""
    #     for transaction in self.transactions:
    #         if transaction['type'] == 'deposit':
    #             self.__balance += transaction['amount']
    #         elif transaction['type'] == 'withdraw':
    #             self.__balance -= transaction['amount']

    # def _save_transaction(self):
    #     """ Saves current transaction to file."""
    #     self.file_handler.save_data(self.transactions)