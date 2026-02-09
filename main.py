import tkinter as tk

from pages.accueil import PageAccueil
from pages.bdc import PageBDC
from pages.prestataires import PagePrestataires
from pages.sites import PageSites
from pages.parametres import PageParametres


class Application(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(fill="both", expand=True)

        # CONTEXTE GLOBAL (temporaire pour tests)
        self.contexte = {
            "utilisateur": "user_001",
            "utilisateur_id": "user_001",
            "secteur": "Labourd Nord",
            "annee": 2026,
            "annees": [2024, 2025, 2026, 2027]
        }

        self.pages = {}

        # Enregistrement des pages
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
