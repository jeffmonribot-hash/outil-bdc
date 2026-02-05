"""
Statuts des Bons de Commande (BDC)
Source de vérité des statuts utilisés dans l'application.
Ne pas coder en dur ailleurs.
"""

STATUTS_BDC = [
    # Création
    {"key": "A_VALIDER", "label": "À valider", "ordre": 1, "auto": True},

    # Cycle SAF / BDC
    {"key": "A_ENVOYER_SAF", "label": "À envoyer au SAF", "ordre": 2, "auto": False},
    {"key": "ENVOYE_SAF", "label": "Envoyé au SAF", "ordre": 3, "auto": True},
    {"key": "BDC_ETABLI", "label": "BDC établi", "ordre": 4, "auto": False},
    {"key": "BDC_ENVOYE_ENTREPRISE", "label": "BDC envoyé à l’entreprise", "ordre": 5, "auto": False},

    # Exécution
    {"key": "TRAVAUX_EN_COURS", "label": "Travaux en cours", "ordre": 6, "auto": False},

    # Facturation
    {"key": "FACTURE_NON_SOLDEE", "label": "Facture non soldée", "ordre": 7, "auto": False},
    {"key": "FACTURE_PARTIE", "label": "Facture en partie", "ordre": 8, "auto": False},

    # Clôture
    {"key": "CLOTURE", "label": "Clôturé", "ordre": 9, "auto": False},
    {"key": "BDC_DEGAGE", "label": "BDC dégagé", "ordre": 10, "auto": False},
    {"key": "ANNULE", "label": "Annulé", "ordre": 11, "auto": False},
]


def get_statuts_labels():
    """Retourne la liste des libellés, triés par ordre."""
    return [s["label"] for s in sorted(STATUTS_BDC, key=lambda x: x["ordre"])]


def get_statut_par_key(key):
    """Retourne un statut à partir de sa clé interne."""
    for s in STATUTS_BDC:
        if s["key"] == key:
            return s
    return None


def get_statut_par_defaut():
    """Statut par défaut à la création d'un BDC."""
    return next(s for s in STATUTS_BDC if s["auto"] and s["ordre"] == 1)

