class Validation:

    @staticmethod
    def valid_empty_str(name: str, message: str):
        if name == "":
            raise ValueError(message)

    @staticmethod
    def valid_number(number: int, valid_range: int, message: str):
        if number < valid_range:
            raise ValueError(message)



    @staticmethod
    def movie_owner(owner):
        if owner.__class__.__name__ != "User":
            raise ValueError("The owner must be an object of type User!")


    @staticmethod
    def user_owned_movie(client_class, movie_class):
        if movie_class.owner.username != client_class.username:
            raise Exception(f"{client_class.username} is not the owner of the movie {movie_class.title}!")
