import hashlib
import os
import logging

logger = logging.getLogger(__name__)

class AuthService:
    def hash_password(self, password):
        """ Generates random salt and returns salted_hex and hashed password."""
        try:
            salt = os.urandom(16) # Generates a random 16-byte salt
            pwd_bytes = password.encode('utf-8') # Converts password to bytes
            salted_pwd = salt + pwd_bytes
            hashed_pwd = hashlib.sha256(salted_pwd).hexdigest() # Hashes the salted password

            logger.debug("Password hashed Successfully")
            return salt.hex(), hashed_pwd
        
        except Exception as e:
            logger.error(f"Hashing Failed. Error: {e}")
            raise

    def verify_password(self, stored_salt_hex, stored_hash, input_password):
        """ Checks if input_password matches the stored hash"""
        try:
            salt = bytes.fromhex(stored_salt_hex) # Converts hex salt to bytes
            input_pwd_bytes = input_password.encode('utf-8') # Converts input password to bytes
            salted_input = salt + input_pwd_bytes
            input_hash = hashlib.sha256(salted_input).hexdigest() # Hashes the salted input password

            match = (input_hash == stored_hash)
            if match:
                logger.debug("Password Verification Successful")
            else:
                logger.warning("Password Verification Failed")
            return match
        except Exception as e:
            logger.error(f"Verification failed. Error: {e}")
            return False