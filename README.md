# Downloads Organizer
**NOTE: This version of the script is still in development and may not work as expected. Use at your own risk. The script WILL overwrite files with the same name in it's current state. Use at your own risk. If you find any bugs or have any suggestions, please let me know.**
## Description
### What is it?
This script organizes the downloads folder by moving files into folders based on their extension.
The script will create a folder for each extension and move the files into the corresponding folder. If a folder already exists for a certain extension, the files will be moved into that folder. The goal is to make it easier to find and manage files in the downloads folder. Sorting files by extension helps to find files faster and makes it easier to delete files that are no longer needed or move important files to another location.
### What does it do?
- Organizes the downloads folder by moving files into folders based on their extension
- Creates a folder for each extension and moves the files into the corresponding folder
## Requirements
- Python 3
- Any operating system
- Downloads folder in the home directory
## Usage
Open a terminal in the directory where the script is located and run the following command:
```bash
python main.py
```
This will open an interactive menu where you can choose to organize the downloads folder, choose a different folder to organize or exit the script. If you choose to organize the downloads folder, the script will create a folder for each extension and move the files into the corresponding folder. If a folder already exists for a certain extension, the files will be moved into that folder. If you choose to organize a different folder, you will be prompted to enter the path to the folder you want to organize. The script will then create a folder for each extension and move the files into the corresponding folder. If a folder already exists for a certain extension, the files will be moved into that folder. If you choose to exit the script, the script will exit.
