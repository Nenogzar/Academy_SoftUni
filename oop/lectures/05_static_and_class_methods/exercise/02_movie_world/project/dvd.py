from calendar import month_name


class DVD:
    def __init__(self, name: str, dvd_id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented: bool = False

    #     @classmethod
    #     def from_date(cls, dvd_id: int, name: str, date: str, age_restriction: int):
    #         day, month, year = map(int, date.split('.'))
    #         months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    #         creation_month = months[month - 1]
    #         return cls(name, dvd_id, year, creation_month, age_restriction)
    #
    #     def __repr__(self):
    #         status = "rented" if self.is_rented else "not rented"
    #         return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"

    #
    # @classmethod
    # def from_date(cls, dvd_id: int, name: str, date: str, age_restriction: int):
    #     month, year = [int(x) for x in date.split(".")[1:]]
    #     months = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June",
    #               7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
    #     return cls(name, dvd_id, year, months[month], age_restriction)
    #

    @classmethod
    def from_date(cls, dvd_id: int, name: str, date: str, age_restriction: int):
        day, month, year = map(int, date.split('.'))
        creation_month = month_name[month]
        return cls(name, dvd_id, year, creation_month, age_restriction)

    def __repr__(self):
        status = "rented" if self.is_rented else "not rented"
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction "
                f"{self.age_restriction}. Status: {status}")
