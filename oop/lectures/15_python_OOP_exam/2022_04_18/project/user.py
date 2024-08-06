from project.validation.validation import Validation


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []  # contain all movies (objects) liked by the user
        self.movies_owned = []  # contain all movies (objects) owned by the user

    @property
    def username(self):
        return self.__name

    @username.setter
    def username(self, value):
        Validation.valid_empty_str(value, "Invalid username!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validation.valid_number(value, 6, f"Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        liked_movies_str = "No movies liked." if not self.movies_liked else \
            "\n".join(movie.details() for movie in self.movies_liked)
        owned_movies_str = "No movies owned." if not self.movies_owned else \
            "\n".join(movie.details() for movie in self.movies_owned)

        return (
            f"Username: {self.username}, Age: {self.age}\n"
            f"Liked movies:\n{liked_movies_str}\n"
            f"Owned movies:\n{owned_movies_str}"
        )
