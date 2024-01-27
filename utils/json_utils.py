"""
This module contains the functions that are used to load and save the FILE_TYPES dictionary to a JSON file.
"""
import json

def load_from_json():
    try:
        # Load the FILE_TYPES dictionary from the JSON file
        with open('file_types.json') as f:
            file_types = json.load(f)
        return file_types
    except Exception as e:
        print(f"Error loading from JSON: {e}")
        return {}

def save_to_json(file_types):
    try:
        # Save file types to the JSON file
        with open('file_types.json', 'w') as json_file:
            json.dump(file_types, json_file, indent=4)
        return True  # Return True if the save operation was successful
    except Exception as e:
        print(f"Error saving to JSON: {e}")
        return False  # Return False if the save operation failed
