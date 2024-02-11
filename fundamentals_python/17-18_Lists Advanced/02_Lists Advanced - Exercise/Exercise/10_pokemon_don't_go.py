pokemons = [int(n) for n in input().split()]
sum_of_captures_pokemons = []


def capture_pokemons(index, pokemons):
    first_element = int(pokemons[0])
    last_element = int(pokemons[-1])
    if index < 0:
        sum_of_captures_pokemons.append(first_element)  # appends the first element
        del pokemons[0]                     # deletes element at current_index 0
        pokemons.insert(0, last_element)    # puts last element to current_index 0

    elif index > len(pokemons) - 1:
        sum_of_captures_pokemons.append(last_element)  # appends the last element
        del pokemons[-1]                    # deletes element at current_index -1
        pokemons.insert(len(pokemons), first_element)  # puts first element at current_index -1

    if 0 <= index < len(pokemons):
        if index == len(pokemons):
            sum_of_captures_pokemons.append(pokemons[index - 1])
            del pokemons[index - 1]
        else:
            sum_of_captures_pokemons.append(pokemons[index])
            del pokemons[index]

    for counter, number in enumerate(pokemons):
        if number <= sum_of_captures_pokemons[-1]:
            pokemons[counter] = number + sum_of_captures_pokemons[-1]
        elif number > sum_of_captures_pokemons[-1]:
            pokemons[counter] = number - sum_of_captures_pokemons[-1]


while len(pokemons) > 0:
    current_position = int(input())
    capture_pokemons(current_position, pokemons)

print(sum(sum_of_captures_pokemons))


""" 2  Ivan Shopov """

distance = [int(number) for number in input().split()]
sum_of_removed_elements = 0
while distance: # while len(distance) > 0
    index = int(input())
    removed_element = 0
    if index < 0:
        removed_element = distance[0]
        distance[0] = distance[-1]
    elif index >= len(distance):
        removed_element = distance[-1]
        distance[-1] = distance[0]
    else:  # Index is valid
        removed_element = distance.pop(index)
    sum_of_removed_elements += removed_element
    for manipulating_index in range(len(distance)):
        if distance[manipulating_index] <= removed_element:
            distance[manipulating_index] += removed_element
        else:  # distance_list[manipulating_index] > removed_element
            distance[manipulating_index] -= removed_element
print(sum_of_removed_elements)


""" 3 Ceo """
distance_to_pokemon = [int(x) for x in input().split()]

result_ = []


while distance_to_pokemon:
    index_ = int(input())
    captured_pokemon = ""
    if index_ < 0:
        captured_pokemon = distance_to_pokemon.pop(0)
        distance_to_pokemon.insert(0, distance_to_pokemon[-1])
    elif index_ >= len(distance_to_pokemon):
        captured_pokemon = distance_to_pokemon.pop(-1)
        distance_to_pokemon.append(distance_to_pokemon[0])
    if not captured_pokemon:
        captured_pokemon = distance_to_pokemon.pop(index_)
    result_.append(captured_pokemon)
    for pos, pokemon in enumerate(distance_to_pokemon):
        if pokemon <= captured_pokemon:
            distance_to_pokemon[pos] += captured_pokemon
        else:
            distance_to_pokemon[pos] -= captured_pokemon

print(sum(result_))
