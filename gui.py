"""
Käyttöliittymä tiedostojen järjestämiseen
"""
import os
import json
import tkinter as tk
from tkinter import messagebox, filedialog
from file_organizer_logic import organize_files


# Lataa tiedostotyypit json-tiedostosta.
with open('file_types.json') as f:
    FILE_TYPES = json.load(f)
    #   TODO: Anna käyttäjän lisätä tiedostotyyppejä käyttöliittymästä
    #   TODO: Anna käyttäjän päättää mihin kansioon tiedosto kuuluu
    #   TODO: Anna käyttäjän määrittää kansioiden nimet ja sijainnit


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


def show_notification(title, message):
    messagebox.showinfo(title, message)


def create_gui():
    root = tk.Tk()
    root.title("File Organizer")

    # Muuttujat
    source_var = tk.StringVar()
    downloads_var = tk.StringVar(value=os.path.join(os.path.expanduser("~"), "Downloads"))

    # Widgetit
    source_label = tk.Label(root, text="Source Folder:")
    source_entry = tk.Entry(root, textvariable=source_var, width=40)
    or_label = tk.Label(root, text="...Or Choose A Folder To Organize:", font=("Helvetica", 10, "bold"))

    # Käytetään lambda-funktiota, jotta funktioon voidaan välittää parametreja
    source_button = tk.Button(root, text="Browse", command=lambda: select_folder(source_var))
    organize_button = tk.Button(root, text="Organize Chosen Folder", command=lambda: organize_button_clicked(source_var, FILE_TYPES))

    # Vaihtoehtoinen nappi, joka järjestää tiedostot latauskansiosta, jolloin lähdekansiota ei tarvitse erikseen valita
    downloads_button = tk.Button(root, text="Organize Downloads Only", command=lambda: organize_button_clicked(downloads_var, FILE_TYPES))

    # Grid layout
    or_label.grid(row=2, column=1, pady=20)
    downloads_button.grid(row=1, column=1, pady=20)
    source_label.grid(row=3, column=0, padx=10, pady=10)
    source_entry.grid(row=3, column=1, padx=10, pady=10)
    source_button.grid(row=3, column=2, padx=10, pady=10)
    organize_button.grid(row=4, column=1, pady=20)

    # Käynnistetään ikkuna
    root.mainloop()


if __name__ == "__main__":
    create_gui()
