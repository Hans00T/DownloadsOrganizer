"""
This is the main file of the program. It is used to run the program.
"""
import os, sys

# Add the project root directory to the path so that the module can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gui.gui import create_gui


if __name__ == "__main__":
    create_gui()
