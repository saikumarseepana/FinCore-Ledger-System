import logging
import os
import sys
from src.bank_account import BankAccount
from src.user_manager import UserManager



# Setting up the directory for logs
log_folder = 'logs'
os.makedirs(log_folder, exist_ok=True)

# Configuring the log file
log_file = os.path.join(log_folder, 'banking.log')

# Handlers
file_handler = logging.FileHandler(log_file)
console_handler = logging.StreamHandler(sys.stdout)

logging.basicConfig(
    # filename = log_file,
    level = logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers = [file_handler, console_handler]
)

# print(f"System Initialized. Logs are writing to: {log_file}")
logger = logging.getLogger("MainApp")
logger.info(f"System Initialized. Logs are writing to: {log_file}")

def main():
    print("\n=== FinCore Ledger System (Secure v1.0) ===")

    user_manager = UserManager()

    while True:
        print("\n--- AUTH MENU ---")
        print("1. Login")
        print("2. Register New User")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            username = input("username: ").strip()
            password = input("password: ").strip()

            success, message = user_manager.login(username, password)
            print(message)

            if success:
                run_bank_system(username, user_manager)

        elif choice == '2':
            new_user = input("Enter a Username: ").strip()
            new_pass = input("Enter a Password: ").strip()

            if not new_user or not new_pass:
                print("Error: Username/Password cannot be empty.")
                continue
            
            success, message = user_manager.register_user(new_user, new_pass)
            print(message)

        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


def run_bank_system(username, user_manager):
    """ Protected banking Area, only accessible after successful login."""
    logger.info(f"Starting Bank session for {username}")

    
    try:
        # Initializing the account for this user
        account = BankAccount(username=username)
    except ValueError as e:
        print(f"Error loading account: {e}")
        return

    while True:

        print(f"\n User: {username} | Balance: ${account.get_balance():.2f}")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer Funds")
        print("4. Print Statement")
        print("5. Exit")

        choice = input("Select an option: ")

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
                recipient_name = input("Enter recipient username: ").strip()

                if recipient_name == username: # Self transfer check
                    print("You cannot self transfer funds")
                    continue

                if recipient_name not in user_manager.users: # Recipient existence check
                    print("Recipient not found")
                    continue

                amount = float(input("Enter transfer amount: "))

                if amount > account.get_balance(): # Insufficient funds check
                    print("Insufficient funds for transfer")
                    continue

                print("Processing transfer...")

                try:
                    account.withdraw(amount) # withdraw from sender


                    # Loads the recipient's account and deposits the amount
                    recipient_account = BankAccount(username=recipient_name)
                    recipient_account.receive_transfer(amount, sender=username)

                    print(f"✅ Success! Sent ${amount} to {recipient_name}.")
                    logger.info(f"Transfer success: {username} -> {recipient_name} | Amount: ${amount}")

                except Exception as e:
                    print(f"Transfer failed: {e}")
                    print("Rolling back transaction...")

                    account.deposit(amount) # Refunds the amount back to sender in case of any failure during transfer
                    logger.error(f"Transfer failed: {username} -> {recipient_name} | Reason: {e}")

            elif choice == '4':
                account.print_statement()

            elif choice == "5":
                print(f"Logging out {username}...")
                logger.info(f"Ending session for {username}")
                break
            else:
                print("Invalid choice.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()