# ******* Exercise: Class and Static Methods ******* #

# *******  01_photo_album  ******* #

# *******  TASK CONDITION  ******* #
"""
https://judge.softuni.org/Contests/2431/Static-and-Class-Methods-Exercise

Create a class called PhotoAlbum.
    Upon initialization, it should receive pages (int).
    It should also have one more attribute:
        photos (empty matrix) representing the album with its pages where you should put the photos.
            Each page can contain only 4 photos.

    The class should also have 3 more methods:
•	from_photos_count(photos_count: int)
    - creates a new instance of PhotoAlbum.
        Note: Each page can contain 4 photos.

•	add_photo(label: str)
    - adds the photo in the first possible page and slot and
            return "{label} photo added successfully on page {page_number(starting from 1)} slot {slot_number(starting from 1)}".
        If there are no free slots left,
            return "No more free slots"

•	display() -
            returns a string representation of each page and the photos in it.

Each photo is marked with "[]", and the page separation is made using 11 dashes (-).
    For example, if we have 1 page and 2 photos:

-----------
[] []
-----------
and if we have 2 empty pages:
-----------

-----------

-----------

"""

##########: SOLUTION :##########

from math import ceil


class PhotoAlbum:
    photos_per_page = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> "PhotoAlbum":
        return cls(ceil(photos_count / PhotoAlbum.photos_per_page))

    def add_photo(self, label: str) -> str:
        for i, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.photos_per_page:
                page.append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        separator = "-" * 11 + "\n"
        result = separator
        for page in self.photos:
            result += " ".join("[]" for _ in page) + "\n"
            result += separator
        return result.strip()


##########: TEST CODE :##########
album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

"""
Output:
baby photo added successfully on page 1 slot 1
first grade photo added successfully on page 1 slot 2
eight grade photo added successfully on page 1 slot 3
party with friends photo added successfully on page 1 slot 4
[['baby', 'first grade', 'eight grade', 'party with friends'], []]
prom photo added successfully on page 2 slot 1
wedding photo added successfully on page 2 slot 2
-----------
[] [] [] []
-----------
[] []
-----------

 """
##########: UNITTEST :##########

import unittest


class TestsPhotoAlbum(unittest.TestCase):
    def test_init_creates_all_attributes(self):
        album = PhotoAlbum(2)
        self.assertEqual(album.pages, 2)
        self.assertEqual(album.photos, [[], []])

    def test_from_photos_should_create_instace(self):
        album = PhotoAlbum.from_photos_count(12)
        self.assertEqual(album.pages, 3)
        self.assertEqual(album.photos, [[], [], []])

    def test_add_photo_with_no_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.add_photo("prom")
        self.assertEqual(result, "No more free slots")

    def test_add_photo_with_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])

    def test_display_with_one_page(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------")

    def test_display_with_three_pages(self):
        album = PhotoAlbum(3)
        for _ in range(8):
            album.add_photo("asdf")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------")


if __name__ == "__main__":
    unittest.main()
