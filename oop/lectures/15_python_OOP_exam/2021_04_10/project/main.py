from project.fish.base_fish import BaseFish
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

import unittest

class TestFish(unittest.TestCase):
    def test_freshwater_fish_eat(self):

        freshwater_fish = FreshwaterFish("Pino", "Goldfish", 10.0)

        self.assertEqual(freshwater_fish.size, 3)

        freshwater_fish.eat()

        self.assertEqual(freshwater_fish.size, 6)

if __name__ == '__main__':
    unittest.main()

