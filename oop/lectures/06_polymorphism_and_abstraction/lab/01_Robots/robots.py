class Robot:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        """Is overridden in:
        MedicalRobot
        ChefRobot
        WarRobot"""
        return 1

    def __add__(self, other):
        return self.sensors_amount() + other.sensors_amount()


class MedicalRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 6


class ChefRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 4


class WarRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 12


class New_robot(Robot):
    pass


def result(robot):
    print(robot.sensors_amount())


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')
baby = New_robot('Phoncho')

result(basic_robot)
result(da_vinci)
result(moley)
result(griffin)
result(baby)

print(griffin + moley)
print(griffin.sensors_amount() + moley.sensors_amount())
