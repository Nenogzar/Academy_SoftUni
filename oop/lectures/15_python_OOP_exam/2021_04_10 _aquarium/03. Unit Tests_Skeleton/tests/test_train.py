from unittest import TestCase, main
from project.train.train import Train

import unittest

class TestTrain(unittest.TestCase):

    def setUp(self):
        self.train = Train(name="Express", capacity=2)

    def test_init(self):
        train = Train(name="Express", capacity=2)
        self.assertEqual(train.name, "Express")
        self.assertEqual(train.capacity, 2)
        self.assertEqual(train.passengers, [])

    def test_add_passenger_success(self):
        result = self.train.add("John")
        self.assertEqual(result, "Added passenger John")
        self.assertIn("John", self.train.passengers)

    def test_add_passenger_full(self):
        self.train.add("John")
        self.train.add("Doe")
        with self.assertRaises(ValueError) as ex:
            self.train.add("Jane")
        self.assertEqual(str(ex.exception), Train.TRAIN_FULL)

    def test_add_passenger_exists(self):
        self.train.add("John")
        with self.assertRaises(ValueError) as ex:
            self.train.add("John")
        self.assertEqual(str(ex.exception), Train.PASSENGER_EXISTS.format("John"))

    def test_remove_passenger_success(self):
        self.train.add("John")
        result = self.train.remove("John")
        self.assertEqual(result, "Removed John")
        self.assertNotIn("John", self.train.passengers)

    def test_remove_passenger_not_found(self):
        with self.assertRaises(ValueError) as ex:
            self.train.remove("John")
        self.assertEqual(str(ex.exception), Train.PASSENGER_NOT_FOUND)

    def test_add_empty_passenger_name(self):
        with self.assertRaises(ValueError) as ex:
            self.train.add("")
        self.assertEqual(str(ex.exception), Train.PASSENGER_EXISTS.format(""))

    def test_remove_empty_passenger_name(self):
        with self.assertRaises(ValueError) as ex:
            self.train.remove("")
        self.assertEqual(str(ex.exception), Train.PASSENGER_NOT_FOUND)

    def test_add_passenger_with_whitespace(self):
        result = self.train.add("   ")
        self.assertEqual(result, "Added passenger    ")
        self.assertIn("   ", self.train.passengers)

    def test_remove_passenger_with_whitespace(self):
        self.train.add("   ")
        result = self.train.remove("   ")
        self.assertEqual(result, "Removed    ")
        self.assertNotIn("   ", self.train.passengers)

if __name__ == '__main__':
    unittest.main()
