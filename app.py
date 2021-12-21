from flask import Flask, json, Response, request

from database.db import initialize_db

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://adminPGabriel:adminPGabriel@cluster0.pgpdg.mongodb.net/taskListIonic?retryWrites=true&w=majority"'
}

initialize_db(app)


@app.route('/movies', methods=["POST"])
def add_movie():
    movie = request.get_json()
    movies.append(movie)
    return {'id': len(movies)}, 200


@app.route('/movies/<int:index>', methods=["PUT"])
def update_movie(index):
    movie = request.get_json()
    movies[index] = movie
    return jsonify(movies[index]), 200


@app.route('/movies/<int:index>', methods=["DELETE"])
def delete_movie(index):
    movies.pop(index)
    return 'None', 200


app.run()
