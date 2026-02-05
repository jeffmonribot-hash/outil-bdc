import tkinter as tk
from app import Application

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Outil de gestion des BDC – CAPB")
    root.geometry("900x600")
    root.minsize(800, 500)

    app = Application(root)
    app.pack(fill="both", expand=True)

    root.mainloop()
