"""
GUI for the file organizer. All the logic is located in utils/gui_utils.py
"""
import os
import tkinter as tk
import tkinter.ttk as ttk
from utils.json_utils import load_from_json # Importing the FILE_TYPES dictionary from the json_utils file
from utils import gui_utils as utils        # Importing the functions from the utils folder


def create_gui():
    root = tk.Tk()
    root.title("File Organizer")

    # Creating notebook for tabs
    notebook = tk.ttk.Notebook(root)
    notebook.grid(row=0, column=0, sticky="nsew")

    # Creating tabs
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="Organize Files")

    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text="Create New Folder Templates")

    tab3 = ttk.Frame(notebook)
    notebook.add(tab3, text="Delete Folder Templates")

    tab4 = ttk.Frame(notebook)
    notebook.add(tab4, text="Edit Folder Templates")

    # Variables
    source_var = tk.StringVar()
    new_file_type_var = tk.StringVar()
    new_file_extensions_var = tk.StringVar()
    downloads_var = tk.StringVar(value=os.path.join(os.path.expanduser("~"), "Downloads"))
    file_types = load_from_json()

    # Widgets
    source_label = tk.Label(tab1, text="Source Folder:")
    source_entry = tk.Entry(tab1, textvariable=source_var, width=40)
    or_label = tk.Label(tab1, text="...Or Choose A Folder To Organize:", font=("Helvetica", 10, "bold"))

    # Using lambda function to pass parameters to the function
    source_button = tk.Button(tab1, text="Browse", command=lambda: utils.select_folder(source_var))
    organize_button = tk.Button(tab1, text="Organize Chosen Folder", command=lambda: utils.organize_button_clicked(source_var))

    # An alternative button that organizes files from the downloads folder, so the source folder doesn't have to be selected separately
    downloads_label = tk.Label(tab1, text="Organize Downloads Folder Only:", font=("Helvetica", 10, "bold"))
    downloads_button = tk.Button(tab1, text="Organize Downloads", command=lambda: utils.organize_button_clicked(downloads_var))

    # Organize Files layout
    downloads_label.grid(row=0, column=0, padx=10, pady=5)
    or_label.grid(row=2, column=0, padx=10, pady=5)
    downloads_button.grid(row=1, column=0, padx=10, pady=5)
    source_label.grid(row=3, column=0, padx=5, pady=5)
    source_entry.grid(row=4, column=0, padx=5, pady=5)
    source_button.grid(row=4, column=1, padx=5, pady=5)
    organize_button.grid(row=5, column=0, pady=5)

    # Delete Folder templates tab
    delete_file_type_label = tk.Label(tab3, text="Delete A Folder Template (this will not delete existing folders):", font=("Helvetica", 10, "bold"))
    selected_folder_var_delete = tk.StringVar(value=list(file_types.keys())[0])  # Use a different variable name
    folder_name_dropdown_delete = tk.OptionMenu(tab3, selected_folder_var_delete, *file_types.keys())  # Use a different variable name
    delete_filetype_button = tk.Button(tab3, text="Delete Folder Template", command=lambda: utils.delete_folder(selected_folder_var_delete, folder_name_dropdown_delete))  # Use a different variable name

    # Delete Folder templates layout
    delete_file_type_label.grid(row=5, column=0, padx=10, pady=5)
    folder_name_dropdown_delete.grid(row=6, column=0, padx=10, pady=5)
    delete_filetype_button.grid(row=6, column=1, padx=10, pady=5)

    # Callback to update options when the tab is selected
    def update_delete_tab_optmenu(*args):
        print("Updating tab optionmenu")
        utils.update_dropdowns(folder_name_dropdown_delete, selected_folder_var_delete)

    tab3.bind("<Visibility>", update_delete_tab_optmenu)  # Bind the visibility event to the callback


    # Edit Folder templates tab
    edit_file_type_label = tk.Label(tab4, text="Edit Folder Templates (this will not change already created folders):", font=("Helvetica", 10, "bold"))
    selected_folder_var_edit = tk.StringVar(value=list(file_types.keys())[0])
    folder_name_dropdown_edit = tk.OptionMenu(tab4, selected_folder_var_edit, *file_types.keys())
    new_folder_name_entry = tk.Entry(tab4, textvariable=new_file_type_var, width=20)
    new_extensions_entry = tk.Entry(tab4, textvariable=new_file_extensions_var, width=30)
    edit_filetype_button = tk.Button(tab4, text="Edit Folder Template", command=lambda: utils.edit_folder(selected_folder_var_edit, new_folder_name_entry, new_extensions_entry, folder_name_dropdown_edit))
    original_folder_name_var = tk.StringVar()
    original_extensions_var = tk.StringVar()
    new_folder_name_label = tk.Label(tab4, text="New Folder Template Name:", font=("Helvetica", 10, "bold"))
    new_extensions_label = tk.Label(tab4, text="New File Extensions (comma-separated):", font=("Helvetica", 10, "bold"))
    original_folder_name_label = tk.Label(tab4, textvariable=original_folder_name_var)
    original_extensions_label = tk.Label(tab4, textvariable=original_extensions_var)

    #tab4.bind("<Visibility>", lambda _: update_tab_optmenu(folder_name_dropdown_edit, selected_folder_var_edit))  # Bind the visibility event to the callback
    def update_edit_tab_optmenu(*args):
        print("Updating edit tab option menu")
        utils.update_dropdowns(folder_name_dropdown_edit, selected_folder_var_edit)

    tab4.bind("<Visibility>", update_edit_tab_optmenu)

    # New Folder template tab
    add_file_type_label = tk.Label(tab2, text="Add A New Folder Template:", font=("Helvetica", 10, "bold"))
    file_type_label = tk.Label(tab2, text="Folder Template name:")
    folder_name_entry = tk.Entry(tab2, textvariable=new_file_type_var, width=20)
    extension_label = tk.Label(tab2, text="File Extensions (comma-separated):")
    extensions_entry = tk.Entry(tab2, textvariable=new_file_extensions_var, width=30)
    add_filetype_button = tk.Button(tab2, text="Add Folder Template", command=lambda: utils.add_folder(folder_name_entry, extensions_entry, folder_name_dropdown_edit, selected_folder_var_edit))
    
    # New Folder templates layout
    add_file_type_label.grid(row=5, column=0, padx=10, pady=5)
    file_type_label.grid(row=6, column=0, padx=10, pady=5)
    folder_name_entry.grid(row=6, column=1, padx=10, pady=5)
    extension_label.grid(row=7, column=0, padx=10, pady=5)
    extensions_entry.grid(row=7, column=1, padx=10, pady=5)
    add_filetype_button.grid(row=7, column=2, padx=10, pady=5)

    # Binding the update function to the dropdown's selection
    selected_folder_var_delete.trace_add("write", lambda *args: utils.update_labels(selected_folder_var_delete.get(), new_folder_name_entry, new_extensions_entry, original_folder_name_var, original_extensions_var))
    selected_folder_var_edit.trace_add("write", lambda *args: utils.update_labels(selected_folder_var_edit.get(), new_folder_name_entry, new_extensions_entry, original_folder_name_var, original_extensions_var))

    # Prefill the labels and entry fields with the first folder type
    initial_selected_folder = list(file_types.keys())[0]
    utils.update_labels(initial_selected_folder, new_folder_name_entry, new_extensions_entry, original_folder_name_var, original_extensions_var)

    # Edit Folder templates layout
    edit_file_type_label.grid(row=1, column=0, padx=10, pady=5)
    folder_name_dropdown_edit.grid(row=2, column=0, padx=10, pady=5)
    edit_filetype_button.grid(row=2, column=1, padx=10, pady=5)
    new_folder_name_label.grid(row=3, column=0, padx=10, pady=5)
    new_extensions_label.grid(row=3, column=1, padx=10, pady=5)
    new_folder_name_entry.grid(row=4, column=0, padx=10, pady=5)
    new_extensions_entry.grid(row=4, column=1, padx=10, pady=5)
    original_folder_name_label.grid(row=5, column=0, padx=10, pady=5)
    original_extensions_label.grid(row=5, column=1, padx=10, pady=5)

    # Run the GUI
    root.mainloop()


if __name__ == "__main__":
    create_gui()
