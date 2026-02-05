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

# try:
#     alice = BankAccount(1000)
#     alice.deposit(3000)
#     print(f"Alice's balance: {alice.get_balance()}")

#     alice.withdraw(5000) # We'll test the error

# except ValueError as e:                                ## Hard coded test
#     print(f"Error: {e}")

def main():
    print("---  FinCore Ledger System  ---")

    account = BankAccount(balance=0)

    while True:

        print(f"\n Current Balance: {account.get_balance()}")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Print Statement")
        print("4. Exit")

        choice = input("Select an option (1 - 4): ")

        try:
            if choice == '1':
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
                print(f"Deposited: {amount}")

            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
                print(f"Withdrew: {amount}")

            elif choice == '3':
                account.print_statement()

            elif choice == "4":
                print("Saving data... Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()