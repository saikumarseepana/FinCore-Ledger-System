import pytest
from src.auth import AuthService

def test_password_hashing_and_verification():
    """
    Test that a password can be hashed and then successfully verified 
    with the correct salt and hash.
    """
    auth = AuthService()
    password = "SuperSecretPassword123!"
    
    # 1. Hash the password
    salt, hashed_pw = auth.hash_password(password)
    
    # 2. Verify with the CORRECT password (Should return True)
    is_valid = auth.verify_password(salt, hashed_pw, password)
    assert is_valid == True, "Valid password was rejected!"

    # 3. Verify with the WRONG password (Should return False)
    wrong_password = "WrongPassword999!"
    is_invalid = auth.verify_password(salt, hashed_pw, wrong_password)
    assert is_invalid == False, "Security Flaw: Wrong password was accepted!"