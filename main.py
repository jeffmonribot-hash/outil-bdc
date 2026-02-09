import tkinter as tk
import pandas as pd
import getpass
import os

from pages.accueil import PageAccueil
from pages.bdc import PageBDC
from pages.prestataires import PagePrestataires
from pages.sites import PageSites
from pages.parametres import PageParametres


def charger_utilisateur():
    """
    Identification automatique de l'utilisateur à partir de :
    - login Windows
    - fichier utilisateurs.xlsx
    """
    fichier_users = "utilisateurs.xlsx"

    if not os.path.exists(fichier_users):
        return None

    df = pd.read_excel(fichier_users)

    # Sécurité colonnes
    if "login" not in df.columns or "actif" not in df.columns:
        return None

    login_windows = getpass.getuser().lower()
    df["login"] = df["login"].astype(str).str.lower()
    df["actif"] = df["actif"].astype(str).str.lower()

    ligne = df[
        (df["login"] == login_windows) &
        (df["actif"] == "oui")
    ]

    if ligne.empty:
        return None

    return ligne.iloc[0].to_dict()


class Application(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(fill="both", expand=True)

        # =========================
        # IDENTIFICATION UTILISATEUR
        # =========================
        user = charger_utilisateur()

        self.contexte = {
            "utilisateur": user["Utilisateur"] if user else "Utilisateur non identifié",
            "utilisateur_id": user["ID"] if user else None,
            "secteur": user["secteur"] if user else None,
            "role": user["role"] if user else None,
            "annee": 2026,
            "annees": [2024, 2025, 2026, 2027]
        }

        self.pages = {}

        # =========================
        # ENREGISTREMENT DES PAGES
        # =========================
        for Page in (
            PageAccueil,
            PageBDC,
            PagePrestataires,
            PageSites,
            PageParametres,
        ):
            page_name = Page.__name__
            frame = Page(parent=self, app_context=self)
            self.pages[page_name] = frame
            frame.place(relwidth=1, relheight=1)

        # Page affichée au démarrage
        self.show_page("PageAccueil")

    def show_page(self, page_name):
        self.pages[page_name].tkraise()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gestion des Bons de Commande")
    root.geometry("1200x800")

    app = Application(root)
    root.mainloop()
