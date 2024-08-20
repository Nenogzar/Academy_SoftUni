import copy


class Person:
    def __init__(self, position):
        self.position = position

class MovePerson(Person):
    def __init__(self, position, is_free):
        super().__init__(position)
        self.is_free = is_free

    def walk_north(self, dist):
        if self.is_free:
            self.position[1] += dist

    def walk_east(self, dist):
        if self.is_free:
            self.position[0] += dist


class FreePerson(MovePerson):
    def __init__(self, position):
        super().__init__(position, True)


class Prisoner(MovePerson):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super().__init__(copy.copy(self.PRISON_LOCATION), False)


prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")

free_person = FreePerson([0,0])
print("The person tryning to walk to north by 10 and east by -3.")

try:
    free_person.walk_north(10)
    free_person.walk_east(-3)
except:
    pass

print(f"The current position of the {free_person.__class__.__name__}: {free_person.position}")
