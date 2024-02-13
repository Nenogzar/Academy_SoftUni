single_digit = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
                5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
                9: 'nine'}

teen = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

tens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
        70: 'seventy', 80: 'eighty', 90: 'ninety'}


def spell_single_digit(digit):
    if 0 <= digit < 10:
        return single_digit[digit]


def spell_two_digits(number):
    if 10 <= number < 20:
        return teen[number]

    if 20 <= number < 100:
        div = (number // 10) * 10
        mod = number % 10
        if mod != 0:
            return tens[div] + "-" + spell_single_digit(mod)
        else:
            return tens[number]


def spell_three_digits(number):
    if 100 <= number < 1000:
        div = number // 100
        mod = number % 100
        if mod != 0:
            if mod < 10:
                return spell_single_digit(div) + " hundred " + \
                    spell_single_digit(mod)
            elif mod < 100:
                return spell_single_digit(div) + " hundred " + \
                    spell_two_digits(mod)
        else:
            return spell_single_digit(div) + " hundred"


def spell(number):
    if -1000000000 < number < 1000000000:
        if number == 0:
            return spell_single_digit(number)
        a = ""
        neg = False
        if number < 0:
            neg = True
            number *= -1
        loop = 0
        while number:
            mod = number % 1000
            if mod != 0:
                c = spell_three_digits(mod) or spell_two_digits(mod) \
                    or spell_single_digit(mod)
                if loop == 0:
                    a = c + " " + a
                elif loop == 1:
                    a = c + " thousand " + a
                elif loop == 2:
                    a = c + " million " + a
            number = number // 1000
            loop += 1
        if neg:
            return "negative " + a
        return a
number = int(input("the number is? "))
print(spell(number))