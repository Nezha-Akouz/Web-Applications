import tkinter as tk
from tkinter import messagebox, simpledialog
import os


# Classe concrète représentant l'application GUI
class GUIApp():
    def __init__(self):
        #self.tasks = Storage()  # Instance de la classe Storage pour gérer les tâches 
        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.root.geometry("700x500")
        self.root.minsize(480,360)
        file_path = os.path.join(os.getcwd(), "logo.ico")
        #self.root.iconbitmap("logo.ico")
        self.root.iconbitmap(file_path)
        self.root.config(background="#a39e9d")

    def run(self):
        self.setup_gui()
        self.root.mainloop() 


    def setup_gui(self): # Configuration de l'interface utilisateur
        self.frame = tk.Frame(self.root, bg="#a39e9d")
        self.frame.pack(fill="both", expand=True)

        self.title_entry = tk.Entry(self.frame, bg=self.root["background"])
        self.title_entry.pack(pady=10)
        self.title_entry.insert(0, "Title")

        self.desc_entry = tk.Entry(self.frame, bg=self.root["background"])
        self.desc_entry.pack(pady=10)
        self.desc_entry.insert(0, "Description")
