import requests
class Pokemon:
  def get_by_number(self, number):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(number))
    content = response.json()
    return content["species"]["name"]
pokemon = Pokemon()
content = pokemon.get_by_number(25)
print(content)