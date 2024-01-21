search_books = input()
book = input()
check_book = 0

while book != "No More Books":
    check_book += 1

    if book == search_books:
        print(f'You checked {check_book - 1} books and found it.')
        break

    book = input()
else:
    print(f'The book you search is not here!\n'
          f'You checked {check_book} books.')
