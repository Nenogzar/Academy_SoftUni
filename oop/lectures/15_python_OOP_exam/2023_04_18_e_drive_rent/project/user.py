from project.validation.validation import Validation


class User:
    increases_points = 0.5
    decreases_points = 2.0
    def __init__(self,first_name: str, last_name: str, driving_license_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.driving_license_number = driving_license_number
        self.rating = 0
        self.is_blocked = False     # represents the user’s blocked status.

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        Validation.validate_empty_str_white_space(value,"First name cannot be empty!")
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        Validation.validate_empty_str_white_space(value, "Last name cannot be empty!" )
        self.__last_name = value
    
    @property
    def driving_license_number(self):
        return self.__driving_license_number
    
    @driving_license_number.setter
    def driving_license_number(self, value):
        Validation.validate_empty_str_white_space(value,"Driving license number is required!")
        self.__driving_license_number = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        Validation.valid_positive_number(value,"Users rating cannot be negative!")
        self.__rating = value

    # thanks to Bilyana Panova
    def increase_rating(self):
        # if (self.rating + self.increases_points) > 10:
        #     self.rating = 10
        # else:
        #     self.rating += self.increases_points
        self.rating = min(10, self.rating + self.increases_points)

    def decrease_rating(self):
        # result = self.rating - self.decreases_points
        # if result < 0:
        #     self.rating = 0
        #     self.is_blocked = True
        # else:
        #     self.rating -= 2.0


        if(self.rating - self.decreases_points) < 0:
            self.rating = 0
            self.is_blocked = True
        else:
            self.rating -= self.decreases_points
        #self.rating = max(0, self.rating - self.decreases_points)

    def __str__(self):
        return f"{self.first_name} {self.last_name} Driving license: {self.driving_license_number} Rating: {self.rating}"


