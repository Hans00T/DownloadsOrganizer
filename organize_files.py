"""
Karkea versio tiedostojen järjestelijästä. Tavoite on tehdä tästä scriptistä sellainen,
että se järjestää tiedostot downloads-kansiosta eri alikansioihin tiedostotyypin mukaan,
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
        "zip": [".zip", ".rar", ".tar", ".gz"]
    }
    
    # Käy läpi kaikki tiedostot lähtökansiossa
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)

        # Tarkista, että kyseessä on tiedosto
        if os.path.isfile(file_path):
            _, extension = os.path.splitext(filename)
            extension = extension[1:].lower()   # poistaa pisteen tiedostopäätteestä ja muuttaa kirjaimet pieniksi

            # Päätä mihin kansioon tiedosto kuuluu tiedostopäätteen perusteella
            if extension in file_types["images"]:
                folder_name = "images"
            elif extension in file_types["videos"]:
                folder_name = "videos"
            elif extension in file_types["documents"]:
                folder_name = "documents"
            elif extension in file_types["programs"]:
                folder_name = "programs"
            elif extension in file_types["zip"]:
                folder_name = "zip"
            else:
                folder_name = "other"

            # Luo kohdekansion, jos sitä ei ole olemassa
            destination_folder = os.path.join(downloads_folder, folder_name)
            os.makedirs(destination_folder, exist_ok=True)

            # Siirrä tiedosto kohdekansioon
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(file_path, destination_path)
            print(f"Moved {filename} to {destination_path}")

if __name__ == "__main__":
    # Etsii Downloads-kansion
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # Kutsuu funktiota ja järjestelee tiedostot
    organize_files(downloads_folder)