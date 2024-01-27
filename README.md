# Downloads Organizer
**NOTE: This version of the script is still in development and may not work as expected. Use at your own risk. If you find any bugs or have any suggestions, please let me know.**
## Description
### What is it?
This script organizes any directory by moving files into directories based on their extension.
The script will create a directory for each extension and move the files into the corresponding directory. If a directory already exists for a certain extension, the files will be moved into that directory. The goal is to make it easier to find and manage files. 
### Why is it?
This project was created for my own needs. Specifically to organize a messy downloads directory and to sharpen my programming skills while at it. Sorting files by extension helps finding files faster and makes it easier to delete files that are no longer needed and to move important files to another location.
### What does it do?
- Organizes the downloads directory (or any directory you choose) by moving files into subdirectories based on their extension
- Creates a directory for each extension and moves the files into the corresponding directory
- Lets you choose the names of the directories and the extensions that go in them and stores that information into file_types.json
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
This will open an interactive menu with the following tabs:
- **Organize Files**: Here you can organize your Downloads directory with a press of a button or choose other directory to organize.
- **Create New Folder Templates**: Choose a name for a new directory and assign what files go in it. This only creates a "template" that will be used when organizing a directory. The template can be edited or deleted later but after creating a directory with such template the existing directory will not be changed changed or removed from your directories by this script.
- **Delete Folder Templates**: Here you can choose any directory template from the dropdown menu and delete it. This will not delete existing directory created with the template.
- **Edit Folder Templates**: Choose any directory template from the dropdown menu and edit its name and extensions.
