from project.pet_shop import PetShop

import unittest

class TestPetShop(unittest.TestCase):
    def setUp(self):
        self.shop = PetShop("TestShop")

    def test_add_food_success(self):
        result = self.shop.add_food("DogFood", 500)
        self.assertEqual(result, "Successfully added 500.00 grams of DogFood.")
        self.assertEqual(self.shop.food["DogFood"], 500)

    def test_add_food_zero_or_negative_quantity(self):
        with self.assertRaises(ValueError):
            self.shop.add_food("CatFood", 0)
        with self.assertRaises(ValueError):
            self.shop.add_food("CatFood", -50)

    def test_add_food_empty_name(self):
        with self.assertRaises(ValueError):
            self.shop.add_food("", 100)

    def test_add_pet_success(self):
        result = self.shop.add_pet("Buddy")
        self.assertEqual(result, "Successfully added Buddy.")
        self.assertIn("Buddy", self.shop.pets)

    def test_add_pet_with_existing_name(self):
        self.shop.add_pet("Buddy")
        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("Buddy")
        self.assertEqual(str(ex.exception), "Cannot add a pet with the same name")

    def test_add_pet_empty_name(self):
        with self.assertRaises(ValueError):
            self.shop.add_pet("")

    def test_feed_pet_success(self):
        self.shop.add_pet("Buddy")
        self.shop.add_food("DogFood", 200)
        result = self.shop.feed_pet("DogFood", "Buddy")
        self.assertEqual(result, "Buddy was successfully fed")
        self.assertEqual(self.shop.food["DogFood"], 100)

    def test_feed_pet_with_insufficient_food(self):
        self.shop.add_pet("Buddy")
        self.shop.add_food("DogFood", 50)
        result = self.shop.feed_pet("DogFood", "Buddy")
        self.assertEqual(result, "Adding food...")
        self.assertEqual(self.shop.food["DogFood"], 1050)

    def test_feed_pet_with_no_food(self):
        self.shop.add_pet("Buddy")
        result = self.shop.feed_pet("DogFood", "Buddy")
        self.assertEqual(result, "You do not have DogFood")

    def test_feed_pet_with_invalid_pet_name(self):
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet("DogFood", "UnknownPet")
        self.assertEqual(str(ex.exception), "Please insert a valid pet name")

    def test_repr(self):
        self.shop.add_pet("Buddy")
        self.shop.add_pet("Max")
        result = repr(self.shop)
        self.assertEqual(result, "Shop TestShop:\nPets: Buddy, Max")

if __name__ == '__main__':
    unittest.main()

