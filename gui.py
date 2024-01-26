"""
Käyttöliittymä tiedostojen järjestämiseen
"""
import os
import tkinter as tk
from utils.json_utils import FILE_TYPES
from utils.gui_utils import select_folder, organize_button_clicked, add_file_type


def create_gui():
    root = tk.Tk()
    root.title("File Organizer")

    # Muuttujat
    source_var = tk.StringVar()
    new_file_type_var = tk.StringVar()
    new_file_extensions_var = tk.StringVar()
    downloads_var = tk.StringVar(value=os.path.join(os.path.expanduser("~"), "Downloads"))

    # Widgetit
    source_label = tk.Label(root, text="Source Folder:")
    source_entry = tk.Entry(root, textvariable=source_var, width=40)
    or_label = tk.Label(root, text="...Or Choose A Folder To Organize:", font=("Helvetica", 10, "bold"))

    # Käytetään lambda-funktiota, jotta funktioon voidaan välittää parametreja
    source_button = tk.Button(root, text="Browse", command=lambda: select_folder(source_var))
    organize_button = tk.Button(root, text="Organize Chosen Folder", command=lambda: organize_button_clicked(source_var, FILE_TYPES))

    # Vaihtoehtoinen nappi, joka järjestää tiedostot latauskansiosta, jolloin lähdekansiota ei tarvitse erikseen valita
    downloads_label = tk.Label(root, text="Organize Downloads Folder Only:", font=("Helvetica", 10, "bold"))
    downloads_button = tk.Button(root, text="Organize Downloads", command=lambda: organize_button_clicked(downloads_var, FILE_TYPES))

    # Lisää tiedostotyyppejä
    add_file_type_label = tk.Label(root, text="Add Your Own File Types:", font=("Helvetica", 10, "bold"))
    file_type_label = tk.Label(root, text="Add File Type:")
    file_type_entry = tk.Entry(root, textvariable=new_file_type_var, width=20)
    extension_label = tk.Label(root, text="File Extensions (comma-separated):")
    extensions_entry = tk.Entry(root, textvariable=new_file_extensions_var, width=30)
    add_filetype_button = tk.Button(root, text="Add File Type", command=lambda: add_file_type(file_type_entry, extensions_entry))
    
    # Grid layout
    downloads_label.grid(row=0, column=0, padx=10, pady=5)
    or_label.grid(row=2, column=0, padx=10, pady=5)
    downloads_button.grid(row=1, column=0, padx=10, pady=5)
    source_label.grid(row=3, column=0, padx=5, pady=5)
    source_entry.grid(row=3, column=1, padx=5, pady=5)
    source_button.grid(row=3, column=2, padx=5, pady=5)
    organize_button.grid(row=4, column=1, pady=5)

    # Lisää tiedostotyyppejä -layout
    add_file_type_label.grid(row=5, column=0, padx=10, pady=5)
    file_type_label.grid(row=6, column=0, padx=10, pady=5)
    file_type_entry.grid(row=6, column=1, padx=10, pady=5)
    extension_label.grid(row=7, column=0, padx=10, pady=5)
    extensions_entry.grid(row=7, column=1, padx=10, pady=5)
    add_filetype_button.grid(row=7, column=2, padx=10, pady=5)

    # Käynnistetään ikkuna
    root.mainloop()

    #   TODO: Anna käyttäjän lisätä tiedostotyyppejä käyttöliittymästä
    #   TODO: Anna käyttäjän päättää mihin kansioon tiedosto kuuluu
    #   TODO: Anna käyttäjän määrittää kansioiden nimet ja sijainnit


if __name__ == "__main__":
    create_gui()
