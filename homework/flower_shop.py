# Create a flower shop application which deals in flower objects
# and use those flower objects in a bouquet object which can then be sold.
# Keep track of the number of objects and when you may need to order more (keep them in a file)
# Allow the user to give commands through the terminal (use sys.argv to read the commands)
# Make unit tests

import abc
import json


class Flower(abc.ABC):
  @abc.abstractmethod
  def __init__(self, colour, smell, petals, type):
    # save the info to the object
    self.colour = colour
    self.smell = smell
    self.petals = petals
    self.type = type


class Rose(Flower):
  def __init__(self, colour, petals):
    super().__init__(colour, "relaxing", petals, "Rose")


class Tulip(Flower):
  def __init__(self, colour, petals):
    super().__init__(colour, "honey", petals, "Tulip")


class Orchid(Flower):
  def __init__(self, colour, petals):
    super().__init__(colour, "cinnamon", petals, "Orchid")


class Bouquet:
  def __init__(self, flowers):
    self.flowers = flowers

  def get_smell(self):
    smells = {}
    for one_flower in self.flowers:
      smells[one_flower.smell] = smells[one_flower.smell] + 1 if one_flower.smell in smells else 1
    return smells


class FlowerShop:
  def place_order(self, flowers):
    bouquet = Bouquet(flowers)
    return bouquet

  def add_to_inventory(self, flowers):
    inventory = self.read_file()

    for one_flower in flowers:
      inventory.append(one_flower.__dict__)
    json_inventory = json.dumps(inventory)
    file = open("inventory.txt", "w")
    file.write(json_inventory)
    file.close()

  def read_file(self):
    # try to open the file for reading, if it exists we read from it
    try:
      file = open("inventory.txt")
      inventory = json.loads(file.read())
    except:
      # if the file if not exist, we create it
      file = open("inventory.txt", 'w')
      file.write(json.dumps([]))
      file.close()
      inventory = []
    return inventory

  def get_inventory(self):
    file_content = self.read_file()
    inventory = []
    for flower in file_content:
      if flower["type"] == "Tulip":
        inventory.append(Tulip(flower["colour"], flower["petals"]))
      if flower["type"] == "Orchid":
        inventory.append(Orchid(flower["colour"], flower["petals"]))
    return inventory


shop = FlowerShop()
print(shop.get_inventory())
#shop.add_to_inventory([Tulip("red", 6), Orchid("white", 3), Orchid("white", 4)])
#order = shop.place_order([Tulip("red", 6), Orchid("white", 3), Orchid("white", 4)])

#print(order.get_smell())