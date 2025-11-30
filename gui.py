import tkinter as tk
from tkinter import ttk, messagebox
from db import Database

class MusicApp:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.root.title("Sistema de Gestão Musical")
        self.root.geometry("600x450")

        
        self.tabs = ttk.Notebook(root)
        self.tab_artists = ttk.Frame(self.tabs)
        self.tab_songs = ttk.Frame(self.tabs)
        
        self.tabs.add(self.tab_artists, text="Gerenciar Artistas")
        self.tabs.add(self.tab_songs, text="Gerenciar Músicas")
        self.tabs.pack(expand=1, fill="both")

        self.setup_artist_tab()
        self.setup_song_tab()

    # Artistas
    def setup_artist_tab(self):
        frame_form = tk.Frame(self.tab_artists)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Nome:").grid(row=0, column=0)
        self.entry_name = tk.Entry(frame_form)
        self.entry_name.grid(row=0, column=1)

        tk.Label(frame_form, text="Gênero:").grid(row=1, column=0)
        self.entry_genre = tk.Entry(frame_form)
        self.entry_genre.grid(row=1, column=1)

        btn_add = tk.Button(frame_form, text="Adicionar", command=self.add_artist)
        btn_add.grid(row=2, columnspan=2, pady=5)

        # Lista (Treeview)
        cols = ("ID", "Nome", "Gênero")
        self.tree_artists = ttk.Treeview(self.tab_artists, columns=cols, show="headings")
        for col in cols:
            self.tree_artists.heading(col, text=col)
        self.tree_artists.pack(fill="both", expand=True, padx=10)

        btn_del = tk.Button(self.tab_artists, text="Excluir Selecionado", command=self.del_artist)
        btn_del.pack(pady=5)
        
        self.refresh_artists()

    # Músicas
    def setup_song_tab(self):
        frame_form = tk.Frame(self.tab_songs)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Título:").grid(row=0, column=0)
        self.entry_title = tk.Entry(frame_form)
        self.entry_title.grid(row=0, column=1)

        tk.Label(frame_form, text="Duração (min):").grid(row=1, column=0)
        self.entry_dur = tk.Entry(frame_form)
        self.entry_dur.grid(row=1, column=1)

        tk.Label(frame_form, text="Reproduções:").grid(row=2, column=0)
        self.entry_plays = tk.Entry(frame_form)
        self.entry_plays.grid(row=2, column=1)

        tk.Label(frame_form, text="ID Artista:").grid(row=3, column=0)
        # Idealmente seria um Combobox, mas simplificamos com ID manual para brevidade
        self.entry_art_id = tk.Entry(frame_form)
        self.entry_art_id.grid(row=3, column=1)

        btn_add = tk.Button(frame_form, text="Adicionar Música", command=self.add_song)
        btn_add.grid(row=4, columnspan=2, pady=5)

        cols = ("ID", "Título", "Duração", "Plays", "Artista")
        self.tree_songs = ttk.Treeview(self.tab_songs, columns=cols, show="headings")
        for col in cols:
            self.tree_songs.heading(col, text=col)
        self.tree_songs.pack(fill="both", expand=True, padx=10)

        btn_del = tk.Button(self.tab_songs, text="Excluir Música", command=self.del_song)
        btn_del.pack(pady=5)

        self.refresh_songs()

    # GUI
    def add_artist(self):
        name = self.entry_name.get()
        genre = self.entry_genre.get()
        if name and genre:
            self.db.add_artist(name, genre)
            self.refresh_artists()
            messagebox.showinfo("Sucesso", "Artista adicionado!")
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos")

    def add_song(self):
        try:
            title = self.entry_title.get()
            dur = self.entry_dur.get()
            plays = int(self.entry_plays.get())
            art_id = int(self.entry_art_id.get())
            
            self.db.add_song(title, dur, plays, art_id)
            self.refresh_songs()
            messagebox.showinfo("Sucesso", "Música adicionada!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao inserir (Verifique o ID do artista): {e}")

    def refresh_artists(self):
        for row in self.tree_artists.get_children():
            self.tree_artists.delete(row)
        for row in self.db.get_artists():
            self.tree_artists.insert("", "end", values=row)

    def refresh_songs(self):
        for row in self.tree_songs.get_children():
            self.tree_songs.delete(row)
        for row in self.db.get_songs():
            self.tree_songs.insert("", "end", values=row)

    def del_artist(self):
        sel = self.tree_artists.selection()
        if sel:
            item = self.tree_artists.item(sel[0])
            id_val = item['values'][0]
            self.db.delete_artist(id_val)
            self.refresh_artists()
            self.refresh_songs() 

    def del_song(self):
        sel = self.tree_songs.selection()
        if sel:
            item = self.tree_songs.item(sel[0])
            id_val = item['values'][0]
            self.db.delete_song(id_val)
            self.refresh_songs()