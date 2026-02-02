import logging
# from datetime import datetime
# import uuid

logger = logging.getLogger(__name__)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        logger.info(f"Account created with balance: {balance}")

    def deposit(self, amount):
        if amount <= 0:
            logger.error(f"Failed Deposit: Negative amount {amount}")
            raise ValueError("Deposit amount must be Positive")
        self.__balance += amount
        logger.info(f"Deposited {amount}, new balance: {self.__balance}")
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
        return self.__balance
    
    def get_balance(self):
        logger.info(f"Balance Checked: {self.__balance}")
        return self.__balance