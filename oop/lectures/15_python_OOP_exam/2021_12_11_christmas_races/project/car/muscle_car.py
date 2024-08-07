from project.car.car import Car


class MuscleCar(Car):
    MIN_SPEED = 250
    MAX_SPEED = 450

    def min_speed_limit(self):
        return self.MIN_SPEED

    def max_speed_limit(self):
        return self.MAX_SPEED
