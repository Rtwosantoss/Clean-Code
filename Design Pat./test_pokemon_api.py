import unittest
from unittest.mock import patch, MagicMock
from pokemon_api import PokemonAPI

class TestPokemonAPI(unittest.TestCase):

    def test_get_pokemon_success(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "name": "pikachu",
            "height": 4,
            "weight": 60
        }
        mock_response.raise_for_status.return_value = None

        with patch("requests.get", return_value=mock_response):
            api = PokemonAPI()
            result = api.get_pokemon("pikachu")

            self.assertEqual(result["name"], "pikachu")
            self.assertEqual(result["height"], 4)
            self.assertEqual(result["weight"], 60)
            mock_response.raise_for_status.assert_called_once()

    def test_get_pokemon_raises_error(self):
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = Exception("Erro 404")

        with patch("requests.get", return_value=mock_response):
            api = PokemonAPI()
            with self.assertRaises(Exception):
                api.get_pokemon("pokemon-invalido")

if __name__ == "__main__":
    unittest.main()
