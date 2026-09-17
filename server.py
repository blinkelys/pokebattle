from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

pokemons = [
    {"id": 1, "name": "Bulbasaur"},
    {"id": 2, "name": "Ivysaur"},
    {"id": 3, "name": "Venusaur"},
]

@app.route("/api/all-pokemons")
def get_pokemons():
    return {"pokemons": pokemons}

if __name__ == "__main__":
    app.run(debug=True)