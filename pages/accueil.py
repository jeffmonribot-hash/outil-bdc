import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class PageAccueil(tk.Frame):
    def __init__(self, parent, app_context):
        super().__init__(parent)

        self.app_context = app_context
        self.pack(fill="both", expand=True)

        # ===== CANVAS =====
        self.canvas = tk.Canvas(self, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # ===== IMAGE DE FOND =====
        self.original_image = Image.open("assets/fond_accueil_capb.png")
        self.bg_image = ImageTk.PhotoImage(self.original_image)
        self.bg = self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        # Redimensionnement automatique
        self.bind("<Configure>", self.redimensionner_fond)

        # ===== BANDEAU TITRE =====
        self.canvas.create_text(
            450, 40,
            text="Outil de gestion des Bons de Commande",
            font=("Arial", 20, "bold"),
            fill="white"
        )

        self.canvas.create_text(
            450, 70,
            text="Communauté d’Agglomération Pays Basque",
            font=("Arial", 12),
            fill="white"
        )

        # ===== UTILISATEUR =====
        self.canvas.create_text(
            20, 120,
            text=f"Utilisateur : {app_context['utilisateur']}",
            anchor="w",
            fill="white",
            font=("Arial", 11)
        )

        self.canvas.create_text(
            20, 145,
            text=f"Secteur : {app_context['secteur']}",
            anchor="w",
            fill="white",
            font=("Arial", 11)
        )

        # ===== ANNEE =====
        self.canvas.create_text(
            20, 190,
            text="Année :",
            anchor="w",
            fill="white",
            font=("Arial", 11)
        )

        self.combo_annee = ttk.Combobox(
            self,
            values=app_context["annees"],
            width=10
        )
        self.combo_annee.set(app_context["annee"])
        self.canvas.create_window(80, 190, window=self.combo_annee, anchor="w")

        # ===== ZONE ACTIONS (CENTREE) =====
        self.zone_actions = tk.Frame(self.canvas, bg="", bd=0)
        self.canvas.create_window(450, 330, window=self.zone_actions)

        # Style des boutons
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12, "bold"), padding=10)

        # ===== BOUTONS =====
        self.bouton_liste = ttk.Button(
            self.zone_actions,
            text="📋 Liste des BDC",
            command=self.ouvrir_liste_bdc,
            width=25
        )
        self.bouton_liste.pack(pady=10)

        self.bouton_nouveau = ttk.Button(
            self.zone_actions,
            text="➕ Nouveau BDC",
            command=self.ouvrir_nouveau_bdc,
            width=25
        )
        self.bouton_nouveau.pack(pady=10)

        self.bouton_parametres = ttk.Button(
            self.zone_actions,
            text="⚙️ Paramètres",
            command=self.ouvrir_parametres,
            width=25
        )
        self.bouton_parametres.pack(pady=10)

    # ===== REDIMENSIONNEMENT DU FOND =====
    def redimensionner_fond(self, event):
        largeur = event.width
        hauteur = event.height

        image_redim = self.original_image.resize((largeur, hauteur))
        self.bg_image = ImageTk.PhotoImage(image_redim)
        self.canvas.itemconfig(self.bg, image=self.bg_image)

    # ===== ACTIONS (VIDES POUR L’INSTANT) =====
    def ouvrir_liste_bdc(self):
        print("Ouverture de la liste des BDC")

    def ouvrir_nouveau_bdc(self):
        print("Ouverture de la fenêtre Nouveau BDC")

    def ouvrir_parametres(self):
        print("Ouverture des paramètres")
