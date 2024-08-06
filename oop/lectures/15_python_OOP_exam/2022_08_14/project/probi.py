from project.jockey import Jockey

try:
    j = Jockey("Koko", 21)
except ValueError as e:
    print(e)

