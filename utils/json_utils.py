"""
This module contains the functions that are used to load and save the FILE_TYPES dictionary to a JSON file.
"""
import json, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Loads the FILE_TYPES dictionary from the file_types.json file
def load_from_json():
    try:
        with open('file_types.json') as f:
            file_types = json.load(f)
        return file_types
    except Exception as e:
        print(f"Error loading from JSON: {e}")
        return {}

# Updated save_to_json function
def save_to_json(file_types, filename='file_types.json'):
    try:
        with open(filename, 'w') as json_file:
            json.dump(file_types, json_file, indent=4)
        return True  # Return True if the save operation was successful
    except Exception as e:
        print(f"Error saving to JSON: {e}")
        return False  # Return False if the save operation failed
