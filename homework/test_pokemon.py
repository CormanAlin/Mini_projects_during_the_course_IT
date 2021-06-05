import unittest
from pokemon import Pokemon
import requests
from unittest.mock import patch
#crate a subclass of API response
class OurResponse(requests.Response):
  def json(self):
    return {"species": {"name": "pikachu"}}


class TestPokemon(unittest.TestCase):
  @patch("requests.get", return_value=OurResponse())
  def test_pikachu(self, get):
    #setup
    pokemon = Pokemon()
    #execution
    value = pokemon.get_by_number(25)
    #assertion

    self.assertEqual("pikachu", value)


