import json
import os
import tkinter as tk
from tkinter import ttk, messagebox

FICHIER_FILMS = "films.json"

def charger_films():
    if os.path.exists(FICHIER_FILMS):
        try:
            with open(FICHIER_FILMS, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def sauvegarder_films(films):
    with open(FICHIER_FILMS, "w", encoding="utf-8") as f:
        json.dump(films, f, ensure_ascii=False, indent=4)

class MovieApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Enregistrer un film")
        self.geometry("350x200")
        self.resizable(False, False)

        self.films = charger_films()
        self.creer_interface()

    def creer_interface(self):
        ttk.Label(self, text="Nom du film :").pack(pady=5)
        self.var_titre = tk.StringVar()
        ttk.Entry(self, textvariable=self.var_titre, width=40).pack()

        ttk.Label(self, text="Année :").pack(pady=5)
        self.var_annee = tk.StringVar()
        ttk.Entry(self, textvariable=self.var_annee, width=10).pack()

        ttk.Button(self, text="Ajouter", command=self.ajouter_film).pack(pady=10)

    def ajouter_film(self):
        titre = self.var_titre.get().strip()
        annee = self.var_annee.get().strip()

        if not titre:
            messagebox.showwarning("Erreur", "Le nom du film est obligatoire.")
            return
        if annee and not annee.isdigit():
            messagebox.showwarning("Erreur", "L'année doit être un nombre.")
            return

        # Vérifie les doublons
        for film in self.films:
            if film["title"].lower() == titre.lower() and film["year"] == annee:
                messagebox.showinfo("Doublon", "Ce film est déjà enregistré.")
                return

        self.films.append({"title": titre, "year": annee})
        sauvegarder_films(self.films)

        messagebox.showinfo("Succès", f"« {titre} » ajouté.")
        self.var_titre.set("")
        self.var_annee.set("")

if __name__ == "__main__":
    app = MovieApp()
    app.mainloop()
