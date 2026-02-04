# FinCore-Ledger-System
A production-grade banking backend implementing robust OOP principles, transaction logging, and audit trails. Built with Python.

## 🚀 Key Features

* **OOP Architecture:** Encapsulated logic with private attributes to prevent direct state modification.
* **Robust Validation:** Prevents negative deposits and overdrafts with custom error handling.
* **Audit Logging:** Replaces standard `print` statements with Python's `logging` module to create a permanent, timestamped audit trail of all transactions in `logs/banking.log`.
* **Data Persistence:** Automated JSON file handling ensures account balances and transaction history survive program restarts.
* **Interactive CLI:** A user-friendly terminal interface for depositing, withdrawing, and checking balances in real-time.

## 🛠️ How to Run
**1. Start the Application:**
```bash
   python main.py
```
**2. Interact: Follow the on-screen menu to manage your account. Data is automatically saved to data/transactions.json upon every transaction.**

## 🧪 Running Tests
This project uses `pytest` for unit testing to ensure reliability.

**1. Install pytest:**
```bash
pip install pytest
```
**2. Run the test suite:**
```bash
python -m pytest
```