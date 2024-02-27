class Stamps:
    all_stamps = []

    def __init__(self, validation_date: str, BG: int, MI: int, SC: int, Ivert: int, SG: int):

        self.validation_date = validation_date
        self.BG = BG
        self.MI = MI
        self.SC = SC
        self.Ivert = Ivert
        self.SG = SG
        self.period = "Bulgaria"
        self.period_id = 0
        self.stamp_id = ""
        self.validation_year = 1879
        Stamps.all_stamps.append(self)

    def year_id(self):
        day, month, year = map(str, self.validation_date.split('.'))
        self.validation_year = year


    def period_info(self):
        period_id = ""
        period = ""
        if self.validation_year <= 1908:
            self.period = "Principality of Bulgaria"
            self.period_id = 1
        elif self.validation_year <= 1946:
            self.period = "Kingdom of Bulgaria"
            self.period_id = 2
        elif self.validation_year <= 1999:
            self.period = "People's Republic of Bulgaria"
            self.period_id = 3
        else:
            self.period = "Republic of Bulgaria"
            self.period_id = 4


    def ID_generator(self):
        validation_year = self.year_id()
        self.stamp_id = f"{self.period_id}_{self.validation_year}_{self.BG}"


# Create an instance of Stamps
stamp1 = Stamps("01.05.1879", 1, 1, 1, 1, 1)
stamp2 = Stamps("01.05.1879", 2, 2, 2, 2, 2)
stamp348 = Stamps("25.02.1938", 348, 338, 324, 348, 326)
stamp878 = Stamps("11.11.1952", 878, 836, 779, 836, 856)

for stamp in Stamps.all_stamps:
    stamp.period_info()
    stamp.ID_generator()
    print(
        f"Postmark number according to BG catalog {stamp.BG} is an edition in {stamp.period} and gets an ID: {stamp.stamp_id}. \n"
        f"It was issued during the period of {stamp.period_id}\n"
        f"__________"
    )
    print(f"BG: {stamp.BG}, Period: {stamp.period}, Period ID: {stamp.period_id}, Stamp ID: {stamp.stamp_id}")
    print("____________________")

