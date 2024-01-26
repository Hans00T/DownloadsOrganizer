import tkinter as tk
from tkinter import messagebox, filedialog
from file_organizer_logic import organize_files
from utils.json_utils import FILE_TYPES
import json


def select_folder(entry_var):
    folder_path = filedialog.askdirectory()
    entry_var.set(folder_path)


def organize_button_clicked(entry_var, file_types):
    source_folder = entry_var.get()
    success, error_message = organize_files(source_folder, file_types)

    if success:
        show_notification("Success", "Files organized successfully!")
    else:
        show_notification("Error", error_message)


def add_file_type(file_type_entry, extensions_entry):
    new_file_type = file_type_entry.get()
    extensions = extensions_entry.get().split(",")

    FILE_TYPES[new_file_type] = extensions

    with open('file_types.json', 'w') as json_file:
        json.dump(FILE_TYPES, json_file, indent=4)

        file_type_entry.delete(0, tk.END)
        extensions_entry.delete(0, tk.END)

def show_notification(title, message):
    messagebox.showinfo(title, message)