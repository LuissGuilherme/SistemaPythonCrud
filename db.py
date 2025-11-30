import sqlite3

class Database:
    def __init__(self, db_name="sistema_musica.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        
        self.cursor.execute("PRAGMA foreign_keys = ON")
        
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS artists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                genre TEXT
            )
        """)
        
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                duration TEXT,
                plays INTEGER,
                artist_id INTEGER,
                FOREIGN KEY (artist_id) REFERENCES artists (id) ON DELETE CASCADE
            )
        """)
        self.conn.commit()

    # CRUD
    def add_artist(self, name, genre):
        self.cursor.execute("INSERT INTO artists (name, genre) VALUES (?, ?)", (name, genre))
        self.conn.commit()

    def get_artists(self):
        self.cursor.execute("SELECT * FROM artists")
        return self.cursor.fetchall()

    def delete_artist(self, artist_id):
        self.cursor.execute("DELETE FROM artists WHERE id = ?", (artist_id,))
        self.conn.commit()

    
    def add_song(self, title, duration, plays, artist_id):
        self.cursor.execute("""
            INSERT INTO songs (title, duration, plays, artist_id) 
            VALUES (?, ?, ?, ?)
        """, (title, duration, plays, artist_id))
        self.conn.commit()

    def get_songs(self):
    
        query = """
            SELECT songs.id, songs.title, songs.duration, songs.plays, artists.name 
            FROM songs 
            JOIN artists ON songs.artist_id = artists.id
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def delete_song(self, song_id):
        self.cursor.execute("DELETE FROM songs WHERE id = ?", (song_id,))
        self.conn.commit()

    def update_artist(self, artist_id, name, genre):
        self.cursor.execute("UPDATE artists SET name = ?, genre = ? WHERE id = ?", (name, genre, artist_id))
        self.conn.commit()

    def update_song(self, song_id, title, duration, plays, artist_id):
        self.cursor.execute("""
            UPDATE songs 
            SET title = ?, duration = ?, plays = ?, artist_id = ? 
            WHERE id = ?
        """, (title, duration, plays, artist_id, song_id))
        self.conn.commit() 
        
    def close(self):
        self.conn.close()