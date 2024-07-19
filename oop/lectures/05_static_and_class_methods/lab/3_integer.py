# ******* Class and Static Methods ******* #

# *******  3_integer  ******* #

# *******  TASK CONDITION  ******* #
"""
https://judge.softuni.org/Contests/2430/Static-and-Class-Methods-Lab

Create a class called Integer.
    Upon initialization, it should receive a single parameter value (int).
    It should have 3 additional methods:

•	from_float(float_value)
        - creates a new instance by flooring the provided floating number.
            If the value is not a float,
                return "value is not a float"

•	from_roman(value)
        - creates a new instance by converting the roman number (as string) to an integer

•	from_string(value)
        - creates a new instance by converting the string to an integer (if the value cannot be converted,
                return a message "wrong type")

"""


##########: SOLUTION :##########
class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value: str):
        roman_numerals = {"I": 1,
                          "V": 5,
                          "X": 10,
                          "L": 50,
                          "C": 100,
                          "D": 500,
                          "M": 1000
                          }

        int_value = 0

        for i in range(len(value)):
            if value[i] in roman_numerals:
                if (
                        i + 1 < len(value)
                        and roman_numerals[value[i]] < roman_numerals[value[i + 1]]
                ):
                    int_value -= roman_numerals[value[i]]
                else:
                    int_value += roman_numerals[value[i]]
        return cls(int_value)


    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, str):
            return "wrong type"

        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"


##########: TEST CODE :##########


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))

"""
Output:
10
4
value is not a float
wrong type

 """
##########: UNITTEST :##########

import unittest


class IntegerTests(unittest.TestCase):
    def test_basic_init(self):
        integer = Integer(1)
        self.assertEqual(integer.value, 1)

    def test_from_float_success(self):
        integer = Integer.from_float(2.5)
        self.assertEqual(integer.value, 2)

    def test_from_float_wrong_type(self):
        result = Integer.from_float("2.5")
        self.assertEqual(result, "value is not a float")

    def test_from_roman(self):
        integer = Integer.from_roman("XIX")
        self.assertEqual(integer.value, 19)

    def test_from_string_success(self):
        integer = Integer.from_string("10")
        self.assertEqual(integer.value, 10)

    def test_from_string_wrong_type(self):
        result = Integer.from_string(1.5)
        self.assertEqual(result, "wrong type")


if __name__ == "__main__":
    unittest.main()
