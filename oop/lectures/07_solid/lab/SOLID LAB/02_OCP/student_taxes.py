class StudentTaxes:
    def __init__(self, name, semester_tax, avg_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = avg_grade

    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.4
        return 0

class AdditionalDiscount(StudentTaxes):
    def get_discount(self):
        result = super().get_discount()
        if result:
            return result
        if 4 < self.average_grade <= 5:
            return self.semester_tax * 0.2

st = AdditionalDiscount('Ivan Andonov', 250, 6)
st.get_discount()
print(st.semester_tax)
print(st.get_discount())
