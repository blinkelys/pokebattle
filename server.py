from flask import Flask
from flask_cors import CORS

from Pokemon import pokemons

app = Flask(__name__)
CORS(app)


@app.route("/api/all-pokemons")
def get_pokemons():
    return {"pokemons": [pokemon.data for pokemon in pokemons]}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)