from flask import Flask
from flask_cors import CORS
import dotenv
import os
dotenv.load_dotenv()

port = int(os.getenv("SERVER_PORT", 5000))
host = os.getenv("HOST", "0.0.0.0")

from Pokemon import pokemons

app = Flask(__name__)
CORS(app)


@app.route("/api/all-pokemons")
def get_pokemons():
    return {"pokemons": [pokemon.data for pokemon in pokemons]}


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True, host="0.0.0.0", port=5001)
=======
    debug = os.getenv("FLASK_DEBUG", "1").lower() in ("1", "true", "yes")
    app.run(debug=debug, host=host, port=port)
>>>>>>> d668bca (feat: improved prod setup)
