"""
Utilisateurs et mails de référence
Utilisés pour les envois, copies et retours BDC.
"""

UTILISATEURS = [
    {
        "key": "SAF",
        "label": "SAF",
        "email": "saf.dpbmg@communaute-paysbasque.fr",
        "actif": True
    },
    {
        "key": "RETOUR_BDC_01",
        "label": "Retour BDC 01",
        "email": "j.monribot@communaute-paysbasque.fr",
        "actif": True
    },
    {
        "key": "RETOUR_BDC_02",
        "label": "Retour BDC 02",
        "email": "m.etchegaray@communaute-paysbasque.fr",
        "actif": True
    },
    {
        "key": "UTILISATEUR_01",
        "label": "Utilisateur 01",
        "email": "j.monribot@communaute-paysbasque.fr",
        "actif": True
    },
    {
        "key": "UTILISATEUR_02",
        "label": "Utilisateur 02",
        "email": "f.camou@communaute-paysbasque.fr",
        "actif": True
    },
]


def get_utilisateurs_actifs():
    """Retourne les utilisateurs actifs."""
    return [u for u in UTILISATEURS if u["actif"]]


def get_emails_actifs():
    """Retourne uniquement les emails actifs."""
    return [u["email"] for u in UTILISATEURS if u["actif"]]


def get_utilisateur_par_key(key):
    """Retourne un utilisateur par clé."""
    for u in UTILISATEURS:
        if u["key"] == key:
            return u
    return None


def desactiver_utilisateur(key):
    """Désactive un utilisateur sans supprimer l'historique."""
    for u in UTILISATEURS:
        if u["key"] == key:
            u["actif"] = False
            return
