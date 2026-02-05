"""
Chemins dossiers – version fondation
On conserve toutes les catégories (BDC à créer, à intégrer, etc.)
mais pour l’instant elles pointent toutes vers le CHEMIN_REFERENCE.

Plus tard : Paramètres permettra de définir les vrais sous-chemins.
"""

CHEMIN_REFERENCE = r"M:\01-BATIMENTS"

CHEMINS = [
    {
        "key": "BDC_A_CREER",
        "label": "BDC à créer",
        "description": "Dossier cible pour stocker les devis (phase fondation : chemin de référence)",
        "chemin": CHEMIN_REFERENCE,
        "actif": True
    },
    {
        "key": "BDC_A_INTEGRER",
        "label": "BDC à intégrer",
        "description": "Dossier cible pour stocker les BDC (phase fondation : chemin de référence)",
        "chemin": CHEMIN_REFERENCE,
        "actif": True
    },
    {
        "key": "FICHE_TRAVAUX",
        "label": "Fiche travaux",
        "description": "Dossier cible des fiches travaux (phase fondation : chemin de référence)",
        "chemin": CHEMIN_REFERENCE,
        "actif": True
    },
    {
        "key": "EXPORT_PDF",
        "label": "Export PDF",
        "description": "Dossier cible des exports PDF (phase fondation : chemin de référence)",
        "chemin": CHEMIN_REFERENCE,
        "actif": True
    },
    {
        "key": "SIGNATURE",
        "label": "Signature",
        "description": "Dossier / ressource de signature (phase fondation : chemin de référence)",
        "chemin": CHEMIN_REFERENCE,
        "actif": True
    },
    {
        "key": "RAPPORT",
        "label": "Rapport",
        "description": "Dossier cible des rapports (phase fondation : chemin de référence)",
        "chemin": CHEMIN_REFERENCE,
        "actif": True
    },
]


def get_chemin_par_key(key: str) -> str | None:
    """Retourne le chemin actif associé à une clé."""
    for c in CHEMINS:
        if c["key"] == key and c["actif"]:
            return c["chemin"]
    return None


def get_chemins_actifs():
    """Retourne les chemins actifs (objets complets)."""
    return [c for c in CHEMINS if c["actif"]]
