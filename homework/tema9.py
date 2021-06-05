# Exercitiul 1 Bank Account
# Write 2 asserts for withdraw
import unittest
class BankAccount:
  def __init__(self, balance):
    self.balance = balance

  def withdraw(self, amount):
    self.balance -= amount

  def deposit(self, amount):
    self.balance += amount

class TestBankAccount(unittest.TestCase):
  def test_windraw(self):
    account = BankAccount(100)
    account.withdraw(40)
    self.assertEqual(60, account.balance)
    account.withdraw(20)
    self.assertEqual(40 , account.balance)

# Write 2 asserts for deposit
#Aceiasi chestie ca si la prima linie

# Add a 1ron tax for withdraw and update the test
import unittest
class BankAccount:
  def __init__(self, balance):
    self.balance = balance

  def withdraw(self, amount):
    self.balance -= amount +1

  def deposit(self, amount):
    self.balance += amount

class TestBankAccount(unittest.TestCase):
  def test_windraw(self):
    account = BankAccount(100)
    account.withdraw(40)
    self.assertEqual(59, account.balance)
    account.withdraw(20)
    self.assertEqual(38 , account.balance)

# Return False if we try to withdraw more than what we have
import unittest
class BankAccount:
  def __init__(self, balance):
    self.balance = balance

  def withdraw(self, amount):
    if amount > self.balance:
      return False
    self.balance -= amount +1

  def deposit(self, amount):
    self.balance += amount

class TestBankAccount(unittest.TestCase):
  def test_windraw(self):
    account = BankAccount(100)
    account.withdraw(40)
    self.assertEqual(59, account.balance)
    account.withdraw(20)
    self.assertEqual(38 , account.balance)
  def test_winthdraw_more_than_we_have(self):
    account = BankAccount(5000)
    response = account.withdraw(6000)
    self.assertEqual(False, response)
    self.assertEqual(5000, account.balance)

# Write an assert if we try to withdraw more than what we have

# Exercitiul 2 Password
class Password:
  def __init__(self, password):
    self.__password = password

  #create tests for all strength levels
  def strength_level(self):
    length = len(self.__password)
    if length < 10:
      return 0
    elif length < 20:
      return 1
    else:
      return 2

# change strength levels to 4
# 1st level < 8
# 2nd level < 16
# 3rd level < 24
# 4th level > 24
# update tests for this method

# Exercitiul 3 Rectangle
import unittest
class Rectangle:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # implement the method to compute the perimeter, the sum of the vertices
  # write tests for it
  def perimeter(self):
    return 2 * self.x + 2 * self.y

  # implement method to compute the area
  # write tests for it
  def area(self):
    return self.x * self.y

class TestRectangle(unittest.TestCase):
  def test_perimeter(self):
    #setup test
    rectangle1 = Rectangle(3, 5)
    rectangle2 = Rectangle(6, 12)
    #execution
    per1 = rectangle1.perimeter()
    per2 = rectangle2.perimeter()
    #assertion
    self.assertEqual(16, per1)
    self.assertEqual(36, per2)


# Create a subclass of Rectangle, square
class Square(Rectangle):
  def __init__(self, x):
    self.x = x
    self.y = x
class TestSquare(unittest.TestCase):
  def test_area(self):
    #setup
    square = Square(10)
    #execution
    area = square.area()
    #assertion
    self.assertEqual(100, area)
# write tests for perimeter & area

# Exercitiul 4 Steam
class GameCollection:
  @staticmethod
  def get():
    return [
      {'name': 'Cyberpunk', 'price': 60, 'voucher': 'ADA'},
      {'name': 'Minecraft', 'price': 30, 'voucher': ''},
      {'name': 'Yaga', 'price': 15, 'voucher': 'Romania'},
      {'name': 'Fifa 21', 'price': 70, 'voucher': 'ADA'},
      {'name': 'Kingdom Come Deliverance', 'price': 40, 'voucher': ''},
      {'name': 'Spiderman', 'price': 70, 'voucher': ''},
      {'name': 'Fortnite', 'price': 0, 'voucher': ''},
      {'name': 'Sims', 'price': 10, 'voucher': 'DAD'},
      {'name': 'Cities Skyline', 'price': 26, 'voucher': 'DAD'},
      {'name': 'Witcher', 'price': 20, 'voucher': ''},
      {'name': 'Prince of Persia', 'price': 10, 'voucher': ''},
    ]
  @staticmethod
  def get_price(game_name, voucher=""):
    for game in GameCollection.get():
      if game_name == game["name"]:
        if game["voucher"] != "" and game["voucher"] == voucher:
          return 90 / 100 * game["price"]
        return game["price"]

class Client:
  def __init__(self, username):
    self.username = username
    self.money = 0

  # make tests for it, return False if he tries to add more than 500
  def add_money(self, ammount):
    if ammount > 500:
      return False
    self.money += ammount

  # give a list of games, if the user has enough money buy them (substract money)
  # if the voucher code applies to a game, reduce the price by 10%
  # write at least 6 tests
  def buy_games(self, list_of_games, voucher=''):
    for game in list_of_games:
      self.money -= GameCollection.get_price(game, voucher)

class TestClient(unittest.TestCase):
  def test_add_money(self):
    #setup
    client = Client("user1")
    #execution
    client.add_money(100)
    #assertion
    self.assertEqual(100, client.money)
  def test_return_false_if_too_much_money_was_added(self):
    #setup
    client = Client("user1")
    #execution
    response = client.add_money(700)
    #assertion
    self.assertEqual(False, response)
    self.assertEqual(0, client.money)
  def test_buy_games(self):
    #setup
    client = Client("user1")
    client.add_money(300)
    list = ["Cyberpunk", "Minecraft", "Sims"]
    #execution
    client.buy_games(list, "ADA")
    #assertion
    self.assertEqual(206, client.money)


# write a subclass of Client, PremiumClient
# every game is 20% cheaper
# vouchers do not work
# every ammount of money added is taxed with 10%
# write the same test cases as for Client

# Exercitiul 5 Warehouse
import json
import os


class Warehouse:
  @staticmethod
  def add(product):
    # remove try/except and use os.path.exists
    # tests should still pass
    try:
      # read from the file if it exists
      f = open('warehouse', 'r')
      items = f.read()
      decoded_items = json.loads(items)
      f.close()
    except:
      # if no file, the structure is empty
      decoded_items = {}

    decoded_items[product.name] = product.__dict__

    # write the new item structure to the file
    encoded_items = json.dumps(decoded_items)

    # open the file for writing
    f = open('warehouse', 'w')
    f.write(encoded_items)
    f.close()

  @staticmethod
  def show():
    if os.path.exists('warehouse'):  # we check the file exists
      f = open('warehouse')  # open the file for read
      encoded_items = f.read()  # we read the JSON
      items = json.loads(encoded_items)  # we decode the JSON
      f.close()
      return items
    return {}

  # implement method to remove a product
  # make tests for it
  #   test nr 1, if we do not have a file
  #   test nr 2, if we have a file but no products in it
  #   test nr 3, if we have a file but not the specified product
  #   test nr 4, if we have only the specified product and it succesfully removes it
  #   test nr 5, we have 2 products and the specified one
  @staticmethod
  def remove(product):
    pass


class Product:
  def __init__(self, name, price, number):
    self.name = name
    self.price = price
    self.number = number