"""Interface pour consulter la liste des films enregistrés.

Ce module charge les films depuis un fichier JSON et les affiche dans
une liste défilante au format ``année - titre``.
"""

from __future__ import annotations

import json
import os
import tkinter as tk
from tkinter import ttk

FICHIER_FILMS = "films.json"


def charger_films() -> list[dict]:
    """Retourne la liste des films stockés dans ``FICHIER_FILMS``.

    Si le fichier n'existe pas ou contient un JSON invalide, une liste vide
    est renvoyée.
    """

    if os.path.exists(FICHIER_FILMS):
        try:
            with open(FICHIER_FILMS, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


class ConsulterApp(tk.Tk):
    """Fenêtre principale affichant les films dans une liste défilante."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Films enregistrés")
        self.geometry("300x400")
        self.resizable(False, False)

        films = charger_films()

        frame = ttk.Frame(self)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        scrollbar = ttk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=self.listbox.yview)

        for film in films:
            titre = film.get("title") or film.get("titre", "")
            annee = film.get("year") or film.get("année", "")
            ligne = f"{annee} - {titre}" if annee else titre
            self.listbox.insert(tk.END, ligne)


if __name__ == "__main__":
    app = ConsulterApp()
    app.mainloop()

