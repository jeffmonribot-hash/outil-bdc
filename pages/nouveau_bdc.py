import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import datetime

from data.marches import get_marches_actifs


class NouveauBDC(tk.Toplevel):
    def __init__(self, parent, app_context):
        super().__init__(parent)

        self.app = app_context
        self.title("Nouveau Bon de Commande")
        self.geometry("700x520")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()  # modal

        # =========================
        # VARIABLES
        # =========================
        self.var_designation = tk.StringVar()
        self.var_prestataire = tk.StringVar()
        self.var_site = tk.StringVar()
        self.var_marche = tk.StringVar()
        self.var_montant = tk.StringVar()

        self.var_mode_pj = tk.StringVar(value="DOSSIER")
        self.var_nom_fichier = tk.StringVar()
        self.var_chemin_fichier = tk.StringVar()

        # =========================
        # TITRE
        # =========================
        tk.Label(
            self,
            text="Création d’un nouveau Bon de Commande",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        container = tk.Frame(self)
        container.pack(fill="both", expand=True, padx=20)

        # =========================
        # FORMULAIRE
        # =========================
        def ligne(label, widget):
            frame = tk.Frame(container)
            frame.pack(fill="x", pady=6)
            tk.Label(frame, text=label, width=18, anchor="w").pack(side="left")
            widget.pack(side="left", fill="x", expand=True)

        ligne("Désignation :", ttk.Entry(container, textvariable=self.var_designation))
        ligne("Prestataire :", ttk.Combobox(container, textvariable=self.var_prestataire, state="readonly"))
        ligne("Site / Bâtiment :", ttk.Combobox(container, textvariable=self.var_site, state="readonly"))
        ligne("Marché :", ttk.Combobox(container, textvariable=self.var_marche,
                                       values=get_marches_actifs(), state="readonly"))
        ligne("Montant HT :", ttk.Entry(container, textvariable=self.var_montant))

        # =========================
        # INFOS CONTEXTE
        # =========================
        frame_info = tk.Frame(container)
        frame_info.pack(fill="x", pady=10)

        tk.Label(
            frame_info,
            text=f"Utilisateur : {self.app.contexte['utilisateur']}  |  "
                 f"Secteur : {self.app.contexte['secteur']}  |  "
                 f"Année : {self.app.contexte['annee']}",
            font=("Arial", 10, "italic")
        ).pack(anchor="w")

        # =========================
        # PIECE JOINTE
        # =========================
        tk.Label(container, text="Pièce jointe", font=("Arial", 12, "bold")).pack(anchor="w", pady=(15, 5))

        frame_pj = tk.Frame(container)
        frame_pj.pack(fill="x")

        ttk.Radiobutton(
            frame_pj, text="Depuis Outlook", variable=self.var_mode_pj, value="OUTLOOK"
        ).pack(side="left", padx=10)

        ttk.Radiobutton(
            frame_pj, text="Depuis un dossier", variable=self.var_mode_pj, value="DOSSIER"
        ).pack(side="left", padx=10)

        frame_btn_pj = tk.Frame(container)
        frame_btn_pj.pack(fill="x", pady=8)

        ttk.Button(frame_btn_pj, text="📎 Récupérer la pièce jointe",
                   command=self.gerer_piece_jointe).pack(side="left")

        tk.Label(container, textvariable=self.var_nom_fichier).pack(anchor="w")
        tk.Label(container, textvariable=self.var_chemin_fichier,
                 font=("Arial", 9), fg="#555555", wraplength=650, justify="left").pack(anchor="w")

        # =========================
        # BOUTONS
        # =========================
        frame_actions = tk.Frame(self)
        frame_actions.pack(pady=15)

        ttk.Button(frame_actions, text="💾 Enregistrer", width=18,
                   command=self.enregistrer).pack(side="left", padx=10)
        ttk.Button(frame_actions, text="❌ Annuler", width=18,
                   command=self.destroy).pack(side="left", padx=10)

    # ==================================================
    # PIECE JOINTE
    # ==================================================
    def gerer_piece_jointe(self):
        mode = self.var_mode_pj.get()

        if mode == "OUTLOOK":
            messagebox.showinfo(
                "Outlook",
                "Récupération Outlook à implémenter.\n\n"
                "• Outlook ouvert\n"
                "• Mail sélectionné\n"
                "• Choix de la PJ si plusieurs"
            )
            return

        # MODE DOSSIER
        fichier = filedialog.askopenfilename(title="Sélectionner la pièce jointe")
        if fichier:
            self.var_chemin_fichier.set(fichier)
            self.var_nom_fichier.set(fichier.split("/")[-1])

    # ==================================================
    # ENREGISTREMENT (HOOK)
    # ==================================================
    def enregistrer(self):
        if not self.var_designation.get():
            messagebox.showwarning("Champ obligatoire", "La désignation est obligatoire.")
            return

        # À CE STADE : simple contrôle + fermeture
        print("BDC prêt à être enregistré :")
        print("Désignation :", self.var_designation.get())
        print("Prestataire :", self.var_prestataire.get())
        print("Site :", self.var_site.get())
        print("Marché :", self.var_marche.get())
        print("Montant HT :", self.var_montant.get())
        print("Fichier :", self.var_chemin_fichier.get())

        self.destroy()

