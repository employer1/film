import tkinter as tk
import subprocess
import sys

def run_ajouter():
    """Execute ajouter.py using the current Python interpreter."""
    subprocess.run([sys.executable, "ajouter.py"])

def run_consulter():
    """Execute consulter.py using the current Python interpreter."""
    subprocess.run([sys.executable, "consulter.py"])

root = tk.Tk()
root.title("Gestion des films")

# Title label
label = tk.Label(root, text="Gestion des films", font=("Helvetica", 16))
label.pack(padx=20, pady=20)

# Buttons
ajouter_button = tk.Button(root, text="Ajouter", command=run_ajouter)
ajouter_button.pack(fill="x", padx=20, pady=5)

consulter_button = tk.Button(root, text="Consulter", command=run_consulter)
consulter_button.pack(fill="x", padx=20, pady=5)

root.mainloop()
