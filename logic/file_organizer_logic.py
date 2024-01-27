"""
Logic for the file organizer
"""
import os
import shutil

def organize_files(downloads_folder, file_types):
    if not os.path.exists(downloads_folder): # Check if the downloads folder exists
        print("Source folder does not exist")
        return False, "Source folder does not exist"

    # Check if the downloads folder is empty
    if not any(os.path.isfile(os.path.join(downloads_folder, f)) for f in os.listdir(downloads_folder)):
        print("Source folder is empty")
        return False, "Source folder is empty"

    for filename in os.listdir(downloads_folder):   # Loop through all the files in the downloads folder
        file_path = os.path.join(downloads_folder, filename)

        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(filename)
            extension = file_extension.lower()

            # Get the folder name based on the file extension, or use the 'other' folder if it doesn't exist
            folder_name = next((file_type for file_type, extensions_list in file_types.items() if extension in extensions_list), "other")

            destination_folder = os.path.join(downloads_folder, folder_name) # Create the destination folder path
            os.makedirs(destination_folder, exist_ok=True)

            destination_path = os.path.join(destination_folder, filename) # Create the destination file path
            base_name, extension = os.path.splitext(filename)
            counter = 1 # Used to prevent overwriting files with the same name

            while os.path.exists(destination_path): # If a file with the same name already exists, add a counter to the filename
                new_filename = f"{base_name}({counter}){extension}"
                destination_path = os.path.join(destination_folder, new_filename)
                counter += 1

            try:
                shutil.move(file_path, destination_path)
                print(f"Moved {filename} to {destination_path}")

            except Exception as e:
                error_message = f"Error organizing file {filename}: {str(e)}"
                print(error_message)
                return False, error_message

    return True, None
