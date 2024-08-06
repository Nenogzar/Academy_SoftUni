from project.movie_specification.movie import Movie



class Thriller(Movie):
    _restrict_age = 16
    _message = f"Thriller movies must be restricted for audience under {_restrict_age} years!"

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = _restrict_age ):
        super().__init__(title, year, owner, age_restriction)


    def details(self):
        return f"Thriller - Title:{self.title}, " \
                            f"Year:{self.year}, " \
                            f"Age restriction:{self.age_restriction}, " \
                            f"Likes:{self.likes}, " \
                            f"Owned by:{self.owner.username}"
