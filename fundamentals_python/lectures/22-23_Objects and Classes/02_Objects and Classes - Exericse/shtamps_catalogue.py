class Shtamps:
    all_stamps = []  # Class variable to store all instances

    def __init__(self, data_iz, BG, MI, SC, Ivert, SG):
        self.data_iz = data_iz
        self.BG = BG
        self.MI = MI
        self.SC = SC
        self.Ivert = Ivert
        self.SG = SG
        self.year = None
        self.Period = None
        self.shtamp_id = None
        self.period_id = None

        # Call the year_id method to set the year attribute
        self.year_id()
        # Call the period_info method to set the Period attribute
        self.period_info()
        # Call the ID_generator method to set the shtamp ID
        self.ID_generator()
        # Add the current instance to the class variable
        Shtamps.all_stamps.append(self)

    def year_id(self):
        day, month, year = map(str, self.data_iz.split('.'))
        self.year = year

    def period_info(self):
        self.period_id = ""  # Initialize to an empty string
        if int(self.year) <= 1908:
            self.Period = "Княжество България"
            self.period_id = 1
        elif int(self.year) <= 1946:
            self.Period = "Царство България"
            self.period_id = 2
        elif int(self.year) <= 1999:
            self.Period = "Народна Република България"
            self.period_id = 3
        else:
            self.Period = "Република България"
            self.period_id = 4

    def ID_generator(self):
        self.shtamp_id = f"{self.period_id}_{self.year}_{self.BG}"


# Create an instance of Shtamps
stamp1 = Shtamps("01.05.1879", 1, 1, 1, 1, 1)
stamp348 = Shtamps("25.02.1938", 348, 338, 324, 348, 326)
stamp878 = Shtamps("11.11.1952", 878, 836, 779, 836, 856)
# print(f"Марка номер по БГ каталог {stamp1.BG} е издание през {stamp1.year} и получава ID: {stamp1.shtamp_id}")
# print(f"Марка номер по БГ каталог {stamp348.BG} е издание през {stamp348.year} и получава ID: {stamp348.shtamp_id}")

# Iterate over the instances and print their details
for stamp in Shtamps.all_stamps:
    print(f"Марка номер по БГ каталог {stamp.BG} е издание през {stamp.year} и получава ID: {stamp.shtamp_id}. \n"
          f"Тя е издарена през перида на {stamp.Period}\n"
          f"__________")
