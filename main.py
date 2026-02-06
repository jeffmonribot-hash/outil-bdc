import tkinter as tk
from pages.accueil import PageAccueil

if __name__ == "__main__":
    app = tk.Tk()
    app.title("Outil BDC – CAPB")
    app.geometry("900x600")

    # ===== CONTEXTE GLOBAL =====
    contexte = {
        "utilisateur": "Jeff Monribot",
        "secteur": "DPBMG – Labourd Sud",
        "annee": "2026",
        "annees": ["2024", "2025", "2026"]
    }

    PageAccueil(app, contexte)

    app.mainloop()
