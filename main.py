import tkinter as tk
from pages.accueil import PageAccueil

if __name__ == "__main__":
    app = tk.Tk()
    app.title("Outil BDC – CAPB")

    # 👉 Plein écran (Windows)
    app.state("zoomed")

    # Contexte global
    contexte = {
        "utilisateur": "Jeff Monribot",
        "secteur": "DPBMG – Labourd Sud",
        "annee": "2026",
        "annees": ["2024", "2025", "2026"]
    }

    # Chargement de la page d’accueil
    PageAccueil(app, contexte)

    # Lancement de l'application
    app.mainloop()
