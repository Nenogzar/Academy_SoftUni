class Stamps:
    all_stamps = []

    def __init__(self, validation_date: str, BG, MI, SC, Ivert, SG):

        self.validation_date = validation_date
        self.BG = BG
        self.MI = MI
        self.SC = SC
        self.Ivert = Ivert
        self.SG = SG

        Stamps.all_stamps.append(self)

    def year_id(self):
        day, month, year = map(str, self.validation_date.split('.'))
        validation_year = year
        return validation_year

    def period_info(self):
        validation_year = self.year_id()
        period_id = ""
        period = ""
        if int(validation_year) <= 1908:
            period = "Principality of Bulgaria"
            period_id = 1
        elif int(validation_year) <= 1946:
            period = "Kingdom of Bulgaria"
            period_id = 2
        elif int(validation_year) <= 1999:
            period = "People's Republic of Bulgaria"
            period_id = 3
        else:
            period = "Republic of Bulgaria"
            period_id = 4
        return period_id, period

    def ID_generator(self):
        validation_year = self.year_id()
        stamp_id = f"{period_id}_{validation_year}_{self.BG}"
        return stamp_id



# Create an instance of Stamps
stamp1 = Stamps("01.05.1879", 1, 1, 1, 1, 1)
stamp2 = Stamps("01.05.1879", 2, 2, 2, 2, 2)
stamp348 = Stamps("25.02.1938", 348, 338, 324, 348, 326)
stamp878 = Stamps("11.11.1952", 878, 836, 779, 836, 856)

for stamp in Stamps.all_stamps:
    period_id, period = stamp.period_info()
    print(
        f"Postmark number according to BG catalog {stamp.BG} is an edition in {period} and gets an ID: {stamp.ID_generator()}. \n"
        f"It was issued during the period of {period_id}\n"
        f"__________")
