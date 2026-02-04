import tkinter as tk


class PageAccueil(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Titre du logiciel
        titre = tk.Label(
            self,
            text="Outil de gestion des Bons de Commande",
            font=("Arial", 20, "bold")
        )
        titre.pack(pady=20)

        sous_titre = tk.Label(
            self,
            text="Communauté d’Agglomération Pays Basque",
            font=("Arial", 14)
        )
        sous_titre.pack(pady=10)

        # Zone boutons
        zone_boutons = tk.Frame(self)
        zone_boutons.pack(pady=40)

        # Boutons principaux
        boutons = [
            "Bons de commande",
            "Sites",
            "Prestataires",
            "Paramètres"
        ]

        for texte in boutons:
            btn = tk.Button(
                zone_boutons,
                text=texte,
                width=25,
                height=2
            )
            btn.pack(pady=8)

