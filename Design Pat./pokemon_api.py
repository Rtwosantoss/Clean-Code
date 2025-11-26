import requests

class PokemonAPI:
    BASE_URL = "https://pokeapi.co/api/v2/pokemon"

    def get_pokemon(self, name: str) -> dict:

        url = f"{self.BASE_URL}/{name.lower()}"
        response = requests.get(url)
        response.raise_for_status()

        return response.json()

def main():
    api = PokemonAPI()

    pokemon_name = "pikachu"
    pokemon_data = api.get_pokemon(pokemon_name)

    print(f"Nome: {pokemon_data['name']}")
    print(f"Altura: {pokemon_data['height']}")
    print(f"Peso: {pokemon_data['weight']}")

if __name__ == "__main__":
    main()
