# FinCore-Ledger-System
A production-grade banking backend implementing robust OOP principles, transaction logging, and audit trails. Built with Python.

## 🚀 Key Features

* **OOP Architecture:** Encapsulated logic with private attributes to prevent direct state modification.
* **Robust Validation:** Prevents negative deposits and overdrafts with custom error handling.
* **Audit Logging:** Replaces standard `print` statements with Python's `logging` module to create a permanent, timestamped audit trail of all transactions in `logs/banking.log`.

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