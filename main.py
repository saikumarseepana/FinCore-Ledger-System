import logging
import os
from src.bank_account import BankAccount

# Setting up the directory for logs
log_folder = 'logs'
os.makedirs(log_folder, exist_ok=True)

# Configuring the log file
log_file = os.path.join(log_folder, 'banking.log')

logging.basicConfig(
    filename = log_file,
    level = logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

print(f"System Initialized. Logs are writing to: {log_file}")

try:
    alice = BankAccount(1000)
    alice.deposit(3000)
    print(f"Alice's balance: {alice.get_balance()}")

    alice.withdraw(5000) # We'll test the error

except ValueError as e:
    print(f"Error: {e}")