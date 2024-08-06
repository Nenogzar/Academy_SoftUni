from typing import List

from project.movie_specification.movie import Movie
from project.user import User
from project.validation.validation import Validation


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):

        # Съществува ли потребител с даденото име в списъка с потребители
        if any(u.username == username for u in self.users_collection):
            raise Exception("User already exists!")

        # Ако да, го добавям в списъка
        curr_user = User(username, age)
        self.users_collection.append(curr_user)
        return f"{username} registered successfully."



    def upload_movie(self, username: str, movie: Movie):
        user = next((u for u in self.users_collection if u.username == username), None)

        # Ако потребителят не съществува"""
        if user is None:
            raise Exception("This user does not exist!")

        # Ако намереният потребител не е собственик на филма"""
        # if movie.owner.username != username:
        #     raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        Validation.user_owned_movie(user,movie)

        # Проверка дали филмът вече е добавен"""
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        # Ако всички проверки са успешни, добавям филма в списъка
        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."


    def edit_movie(self, username: str, movie: Movie, **kwargs):
        # Проверка дали филмът е добавен в колекцията
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")


        # Проверка дали потребителят е собственик на филма
        user = next(u for u in self.users_collection if u.username == username)
        # if movie.owner.username != username:
        #     raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        Validation.user_owned_movie(user,movie)
        
        # Актуализиране на атрибутите на филма според kwargs
        for key, value in kwargs.items():
            if key == "title":
                movie.title = value
            elif key == "year":
                movie.year = value
            elif key == "age_restriction":
                movie.age_restriction = value

        return f"{username} successfully edited {movie.title} movie."


    def delete_movie(self, username: str, movie: Movie):
        # Проверка дали филмът е добавен в колекцията
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        
        # Проверка дали потребителят е собственик на филма
        user = next(u for u in self.users_collection if u.username == username)
        # if movie.owner.username != username:
        #     raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        Validation.user_owned_movie(user, movie)

        # Премахване на филма от списъка на филмите
        user = next(u for u in self.users_collection if u.username == username)
        user.movies_owned.remove(movie)

        # Премахване на филма от общата колекция
        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        # Проверка дали потребителят е собственик на филма
        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")


        user = next(u for u in self.users_collection if u.username == username)

        # Филмът харесан ли е
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        # Увеличаване на броя на харесванията и го добавям
        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."


    def dislike_movie(self,username: str, movie: Movie):
        user = next(u for u in self.users_collection if u.username == username)

        # Филмът харесан ли е  потребителя
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        # Намаля броя на харесванията на филма
        # премахва филма от списъка с харесани
        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        # Сортиране на филмите по година (низходящо) и след това по заглавие (азбучно)
        sorted_movies = sorted(self.movies_collection, key=lambda m: (-m.year, m.title))

        # Има ли филми в колекцията
        if not sorted_movies:
            return "No movies found."

        return "\n".join(movie.details() for movie in sorted_movies)


    def __str__(self):
         # Списък с потребител
        usernames = [user.username for user in self.users_collection]
        if not usernames:
            users_str = "All users: No users."
        else:
            users_str = "All users: " + ", ".join(usernames)

        # Списък с филми
        movie_titles = [movie.title for movie in self.movies_collection]
        if not movie_titles:
            movies_str = "All movies: No movies."
        else:
            movies_str = "All movies: " + ", ".join(movie_titles)
        return f"{users_str}\n{movies_str}"
