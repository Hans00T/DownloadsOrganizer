"""
This file contains the functions that are used by the GUI.
"""
import os, sys
import tkinter as tk
from tkinter import messagebox, filedialog

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic.file_organizer_logic import organize_files
from utils.json_utils import load_from_json, save_to_json


def select_folder(entry_var):
    folder_path = filedialog.askdirectory()
    entry_var.set(folder_path)


# Organizes the files in the selected folder
def organize_button_clicked(entry_var):
    file_types = load_from_json()
    source_folder = entry_var.get()
    success, error_message = organize_files(source_folder, file_types)

    if success:
        show_notification("Success", "Files organized successfully!")
    else:
        show_notification("Error", error_message)


# Updates the labels in the delete and edit tabs
def update_labels(selected_folder, folder_name_entry, extensions_entry, original_folder_name_var, original_extensions_var):
    file_types = load_from_json()
    original_folder_name_var.set("Original Folder Template Name: " + selected_folder)
    original_extensions_var.set("Original File Extensions: " + ",".join(file_types[selected_folder]))

    # Prefill the entry fields with old data
    folder_name_entry.delete(0, tk.END)
    folder_name_entry.insert(0, selected_folder)

    extensions_entry.delete(0, tk.END)
    extensions_entry.insert(0, ",".join(file_types[selected_folder]))


# Function to update the dropdowns
def update_dropdowns(folder_name_dropdown, selected_folder_var):
    # Clear existing items in the OptionMenu
    folder_name_dropdown['menu'].delete(0, 'end')

    # Load folder types from the JSON file
    file_types = load_from_json()

    # Set the default value of the OptionMenu to the first folder_name
    if file_types:
        selected_folder_var.set(list(file_types.keys())[0])
    else:
        selected_folder_var.set("")  # Set to empty string if there are no folder names

    # Add items to the OptionMenu based on the contents of the JSON file
    for folder_name in file_types.keys():
        folder_name_dropdown['menu'].add_command(label=folder_name, command=tk._setit(selected_folder_var, folder_name))


# Adds a new folder type to the FILE_TYPES dictionary
def add_folder(folder_name_entry, extensions_entry, folder_name_dropdown, selected_folder_var):
    file_types = load_from_json()
    new_folder = folder_name_entry.get()
    extensions = extensions_entry.get().split(",")

    # Makes sure that the folder name is not empty and doesn't already exist
    if (new_folder in file_types) or (new_folder == ""):
        show_notification("Error", "Folder name already exists or is empty.")
    else:
        # Check if the file type already exists
        if new_folder in file_types:
            # If it exists, update the extensions
            file_types[new_folder].extend(extensions)
        else:
            # If it doesn't exist, create a new entry
            file_types[new_folder] = extensions

        # Save file types to the JSON file
        success = save_to_json(file_types)

        print(str(success))

        if success:
            show_notification("Success", "Folder template added successfully!")
            # Clear the entry fields
            folder_name_entry.delete(0, tk.END)
            extensions_entry.delete(0, tk.END)

            # Update the dropdown menu
            update_dropdowns(folder_name_dropdown, selected_folder_var)
        else:
            show_notification("Error", "Failed to update the JSON file.")


# Deletes a folder type from the FILE_TYPES dictionary
def delete_folder(selected_folder_var, folder_name_dropdown):
    file_types = load_from_json()
    folder_name = selected_folder_var.get()  # Get the selected folder name

    # Checks if the file type exists in the dictionary
    if folder_name in file_types:
        # if it does, delete the entry
        del file_types[folder_name]

    # Save file types to the JSON file and update the dropdowns
    success = save_to_json(file_types)

    if success:
        show_notification("Success", "Folder template deleted successfully!")

        # Update the dropdown menu
        update_dropdowns(folder_name_dropdown, selected_folder_var)

        # Update the selected_folder_var_delete variable
        remaining_folders = list(file_types.keys())
        if remaining_folders:
            # Set the selected folder to the first remaining folder
            selected_folder_var.set(remaining_folders[0])
        else:
            # Set to empty string if there are no folder names
            selected_folder_var.set("")
    else:
        show_notification("Error", "Failed to update the JSON file.")


def edit_folder(selected_folder_var, folder_name_entry, extensions_entry, folder_name_dropdown):
    file_types = load_from_json()
    folder_name = selected_folder_var.get()

    # Checks that the folder name is not empty and doesn't already exist
    if (folder_name_entry.get() == "") or (folder_name_entry.get() in file_types):
        show_notification("Error", "Folder name already exists or is empty.")
    else:
        # Checks if the file type exists in the dictionary
        if folder_name in file_types:
            # if it does, update the entry
            updated_folder_name = folder_name_entry.get()
            updated_extensions = extensions_entry.get().split(",")

            # Update the FILE_TYPES dictionary
            file_types.pop(folder_name, None)  # Remove the old entry
            file_types[updated_folder_name] = updated_extensions  # Add the updated entry

            # Save file types to the JSON file
            success = save_to_json(file_types)

            if success:
                show_notification("Success", "Folder template updated successfully!")
                # Update the dropdown menu for both "Delete Folder Templates" and "Edit Folder Templates"
                update_dropdowns(folder_name_dropdown, selected_folder_var)
            else:
                show_notification("Error", "Failed to update the JSON file.")


def show_notification(title, message):
    messagebox.showinfo(title, message)
