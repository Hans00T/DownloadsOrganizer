"""
Karkea versio tiedostojen järjestelijästä. Tavoite on tehdä tästä scriptistä sellainen,
että se järjestää tiedostot downloads-kansiosta eri alikansioihin tiedostotyypin mukaan,
esim. kuvat, videot, dokumentit, ohjelmat, zip-tiedostot jne.
Tämä siistisi downloads-kansion ja helpottaisi tiedostojen löytämistä ja turhien poistoa.
"""
import os
import shutil

def organize_files(source_folder, destination_folder):
    # Tarkista, että lähtö- ja kohdekansiot ovat olemassa
    if not os.path.exists(source_folder) or not os.path.exists(destination_folder):
        raise Exception("Source or destination folder does not exist")
        return
    
    # Käy läpi kaikki tiedostot lähtökansiossa
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Tarkista, että kyseessä on tiedosto
        if os.path.isfile(file_path):
            _, extension = os.path.splitext(filename)

            # Luo kohdekansion, jos sitä ei ole olemassa
            extension_folder = os.path.join(destination_folder, extension[1:].lower())
            os.makedirs(extension_folder, exist_ok=True)

            # Siirrä tiedosto kohdekansioon
            destination_path = os.path.join(extension_folder, filename)
            shutil.move(file_path, destination_path)
            print(f"Moved {filename} to {destination_path}")

if __name__ == "__main__":
    # Pyytää käyttäjältä lähtö- ja kohdekansiot
    source_folder = input("Enter source folder: ")
    destination_folder = input("Enter destination folder: ")

    # Kutsuu funktiota ja järjestelee tiedostot
    organize_files("source", "destination")