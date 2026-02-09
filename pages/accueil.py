import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class PageAccueil(tk.Frame):
    def __init__(self, parent, app_context):
        super().__init__(parent)

        # 👉 app_context = Application (main.py)
        self.app = app_context

        self.pack(fill="both", expand=True)

        # ===== CANVAS =====
        self.canvas = tk.Canvas(self, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # ===== IMAGE DE FOND =====
        self.original_image = Image.open("assets/fond_accueil_capb.png")
        self.bg_image = ImageTk.PhotoImage(self.original_image)
        self.bg = self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        self.bind("<Configure>", self.redimensionner_fond)

        # ===== TITRE =====
        self.canvas.create_text(
            30, 30,
            text="Outil de gestion des Bons de Commande",
            font=("Arial", 20, "bold"),
            fill="black",
            anchor="w"
        )

        self.canvas.create_text(
            30, 65,
            text="Communauté d’Agglomération Pays Basque",
            font=("Arial", 12),
            fill="black",
            anchor="w"
        )

        # ===== CONTEXTE UTILISATEUR =====
        self.canvas.create_text(
            30, 120,
            text=f"Utilisateur : {self.app.contexte['utilisateur']}",
            anchor="w",
            fill="#222222",
            font=("Arial", 11)
        )

        self.canvas.create_text(
            30, 145,
            text=f"Secteur : {self.app.contexte['secteur']}",
            anchor="w",
            fill="#222222",
            font=("Arial", 11)
        )

        # ===== ANNEE =====
        self.canvas.create_text(
            30, 180,
            text="Année :",
            anchor="w",
            fill="#222222",
            font=("Arial", 11)
        )

        self.combo_annee = ttk.Combobox(
            self,
            values=self.app.contexte["annees"],
            width=10,
            state="readonly"
        )
        self.combo_annee.set(self.app.contexte["annee"])
        self.canvas.create_window(90, 180, window=self.combo_annee, anchor="w")

        # ===== ZONE BOUTONS =====
        self.zone_actions = tk.Frame(self.canvas)
        self.zone_actions_id = self.canvas.create_window(
            0, 0,
            window=self.zone_actions,
            anchor="center"
        )

        style = ttk.Style()
        style.configure("TButton", font=("Arial", 13, "bold"), padding=12)

        ttk.Button(
            self.zone_actions,
            text="📋 Liste des BDC",
            command=self.ouvrir_liste_bdc,
            width=28
        ).pack(pady=10)

        ttk.Button(
            self.zone_actions,
            text="➕ Nouveau BDC",
            command=self.ouvrir_nouveau_bdc,
            width=28
        ).pack(pady=10)

        ttk.Button(
            self.zone_actions,
            text="⚙️ Paramètres",
            command=self.ouvrir_parametres,
            width=28
        ).pack(pady=10)

    # ===== REDIMENSIONNEMENT =====
    def redimensionner_fond(self, event):
        largeur = event.width
        hauteur = event.height

        image_redim = self.original_image.resize((largeur, hauteur))
        self.bg_image = ImageTk.PhotoImage(image_redim)
        self.canvas.itemconfig(self.bg, image=self.bg_image)

        self.canvas.coords(self.zone_actions_id, largeur / 2, hauteur / 2 + 60)

    # ===== ACTIONS =====
    def ouvrir_liste_bdc(self):
        self.app.show_page("PageBDC")

    def ouvrir_nouveau_bdc(self):
        from pages.nouveau_bdc import NouveauBDC
        NouveauBDC(self, self.app)

    def ouvrir_parametres(self):
        self.app.show_page("PageParametres")
