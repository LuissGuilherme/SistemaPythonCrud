import threading
import tkinter as tk
from gui import MusicApp
from api import run_api

def start_gui():
    root = tk.Tk()
    app = MusicApp(root)
    root.mainloop()

if __name__ == "__main__":
    api_thread = threading.Thread(target=run_api, daemon=True)
    api_thread.start()
    print("--- SISTEMA INICIADO ---")
    print("API rodando em: http://127.0.0.1:5000/api/artists")
    print("Interface Gráfica iniciando...")
    

    start_gui()