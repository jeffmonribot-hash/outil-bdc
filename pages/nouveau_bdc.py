import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os

from data.marches import get_marches_actifs


class NouveauBDC(tk.Toplevel):
    def __init__(self, parent, app_context):
        super().__init__(parent)

        self.app = app_context
        self.title("Nouveau Bon de Commande")
        self.geometry("720x560")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

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

        self.chemin_site_selectionne = None

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
            tk.Label(frame, text=label, width=20, anchor="w").pack(side="left")
            widget.pack(side="left", fill="x", expand=True)

        self.combo_prestataire = ttk.Combobox(container, textvariable=self.var_prestataire, state="readonly")
        self.combo_site = ttk.Combobox(container, textvariable=self.var_site, state="readonly")

        ligne("Désignation :", ttk.Entry(container, textvariable=self.var_designation))
        ligne("Prestataire :", self.combo_prestataire)
        ligne("Site / Bâtiment :", self.combo_site)
        ligne("Marché :", ttk.Combobox(container, textvariable=self.var_marche,
                                       values=get_marches_actifs(), state="readonly"))
        ligne("Montant HT :", ttk.Entry(container, textvariable=self.var_montant))

        # =========================
        # CONTEXTE
        # =========================
        tk.Label(
            container,
            text=f"Utilisateur : {self.app.contexte['utilisateur']}  |  "
                 f"Secteur : {self.app.contexte['secteur']}  |  "
                 f"Année : {self.app.contexte['annee']}",
            font=("Arial", 10, "italic")
        ).pack(anchor="w", pady=10)

        # =========================
        # PIECE JOINTE
        # =========================
        tk.Label(container, text="Pièce jointe", font=("Arial", 12, "bold")).pack(anchor="w", pady=(15, 5))

        frame_pj = tk.Frame(container)
        frame_pj.pack(fill="x")

        ttk.Radiobutton(frame_pj, text="Depuis Outlook", variable=self.var_mode_pj,
                        value="OUTLOOK").pack(side="left", padx=10)
        ttk.Radiobutton(frame_pj, text="Depuis un dossier", variable=self.var_mode_pj,
                        value="DOSSIER").pack(side="left", padx=10)

        ttk.Button(container, text="📎 Sélectionner la pièce jointe",
                   command=self.gerer_piece_jointe).pack(anchor="w", pady=8)

        tk.Label(container, textvariable=self.var_nom_fichier).pack(anchor="w")
        tk.Label(container, textvariable=self.var_chemin_fichier,
                 wraplength=680, justify="left", font=("Arial", 9), fg="#555").pack(anchor="w")

        # =========================
        # BOUTONS
        # =========================
        frame_actions = tk.Frame(self)
        frame_actions.pack(pady=15)

        ttk.Button(frame_actions, text="💾 Enregistrer", width=18,
                   command=self.enregistrer).pack(side="left", padx=10)
        ttk.Button(frame_actions, text="❌ Annuler", width=18,
                   command=self.destroy).pack(side="left", padx=10)

        # =========================
        # CHARGEMENT DES DONNÉES
        # =========================
        self.charger_prestataires()
        self.charger_sites_filtres()

        self.combo_site.bind("<<ComboboxSelected>>", self._site_change)

    # ==================================================
    # CHARGEMENT PRESTATAIRES
    # ==================================================
    def charger_prestataires(self):
        try:
            df = pd.read_excel("prestataires.xlsx")
            self.combo_prestataire["values"] = sorted(df["Tiers"].dropna().tolist())
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de charger les prestataires\n{e}")

    # ==================================================
    # CHARGEMENT SITES FILTRÉS
    # ==================================================
    def charger_sites_filtres(self):
        try:
            df_sites = pd.read_excel("sites.xlsx")
            df_users = pd.read_excel("utilisateurs.xlsx")

            utilisateur_nom = self.app.contexte["utilisateur"]

            user = df_users[
                (df_users["Utilisateur"] == utilisateur_nom) &
                (df_users["actif"].str.lower() == "oui")
            ].iloc[0]

            role = user["role"].lower()
            secteur = user["secteur "]
            user_id = user["ID"]

            df_sites = df_sites[df_sites["actif"].str.lower() == "oui"]

            if role == "agent":
                df_sites = df_sites[df_sites["Technicien_ID"] == user_id]
            else:  # responsable
                df_sites = df_sites[df_sites["Secteur"] == secteur]

            self.df_sites_filtres = df_sites
            self.combo_site["values"] = sorted(df_sites["BAT"].tolist())

        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de charger les sites\n{e}")

    # ==================================================
    # CHANGEMENT DE SITE
    # ==================================================
    def _site_change(self, event=None):
        bat = self.var_site.get()
        ligne = self.df_sites_filtres[self.df_sites_filtres["BAT"] == bat]
        if not ligne.empty:
            self.chemin_site_selectionne = ligne.iloc[0]["DOSSIER"]

    # ==================================================
    # PIECE JOINTE
    # ==================================================
    def gerer_piece_jointe(self):
        if self.var_mode_pj.get() == "OUTLOOK":
            messagebox.showinfo(
                "Outlook",
                "Outlook sera géré à l’étape suivante.\n\n"
                "• Mail sélectionné\n"
                "• Choix de la PJ si plusieurs\n"
                "• Copie dans le dossier"
            )
            return

        dossier_depart = self.chemin_site_selectionne if self.chemin_site_selectionne else os.getcwd()

        fichier = filedialog.askopenfilename(
            title="Sélectionner la pièce jointe",
            initialdir=dossier_depart
        )
        if fichier:
            self.var_chemin_fichier.set(fichier)
            self.var_nom_fichier.set(os.path.basename(fichier))

    # ==================================================
    # ENREGISTREMENT (HOOK)
    # ==================================================
    def enregistrer(self):
        if not self.var_designation.get():
            messagebox.showwarning("Champ obligatoire", "La désignation est obligatoire.")
            return

        print("BDC prêt :")
        print("Désignation :", self.var_designation.get())
        print("Prestataire :", self.var_prestataire.get())
        print("Site :", self.var_site.get())
        print("Marché :", self.var_marche.get())
        print("Montant HT :", self.var_montant.get())
        print("Fichier :", self.var_chemin_fichier.get())

        self.destroy()
