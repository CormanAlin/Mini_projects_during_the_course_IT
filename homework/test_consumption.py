import unittest
from consumption import ConsumptionBelow100, ConsumptionAbove300

class TestConsumption(unittest.TestCase):
  def test_below_100(self):
    # set up
    consumption = ConsumptionBelow100(50, "name")
    # execution
    actual_price = consumption.get_price()
    # assertion
    self.assertEqual(3, actual_price)

  def test_below_300(self):
    #set up
    consumption = ConsumptionAbove300(310, "name")
    # execution
    actual_price = consumption.get_price()
    # assertion
    self.assertEqual(24, actual_price)
