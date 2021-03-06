import unittest
from tema9 import Client, GameCollection

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