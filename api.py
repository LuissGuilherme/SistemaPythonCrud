from flask import Flask, jsonify, request
from db import Database

app = Flask(__name__)
db = Database()

@app.route('/api/artists', methods=['GET'])
def get_artists():
    artists = db.get_artists()
    result = [{"id": a[0], "name": a[1], "genre": a[2]} for a in artists]
    return jsonify(result)

@app.route('/api/artists', methods=['POST'])
def add_artist():
    data = request.json
    db.add_artist(data['name'], data['genre'])
    return jsonify({"message": "Artista adicionado com sucesso!"}), 201

@app.route('/api/songs', methods=['GET'])
def get_songs():
    songs = db.get_songs()
    result = [
        {"id": s[0], "title": s[1], "duration": s[2], "plays": s[3], "artist": s[4]} 
        for s in songs
    ]
    return jsonify(result)

def run_api():
    app.run(port=5000, debug=False, use_reloader=False)