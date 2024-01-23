"""
Tämän scriptin tavoite on järjestellä tiedostoja Downloads-kansiosta.
Tarkoitus on järjestää tiedostot downloads-kansiosta eri alikansioihin tiedostotyypin mukaan,
esim. kuvat, videot, dokumentit, ohjelmat, zip-tiedostot jne.
Tämä siistisi downloads-kansion ja helpottaisi tiedostojen löytämistä ja turhien poistoa.
"""

import os
import shutil

def organize_files(downloads_folder):
    # Tarkista, että lähtö- ja kohdekansiot ovat olemassa
    if not os.path.exists(downloads_folder):
        print("Source folder does not exist")
    
    file_types = {
        "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "videos": [".mp4", ".avi", ".mov", ".mkv"],
        "documents": [".doc", ".docx", ".pdf", ".txt"],
        "programs": [".exe", ".msi"],
        "zip": [".zip", ".rar", ".tar", ".gz"],
        "data": [".csv", ".xlsx", ".xls", ".json", ".xml"]
    }
    
    # Käy läpi kaikki tiedostot lähtökansiossa
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)

        # Tarkista, että kyseessä on tiedosto
        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(filename)
            extension = file_extension.lower()   # muuttaa kirjaimet pieniksi varmuuden varalta

            # Päätä mihin kansioon tiedosto kuuluu tiedostopäätteen perusteella
            folder_name = "other"
            for file_type, extensions_list in file_types.items():
                if extension in extensions_list:
                    folder_name = file_type
                    break

            # Luo kohdekansion, jos sitä ei ole olemassa
            destination_folder = os.path.join(downloads_folder, folder_name)
            os.makedirs(destination_folder, exist_ok=True)

            # Siirrä tiedosto kohdekansioon
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(file_path, destination_path)
            print(f"Moved {filename} to {destination_path}")

            # TODO: Jos kohdekansiossa on jo samanniminen tiedosto, niin lisää tiedoston nimeen (1), (2) jne.

if __name__ == "__main__":
    # Etsii Downloads-kansion
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # Kutsuu funktiota ja järjestelee tiedostot
    organize_files(downloads_folder)
