import re

def find_cool_emojis(text):
    def calculate_cool_threshold(text):
        all_digits = ''.join(x for x in text if x.isdigit())
        cool_threshold = 1
        for num in all_digits:
            cool_threshold *= int(num)
        return cool_threshold

    cool_threshold = calculate_cool_threshold(text)
    print(f"Cool threshold: {cool_threshold}")

    patterns = re.compile(r"(::)(?P<emoji>[A-Z][a-z]{2,})(::)|(\*\*)(?P<emoji2>[A-Z][a-z]{2,})(\*\*)")
    emojis_found = list(re.finditer(patterns, text))
    print(f"{len(emojis_found)} emojis found in the text. The cool ones are:")
    cool_emojis = []

    for found in emojis_found:
        if found["emoji"]:
            result = found["emoji"]
        elif found["emoji2"]:
            result = found["emoji2"]

        find_cool = sum([ord(letter) for letter in result])
        if find_cool >= cool_threshold:
            cool_emojis.append(found[0])

    return cool_emojis

def main():
    main_string = input()
    cool_emojis = find_cool_emojis(main_string)
    for emoji in cool_emojis:
        print(emoji)

if __name__ == "__main__":
    main()
