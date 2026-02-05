import tkinter as tk


class PageAccueil(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # --- TITRES ---
        titre = tk.Label(
            self,
            text="Outil de gestion des Bons de Commande",
            font=("Arial", 22, "bold")
        )
        titre.pack(pady=40)

        sous_titre = tk.Label(
            self,
            text="Communauté d’Agglomération Pays Basque",
            font=("Arial", 14)
        )
        sous_titre.pack(pady=10)

        # --- ZONE DES BOUTONS ---
        zone_btn = tk.Frame(self)
        zone_btn.pack(pady=60)

        boutons = [
            ("Bons de commande", "PageBDC"),
            ("Prestataires", "PagePrestataires"),
            ("Sites", "PageSites"),
            ("Paramètres", "PageParametres"),
        ]

        for texte, page in boutons:
            btn = tk.Button(
                zone_btn,
                text=texte,
                width=30,
                height=2,
                command=lambda p=page: controller.show_page(p)
            )
            btn.pack(pady=8)
