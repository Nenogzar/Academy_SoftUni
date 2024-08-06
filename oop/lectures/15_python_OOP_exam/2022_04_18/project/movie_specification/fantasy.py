from project.movie_specification.movie import Movie
from project.user import User


class Fantasy(Movie):
    _restrict_age = 6
    _message = f"Fantasy movies must be restricted for audience under {_restrict_age} years!"

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = _restrict_age ):
        super().__init__(title, year, owner, age_restriction)


    def details(self):
        return f"Fantasy - Title:{self.title}, " \
                            f"Year:{self.year}, " \
                            f"Age restriction:{self.age_restriction}, " \
                            f"Likes:{self.likes}, " \
                            f"Owned by:{self.owner.username}"

