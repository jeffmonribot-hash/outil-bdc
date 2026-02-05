"""
Liste des marchés
Données de référence utilisées dans l'application.
Liste volontairement évolutive (ajout / suppression possible).
"""

MARCHES = [
    {"key": "MARCHE_01", "label": "Marché 01", "actif": True},
    {"key": "MARCHE_02", "label": "Marché 02", "actif": True},
    {"key": "MARCHE_03", "label": "Marché 03", "actif": True},
]


def get_marches_actifs():
    """Retourne la liste des marchés actifs (labels)."""
    return [m["label"] for m in MARCHES if m["actif"]]


def get_marche_par_key(key):
    """Retourne un marché à partir de sa clé interne."""
    for m in MARCHES:
        if m["key"] == key:
            return m
    return None


def ajouter_marche(key, label):
    """Ajoute un nouveau marché."""
    MARCHES.append({
        "key": key,
        "label": label,
        "actif": True
    })


def desactiver_marche(key):
    """Désactive un marché sans le supprimer (sécurité historique)."""
    for m in MARCHES:
        if m["key"] == key:
            m["actif"] = False
            return

