secret_key = [int(x) for x in input().split()]
secret_msg = input()

how_long = len(secret_key)
while secret_msg != "find":
    secret_text = "".join([chr(ord(secret_msg[i]) - secret_key[i % how_long]) for i in range(len(secret_msg))])
    item = secret_text.split("&")[-2]
    location = secret_text.split("<")[-1][:-1]
    print(f"Found {item} at {location}")
    secret_msg = input()

""" """

keys = input().split()
index_of_keys = 0

all_results = []

string = input()
while string != "find":
    result = ''
    for character in string:
        if index_of_keys >= len(keys):
            index_of_keys = 0
        result += chr(ord(character) - int(keys[index_of_keys]))
        index_of_keys += 1

    all_results.append(result)
    result, index_of_keys = '', 0
    string = input()

for location in all_results:
    start_index_material = location.index("&") + 1
    end_index_material = location.index("&", start_index_material + 1)
    start_coordinates, end_coordinates = location.index("<") + 1, location.index(">")
    print(f"Found {location[start_index_material:end_index_material]} at {location[start_coordinates:end_coordinates]}")
