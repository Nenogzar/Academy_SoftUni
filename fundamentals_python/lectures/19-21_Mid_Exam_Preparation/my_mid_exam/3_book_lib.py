shelf = input().split("&")

while True:
    command = input().split(" | ")
    action = command[0]

    if action == "Done":
        break

    elif action == "Add Book":
        book_name = command[1]
        if book_name not in shelf:
            shelf.insert(0, book_name)

    elif action == "Take Book":
        book_name = command[1]
        if book_name in shelf:
            shelf.remove(book_name)

    elif action == "Swap Books":
        book1 = command[1]
        book2 = command[2]
        if book1 in shelf and book2 in shelf:
            index1, index2 = shelf.index(book1), shelf.index(book2)
            shelf[index1], shelf[index2] = shelf[index2], shelf[index1]

    elif action == "Insert Book":
        book_name = command[1]
        if book_name not in shelf:
            shelf.append(book_name)

    elif action == "Check Book":
        index = int(command[1])
        if 0 <= index < len(shelf):
            print(shelf[index])

print(", ".join(shelf))


""" """

def add_book(shelf, book_name):
    if book_name not in shelf:
        shelf.insert(0, book_name)

def take_book(shelf, book_name):
    if book_name in shelf:
        shelf.remove(book_name)

def swap_books(shelf, book1, book2):
    if book1 in shelf and book2 in shelf:
        index1, index2 = shelf.index(book1), shelf.index(book2)
        shelf[index1], shelf[index2] = shelf[index2], shelf[index1]

def insert_book(shelf, book_name):
    if book_name not in shelf:
        shelf.append(book_name)

def check_book(shelf, index):
    if 0 <= index < len(shelf):
        print(shelf[index])

shelf = input().split("&")

while True:
    command = input().split(" | ")
    action = command[0]

    if action == "Done":
        break

    elif action == "Add Book":
        add_book(shelf, command[1])

    elif action == "Take Book":
        take_book(shelf, command[1])

    elif action == "Swap Books":
        swap_books(shelf, command[1], command[2])

    elif action == "Insert Book":
        insert_book(shelf, command[1])

    elif action == "Check Book":
        check_book(shelf, int(command[1]))

print(", ".join(shelf))

