# ******* Class and Static Methods ******* #

# *******  4_hotel_rooms  ******* #

# *******  TASK CONDITION  ******* #
"""
https://judge.softuni.org/Contests/2430/Static-and-Class-Methods-Lab

In a folder called project create two files: hotel.py and room.py

In the room.py file, create a class called Room.
    Upon initialization, it should receive a number (int) and a capacity (int).
        It should also have an attribute called guests (0 by default) and is_taken (False by default).
            The class should have 2 additional methods:

        •	take_room(people)
            - if the room is not taken, and there is enough space, the guests take the room.
                Otherwise, the method should
                    return "Room number {number} cannot be taken"

        •	free_room()
            - if the room is taken, free it.
                Otherwise,
                    return "Room number {number} is not taken"

In the hotel.py file, create a class called Hotel. Upon initialization, it should receive a name (str).
    It should also have 2 more attributes: rooms (empty list of rooms) and guests (0 by default).

    The class should have 5 more methods:
    •	from_stars(stars_count: int)
        - creates a new instance with name "{stars_count} stars Hotel"
    •	add_room(room: Room)
        - adds the room to the list of rooms
    •	take_room(room_number, people)
        - finds the room with that number and tries to accommodate the guests in the room
    •	free_room(room_number)
        - finds the room with that number and tries to free it
    •	status()
        - returns information about the hotel in the following format:

"Hotel {name} has {guests} total guests
Free rooms: {numbers of all free rooms separated by comma and space}
Taken rooms: {numbers of all taken rooms separated by comma and space}"

"""

##########: SOLUTION :##########


##########: TEST CODE :##########
from project.hotel import Hotel
from project.room import Room

hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

print(hotel.status())

"""
Output:
Hotel 5 stars Hotel has 3 total guests
Free rooms: 2
Taken rooms: 1, 3

 """
##########: UNITTEST :##########

from project.hotel import Hotel
from project.room import Room
import unittest


class Tests(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, 3)
        self.hotel = Hotel("Some Hotel")

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.room.number, 1)
        self.assertEqual(self.room.capacity, 3)
        self.assertEqual(self.room.guests, 0)
        self.assertEqual(self.room.is_taken, False)

    def test_take_room_success(self):
        self.room.take_room(2)
        self.assertEqual(self.room.is_taken, True)
        self.assertEqual(self.room.guests, 2)

    def test_take_room_not_enough_capacity(self):
        result = self.room.take_room(4)
        self.assertEqual(self.room.is_taken, False)
        self.assertEqual(self.room.guests, 0)
        self.assertEqual(result, "Room number 1 cannot be taken")

    def test_take_room_not_free(self):
        self.room.take_room(1)
        result = self.room.take_room(1)
        self.assertEqual(self.room.is_taken, True)
        self.assertEqual(self.room.guests, 1)
        self.assertEqual(result, "Room number 1 cannot be taken")

    def test_free_room_success(self):
        self.room.take_room(1)
        self.room.free_room()
        self.assertEqual(self.room.is_taken, False)
        self.assertEqual(self.room.guests, 0)

    def test_free_room_not_taken(self):
        result = self.room.free_room()
        self.assertEqual(self.room.is_taken, False)
        self.assertEqual(self.room.guests, 0)
        self.assertEqual(result, "Room number 1 is not taken")

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.hotel.name, "Some Hotel")
        self.assertEqual(self.hotel.rooms, [])
        self.assertEqual(self.hotel.guests, 0)

    def test_class_methods_creates_a_hotel(self):
        hotel = Hotel.from_stars(3)
        self.assertEqual(hotel.name, "3 stars Hotel")
        self.assertEqual(self.hotel.rooms, [])
        self.assertEqual(self.hotel.guests, 0)

    def test_add_room(self):
        room = Room(1, 3)
        self.hotel.add_room(room)
        self.assertEqual(self.hotel.rooms, [room])

    def test_take_room(self):
        room = Room(1, 3)
        self.hotel.add_room(room)
        self.hotel.take_room(1, 3)
        self.assertEqual(self.hotel.rooms[0].is_taken, True)

    def test_free_room(self):
        room = Room(1, 3)
        self.hotel.add_room(room)
        self.hotel.take_room(1, 3)
        self.hotel.free_room(1)
        self.assertEqual(self.hotel.guests, 0)
        self.assertEqual(self.hotel.rooms[0].is_taken, False)
        self.assertEqual(self.hotel.rooms[0].guests, 0)

    def test_print_status(self):
        room = Room(1, 3)
        self.hotel.add_room(room)
        self.hotel.take_room(1, 3)
        res = self.hotel.status().strip()
        actual = 'Hotel Some Hotel has 3 total guests\nFree rooms: \nTaken rooms: 1'
        self.assertEqual(res, actual)


if __name__ == "__main__":
    unittest.main()