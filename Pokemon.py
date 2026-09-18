import requests

class Pokemon:
    def __init__(self, name):
        self.name = name

        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        self.data = response.json()

    def show_info(self):
        print("Name:", self.data["name"])
        print("ID:", self.data["id"])
        print("Height:", self.data["height"])
        print("Weight:", self.data["weight"])
        print("Stats:", self.data["stats"])
        print("Types:", self.data["types"])
        print("Abilities:", self.data["abilities"])
        print("Moves:", self.data["moves"])
        print("Sprites:", self.data["sprites"])

pokemons = [
    Pokemon("bulbasaur"),
    Pokemon("ivysaur"),
    Pokemon("mew")
]