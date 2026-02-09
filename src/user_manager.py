import logging
from src.auth import AuthService
from src.file_handler import FileHandler

logger = logging.getLogger(__name__)

class UserManager:
    def __init__(self):
        self.auth = AuthService()
        self.file_handler = FileHandler('data/users.json') # User data file
        self.users = self._load_data()

    def _load_data(self):
        """ Loads user using FileHandler"""
        data = self.file_handler.load_data()

        if isinstance(data, list):
            return {}
        return data if data else {}
    
    def _save_users(self):
        """ Saves user data using FileHandler"""
        self.file_handler.save_data(self.users)

    def register_user(self, username, password):
        """ Registers a new user with salt + Hash"""
        if username in self.users:
            logger.warning(f"Registration failed. Username {username} already exists.")
            return False, "Username already exists."
        
        try:
            salt, hashed_pwd = self.auth.hash_password(password) # Generates salt and hash
            self.users[username] = {
                'salt': salt,
                'password_hash': hashed_pwd 
            }
            self._save_users() # saves the new user data to file

            logger.info(f"New User Registered: {username}")
            return True, "Registration Successful"
        except Exception as e:
            logger.error(f"Registration error for {username}. Error: {e}")
            return False, f"Error: {e}"
        
    def login(self, username, password):
        """ Verifies user credentials for login"""

        if username not in self.users: # Checks if username exists
            logger.warning(f"Login failed. Username {username} not found.")
            return False, "Invalid username or password."
        
        user_record = self.users[username]
        stored_salt = user_record['salt']
        stored_hash = user_record['password_hash']

        is_valid = self.auth.verify_password(stored_salt, stored_hash, password) # Verifies the password

        if is_valid:
            logger.info(f"Login Successful: {username}")
            return True, "login successful."
        else:
            logger.warning(f"Login Failed. Incorrect password for {username}.")
            return False, "Invalid username or password."



