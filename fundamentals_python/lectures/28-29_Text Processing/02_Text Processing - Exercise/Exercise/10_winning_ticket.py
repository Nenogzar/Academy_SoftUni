tickets = input().replace(" ", "")
tickets = tickets.split(",")
winning_symbols = ["@", "#", "$", "^"]

for ticket in tickets:
    is_jackpot = False
    normal_win = False

    if len(ticket) == 20:
        first_half = ticket[:len(ticket) // 2]
        second_half = ticket[len(ticket) // 2:]
        for symbol in winning_symbols:
            if 20 * symbol in ticket:
                is_jackpot = True
                break

            elif 6 * symbol in first_half and 6 * symbol in second_half:
                symbols = 6
                for index in range(7, 11):  # checking for extra consecutive symbols
                    if index * symbol in first_half and index * symbol in second_half:
                        symbols += 1
                normal_win = True
                break

        if normal_win:
            print(f'ticket "{ticket}" - {symbols}{symbol}')
        elif is_jackpot:
            print(f'ticket "{ticket}" - 10{symbol} Jackpot!')
        elif not normal_win and not is_jackpot:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")




""" CEO """



tickets_sting = input().split(", ")
symbols = ['@', '#', '$', '^']


def get_max_in_a_row(string, symbol):
    next_, current = 0, 0
    for x in range(len(string)):
        if string[x] == symbol:
            next_ += 1
            if x == len(string) - 1:
                if current < next_:
                    current = next_
        else:
            if current < next_:
                current = next_
            next_ = 0
    return current


for ticket_characters in tickets_sting:
    ticket_characters = ticket_characters.replace(" ", "")
    if len(ticket_characters) == 20:
        how_long = int(len(ticket_characters) / 2)
        left_side, right_side = ticket_characters[:how_long], ticket_characters[how_long:]
        for symbol in symbols:
            sum_of_l, sum_of_r = get_max_in_a_row(left_side, symbol), get_max_in_a_row(right_side, symbol)
            if sum_of_l == sum_of_r == 10:
                print(f'ticket "{ticket_characters}" - 10{symbol} Jackpot!')
                break
            winners_price = min(sum_of_l, sum_of_r)
            if winners_price >= 6:
                print(f'ticket "{ticket_characters}" - {winners_price}{symbol}')
                break
        else:
            print(f'ticket "{ticket_characters}" - no match')
    else:
        print("invalid ticket")




""" Ivan Shopov """


def check_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ['@', '#', '$', '^']
    left_part = ticket[:10]
    right_part = ticket[10:]
    for current_winning_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbol_repetition = current_winning_symbol * uninterrupted_match_length
            # Winning ticket
            if winning_symbol_repetition in left_part \
                    and winning_symbol_repetition in right_part:
                # Jackpot ticket
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{current_winning_symbol} Jackpot!'
                # Just a winning ticket
                return f'ticket "{ticket}" - {uninterrupted_match_length}{current_winning_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for current_ticket in tickets:
    print(check_ticket(current_ticket))
