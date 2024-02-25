class Stamps:
    all_stamps = []  # Class variable to store all instances

    def __init__(self, validation_date, BG, MI, SC, Ivert, SG):
        self.stamp_id = None
        self.validation_date = validation_date
        self.validation_year = None
        self.BG = BG
        self.MI = MI
        self.SC = SC
        self.Ivert = Ivert
        self.SG = SG
        self.Period = None
        self.period_id = None

        # Call the year_id method to set the year attribute
        self.year_id()
        # Call the period_info method to set the Period attribute
        self.period_info()
        # Call the ID_generator method to set the shtamp ID
        self.ID_generator()
        # Add the current instance to the class variable
        Stamps.all_stamps.append(self)

    def year_id(self):
        day, month, year = map(str, self.validation_date.split('.'))
        self.validation_year = year

    def period_info(self):
        self.period_id = ""  # Initialize to an empty string
        if int(self.validation_year) <= 1908:
            self.Period = "Княжество България"
            self.period_id = 1
        elif int(self.validation_year) <= 1946:
            self.Period = "Царство България"
            self.period_id = 2
        elif int(self.validation_year) <= 1999:
            self.Period = "Народна Република България"
            self.period_id = 3
        else:
            self.Period = "Република България"
            self.period_id = 4

    def ID_generator(self):
        self.stamp_id = f"{self.period_id}_{self.validation_year}_{self.BG}"


# Create an instance of Stamps
stamp1 = Stamps("01.05.1879", 1, 1, 1, 1, 1)
stamp348 = Stamps("25.02.1938", 348, 338, 324, 348, 326)
stamp878 = Stamps("11.11.1952", 878, 836, 779, 836, 856)
# print(f"Марка номер по БГ каталог {stamp1.BG} е издание през {stamp1.validation_year} и получава ID: {stamp1.stamp_id}")
# print(f"Марка номер по БГ каталог {stamp348.BG} е издание през {stamp348.validation_year} и получава ID: {stamp348.stamp_id}")

# Iterate over the instances and print their details
for stamp in Stamps.all_stamps:
    print(
        f"Марка номер по БГ каталог {stamp.BG} е издание през {stamp.validation_year} и получава ID: {stamp.stamp_id}. \n"
        f"Тя е издарена през перида на {stamp.Period}\n"
        f"__________")
