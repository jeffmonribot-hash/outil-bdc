import tkinter as tk

from pages.accueil import PageAccueil
from pages.bdc import PageBDC
from pages.prestataires import PagePrestataires
from pages.sites import PageSites
from pages.parametres import PageParametres


class Application(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

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
            frame = Page(parent=self, controller=self)
            self.pages[page_name] = frame
            frame.place(relwidth=1, relheight=1)

        # Page affichée au démarrage
        self.show_page("PageAccueil")

    def show_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()
