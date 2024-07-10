import os
import time
  

class FileManager:

    def __init__(self):
        
        with open('/datos/config.json', 'r') as f:
            self.config = json.load(f)

        self.TFCARD_CS = self.config["TFCARD_CS"]
        self.TFCARD_MISO = self.config["TFCARD_MISO"]
        self.TFCARD_MOSI = self.config["TFCARD_MOSI"]
        self.TFCARD_SCK = self.config["TFCARD_SCK"]

        self.current_dir = os.getcwd()  # Get the current working directory

    def list_files(self, path):
        """
        Lists the files and directories in the specified path.

        Args:
            path (str): The path to the directory to list.

        Returns:
            list: A list of filenames and directory names.
        """
        files = os.listdir(path)
        return files

    def change_dir(self, path):
        """
        Changes the current working directory to the specified path.

        Args:
            path (str): The path to the directory to change to.
        """
        try:
            os.chdir(path)
            self.current_dir = os.getcwd()
            print(f"Changed directory to: {self.current_dir}")
        except OSError as e:
            print(f"Error changing directory: {e}")

    def go_back(self):
        """
        Goes back to the previous directory.
        """
        try:
            os.chdir('..')
            self.current_dir = os.getcwd()
            print(f"Changed directory to: {self.current_dir}")
        except OSError as e:
            print(f"Error going back: {e}")

    def execute_script(self, script_name):
        """
        Executes the specified script file.

        Args:
            script_name (str): The name of the script file to execute.
        """
        try:
            with open(script_name, 'r') as f:
                script_code = f.read()
            exec(script_code)
            print(f"Script '{script_name}' executed successfully.")
        except OSError as e:
            print(f"Error executing script '{script_name}': {e}")

# Example usage
# file_manager = FileManager()

# List files in the current directory
# print("Files in current directory:")
# files = file_manager.list_files(".")
# for file in files:
#     print(file)

# Change directory to SD card
# print("\nChanging directory to SD card:")
# file_manager.change_dir("/sd")

# List files in the SD card
# print("\nFiles in SD card:")
# files = file_manager.list_files("/sd")
# for file in files:
#     print(file)

# Go back to the previous directory
# print("\nGoing back to previous directory:")
# file_manager.go_back()

# Execute a script
# print("\nExecuting script 'myscript.py':")
# file_manager.execute_script("myscript.py")
