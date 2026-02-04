import tkinter as tk
from pages.accueil import PageAccueil


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # Titre de la fenêtre
        self.title("Outil de gestion des BDC – CAPB")

        # Taille de la fenêtre (pas trop petite 😉)
        self.geometry("900x600")

        # Empêche une fenêtre minuscule
        self.minsize(800, 500)

        # Conteneur principal
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Affichage de la page d'accueil
        accueil = PageAccueil(self.container)
        accueil.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = Application()
    app.mainloop()

