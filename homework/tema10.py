# Exercitiul 1
# https://api.coingecko.com/api/v3/exchange_rates
# compute the exchange rate of bitcoin in eur and usd
# write tests for the compute function mocking the API

import requests
def main():
  #call coingecko for exchange rates
  response = requests.get("https://api.coingecko.com/api/v3/exchange_rates", )
  #print the object, see the response code
  print(response)
  #print the content of the object
  values = (response.json())
  #print the BTC info
  btc = values["rates"]["btc"]
  #print the EUR info
  eur = values["rates"]["eur"]
  #print the USD info
  usd = values["rates"]["usd"]
  #compute EUR in BTC and USD in BTC
  print("1BTC is "+ str(eur["value"]) + eur["unit"])
  print("1BTC is "+ str(usd["value"]) + usd["unit"])
def get_value_in_euro():
  response = requests.get("https://api.coingecko.com/api/v3/exchange_rates", )
  values = (response.json())
  eur = values["rates"]["eur"]
  return eur["value"]
main()

# Exercitiul 2
# url: https://api.nasa.gov/planetary/apod
# call NASA with params api_key=DEMO_KEY, date of format YYYY-MM-DD (2019-03-20)
# Make a class with a method which makes the call and returns the tile and the explanation
# Write 3 tests for it which call the real API on different dates, can check only the title
# Write 3 tests which mock the API returning different titles and explanations
import requests
def get_today():
  response = requests.get("https://api.nasa.gov/planetary/apod",
                          params={"api_key": "DEMO_KEY", "date": "2020-11-18"})
  print(response)
  #get the content/data
  content = response.json()
  #get the title of the day
  title = content["title"]
  print(title)
get_today()
def get_month():
  i = 1
  while i < 30:
    date = "2020-10-" + str(i)
    response = requests.get("https://api.nasa.gov/planetary/apod",
                            params={"api_key": "DEMO_KEY", "date": date})
    print(response.json()["title"])
    i += 1
get_month()
# nu ne mai lasa dupa cateva incercari sa rulam codul deoarece e demo mode

# Exercitiul 3
# url: https://pokeapi.co/api/v2/pokemon/<pokemon_number>
# pokemon_number=1 will show results for bulbasaur
# url: https://pokeapi.co/api/v2/pokemon/<pokemon_name>
# make a class with 2 methods for each api calls
# write 3 tests which call the real API and 3 tests which mock the API
import requests
class Pokemon:
  def get_by_number(self, number):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(number))
    content = response.json()
    return content["species"]["name"]
pokemon = Pokemon()
content = pokemon.get_by_number(25)
print(content)

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

# Exercitiul 4
# http://www.7timer.info/bin/astro.php
# parameter example: lon=113.2, lat=23.1, ac=0, unit=metric, output=json, tzshift=0
# Make a class with methods to find the weather in Timisoara, Bucharest, Oradea, Suceava
# Make 1 test for each method mocking the API