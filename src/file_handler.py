import json
import os

class FileHandler:
    def __init__(self, file_name):
        self.file_name = file_name
        self._ensure_file_exists() # checks for the file existence on initialization

    def _ensure_file_exists(self):
        """
        Creates the folder and empty file if they don't exist.
        """
        directory = os.path.dirname(self.file_name)  

        if directory and not os.path.exists(directory):
            os.makedirs(directory)       # Create directory if it doesn't exist

        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as file:
                json.dump([], file)     # Initialize with an empty list                         

    def save_data(self, data):
        """
        Takes a list of data and writes it to the file.
        'w' mode overwrites the file with fresh data.
        """
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        """
        Reads data from the file and returns it as a list.
        If the file does not exist or is empty, returns an empty list.
        """
        try:

            with open(self.file_name, 'r') as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []