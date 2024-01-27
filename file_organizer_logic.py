"""
Logic for the file organizer
"""
import os
import shutil


def organize_files(downloads_folder, file_types):
    # Checks that the source folder exists
    if not os.path.exists(downloads_folder):
        print("Source folder does not exist")
        return False, "Source folder does not exist"
    
    # Checks that the source folder is not empty
    if not any(os.path.isfile(os.path.join(downloads_folder, f)) for f in os.listdir(downloads_folder)):
        print("Source folder is empty")
        return False, "Source folder is empty"
    
    # Loops through all the files in the source folder
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)

        # Checks that the file is not a folder
        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(filename)
            extension = file_extension.lower()   # changes the file extension to lowercase just in case

            # Chooses the folder name based on the file extension, chooses "other" if the extension is not set in the dictionary
            folder_name = "other"
            for file_type, extensions_list in file_types.items():
                if extension in extensions_list:
                    folder_name = file_type
                    break

            # Creates the destination folder if it doesn't exist
            destination_folder = os.path.join(downloads_folder, folder_name)
            os.makedirs(destination_folder, exist_ok=True)

            # Handles duplicate files
            destination_path = os.path.join(destination_folder, filename)
            base_name, extension = os.path.splitext(filename)
            counter = 1

            # If the file already exists, add a number to the end of the filename
            while os.path.exists(destination_path): 
                new_filename = f"{base_name}({counter}){extension}"
                destination_path = os.path.join(destination_folder, new_filename)
                counter += 1

            try:
                # Moves the file to the destination folder
                shutil.move(file_path, destination_path)
                print(f"Moved {filename} to {destination_path}")

            except Exception as e:
                error_message = f"Error organizing file {filename}: {str(e)}"
                print(error_message)
                return False, error_message

    return True, None
