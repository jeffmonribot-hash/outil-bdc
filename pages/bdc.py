import tkinter as tk
from tkinter import ttk
import pandas as pd
import os

from data.statuts_bdc import get_statuts_labels, get_couleur_par_label


class PageBDC(tk.Frame):
    def __init__(self, parent, app_context):
        super().__init__(parent)

        self.app = app_context
        self.pack(fill="both", expand=True)

        # ===== TITRE =====
        titre = tk.Label(
            self,
            text="Liste des Bons de Commande",
            font=("Arial", 19, "bold")
        )
        titre.pack(pady=15)

        # ===== STYLE TABLEAU =====
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 11), rowheight=28)
        style.configure("Treeview.Heading", font=("Arial", 11, "bold"))

        # ===== CONTENEUR TABLEAU =====
        frame_table = tk.Frame(self)
        frame_table.pack(fill="both", expand=True, padx=20, pady=10)

        colonnes = (
            "statut",
            "designation",
            "prestataire",
            "site",
            "montant",
            "marche",
            "devis",
            "numero",
        )

        self.table = ttk.Treeview(
            frame_table,
            columns=colonnes,
            show="headings"
        )

        # ===== EN-TÊTES =====
        self.table.heading("statut", text="Statut")
        self.table.heading("designation", text="Désignation")
        self.table.heading("prestataire", text="Prestataire")
        self.table.heading("site", text="Site")
        self.table.heading("montant", text="Montant HT")
        self.table.heading("marche", text="Marché")
        self.table.heading("devis", text="Devis")
        self.table.heading("numero", text="N° BDC")

        # ===== LARGEURS =====
        self.table.column("statut", width=160, anchor="center")
        self.table.column("designation", width=320)
        self.table.column("prestataire", width=200)
        self.table.column("site", width=220)
        self.table.column("montant", width=130, anchor="e")
        self.table.column("marche", width=180)
        self.table.column("devis", width=110, anchor="center")
        self.table.column("numero", width=130, anchor="center")

        # ===== SCROLLBAR =====
        scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)

        self.table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Double-clic pour éditer le statut
        self.table.bind("<Double-1>", self.editer_cellule)

        # ===== BOUTONS =====
        frame_actions = tk.Frame(self)
        frame_actions.pack(pady=15)

        ttk.Button(frame_actions, text="➕ Nouveau BDC", width=20, command=self.nouveau_bdc).pack(side="left", padx=10)
        ttk.Button(frame_actions, text="✏️ Modifier", width=20, command=self.modifier_bdc).pack(side="left", padx=10)
        ttk.Button(frame_actions, text="👁️ Consulter", width=20, command=self.consulter_bdc).pack(side="left", padx=10)
        ttk.Button(frame_actions, text="⬅ Retour accueil", width=20, command=self.retour_accueil).pack(side="left", padx=10)

        # ===== CHARGEMENT DES DONNÉES =====
        self.charger_bdc_depuis_excel()

    # ==========================================================
    # CHARGEMENT DES BDC DEPUIS EXCEL
    # ==========================================================
    def charger_bdc_depuis_excel(self):
        chemin = os.path.join("donnees", "bdc.xlsx")

        print("Chemin BDC utilisé :", os.path.abspath(chemin))

        if not os.path.exists(chemin):
            print("❌ Fichier BDC introuvable")
            return

        df = pd.read_excel(chemin)

        # Nettoyage du tableau
        for row in self.table.get_children():
            self.table.delete(row)

        # Remplissage depuis Excel + couleur statut
        for _, ligne in df.iterrows():
            statut = ligne.get("Statut du BC", "")
            couleur = get_couleur_par_label(statut)

            item_id = self.table.insert(
                "",
                "end",
                values=(
                    statut,
                    ligne.get("DESIGNATION", ""),
                    ligne.get("Prestataire", ""),
                    ligne.get("Site", ""),
                    ligne.get("MONTANT HT2", ""),
                    ligne.get("Marché", ""),
                    "Oui" if pd.notna(ligne.get("chemin devis")) else "Non",
                    ligne.get("NUMERO BDC", "")
                )
            )

            self.table.tag_configure(statut, foreground=couleur)
            self.table.item(item_id, tags=(statut,))

    # ==========================================================
    # ÉDITION DU STATUT (DOUBLE-CLIC)
    # ==========================================================
    def editer_cellule(self, event):
        region = self.table.identify("region", event.x, event.y)
        if region != "cell":
            return

        col = self.table.identify_column(event.x)
        row_id = self.table.identify_row(event.y)

        # On n'édite que la colonne Statut
        if col != "#1" or not row_id:
            return

        bbox = self.table.bbox(row_id, col)
        if not bbox:
            return

        x, y, w, h = bbox

        valeur_actuelle = self.table.set(row_id, "statut")
        liste_statuts = get_statuts_labels()

        combo = ttk.Combobox(
            self.table,
            values=liste_statuts,
            state="readonly"
        )
        combo.set(valeur_actuelle if valeur_actuelle in liste_statuts else liste_statuts[0])
        combo.place(x=x, y=y, width=w, height=h)
        combo.focus_set()

        def valider(_event=None):
            nouveau_statut = combo.get()
            self.table.set(row_id, "statut", nouveau_statut)

            couleur = get_couleur_par_label(nouveau_statut)
            self.table.tag_configure(nouveau_statut, foreground=couleur)
            self.table.item(row_id, tags=(nouveau_statut,))

            combo.destroy()

        combo.bind("<<ComboboxSelected>>", valider)
        combo.bind("<Return>", valider)
        combo.bind("<Escape>", lambda e: combo.destroy())
        combo.bind("<FocusOut>", lambda e: combo.destroy())

    # ==========================================================
    # OUTILS
    # ==========================================================
    def _get_selection(self):
        selection = self.table.selection()
        if not selection:
            return None
        return self.table.item(selection[0])["values"]

    # ==========================================================
    # ACTIONS
    # ==========================================================
    def nouveau_bdc(self):
        print("Nouveau BDC (à venir)")

    def modifier_bdc(self):
        print("Modifier BDC :", self._get_selection())

    def consulter_bdc(self):
        print("Consulter BDC :", self._get_selection())

    def retour_accueil(self):
        self.app.show_page("accueil")
