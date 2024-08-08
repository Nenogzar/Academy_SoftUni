from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert
from project.validation.validation import Validation


class ConcertTrackerApp:

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    @property
    def valid_misician_type(self):
        return {"Guitarist": Guitarist,
                "Drummer": Drummer,
                "Singer": Singer}

    def create_musician(self, musician_type: str, name: str, age: int):
        Validation.validate_ganre_or_music(musician_type, self.valid_misician_type, "Invalid musician type!")

        if any(m.name == name for m in self.musicians):
            raise Exception(f"{name} is already a musician!")

        new_musicians = self.valid_misician_type[musician_type](name, age)
        self.musicians.append(new_musicians)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if any(m.name == name for m in self.bands):
            raise Exception(f"{name} band is already created!")

        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        if any(c.place == place for c in self.concerts):
            raise Exception(f"{place} is already registered for {genre} concert!")

        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next((m for m in self.musicians if m.name == musician_name), None)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        band = next((b for b in self.bands if b.name == band_name), None)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = next((b for b in self.bands if b.name == band_name), None)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = next((m for m in band.members if m.name == musician_name), None)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        concert = next((c for c in self.concerts if c.place == concert_place), None)
        if not concert:
            raise Exception(f"No concert is registered at {concert_place}!")

        band = next((b for b in self.bands if b.name == band_name), None)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        has_singer = any(isinstance(m, Singer) for m in band.members)
        has_drummer = any(isinstance(m, Drummer) for m in band.members)
        has_guitarist = any(isinstance(m, Guitarist) for m in band.members)

        if not (has_singer and has_drummer and has_guitarist):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        genre = concert.genre
        for musician in band.members:
            if genre == "Rock":
                if isinstance(musician, Drummer) and "play the drums with drumsticks" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if isinstance(musician, Singer) and "sing high pitch notes" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if isinstance(musician, Guitarist) and "play rock" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

            elif genre == "Metal":
                if isinstance(musician, Drummer) and "play the drums with drumsticks" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if isinstance(musician, Singer) and "sing low pitch notes" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if isinstance(musician, Guitarist) and "play metal" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

            elif genre == "Jazz":
                if isinstance(musician, Drummer) and "play the drums with drum brushes" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if isinstance(musician, Singer):
                    if "sing high pitch notes" not in musician.skills or "sing low pitch notes" not in musician.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if isinstance(musician, Guitarist) and "play jazz" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {genre} concert in {concert_place}."
