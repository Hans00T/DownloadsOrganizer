# Downloads Organizer
**NOTE: This version of the script is still in development and may not work as expected. Use at your own risk. If you find any bugs or have any suggestions, please let me know.**
## Description
### What is it?
This script organizes any folder by moving files into folders based on their extension.
The script will create a folder for each extension and move the files into the corresponding folder. If a folder already exists for a certain extension, the files will be moved into that folder. The goal is to make it easier to find and manage files. 
### Why is it?
This project was created for my own needs. Specifically to organize a messy downloads folder and to sharpen my programming skills while at it. Sorting files by extension helps finding files faster and makes it easier to delete files that are no longer needed and to move important files to another location.
### What does it do?
- Organizes the downloads folder (or any folder you choose) by moving files into folders based on their extension
- Creates a folder for each extension and moves the files into the corresponding folder
## Requirements
- Python 3
- Any operating system
## Installation steps
Clone the repository:
```bash
git clone https://github.com/Hans00T/DownloadsOrganizer.git
```
Navigate to the directory:
```bash
cd DownloadsOrganizer
```
Create a virtual environment:
```bash
python -m venv venv
```
Activate the virtual environment:
Windows:
```bash
venv\Scripts\activate
```
Linux & MacOS:
```bash
source venv/bin/activate
```
Install the requirements:
```bash
pip install -r requirements.txt
```
## Usage
Open a terminal in the directory where the script is located and run the following command:
```bash
python main.py
```
This will open an interactive menu where you can choose to organize the downloads folder, choose a different folder to organize or exit the script. If you choose to organize the downloads folder, the script will create a folder for each extension and move the files into the corresponding folder. If a folder already exists for a certain extension, the files will be moved into that folder. If you choose to organize a different folder, you will be prompted to enter the path to the folder you want to organize. The script will then create a folder for each extension and move the files into the corresponding folder. If a folder already exists for a certain extension, the files will be moved into that folder. If you choose to exit the script, the script will exit.
