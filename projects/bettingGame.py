import random
MIN_BET = 1
MAX_BET = 500

MAX_LINES = 3
MIN_LINES = 1

ROWS = 3
COLS = 3

symbols = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

symbols_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
}


def check_winnings(lines, bet, value, coloms):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = coloms[0][line]
        for col in range(COLS):
            check_symbol = coloms[col][line]
            if symbol != check_symbol:
                break
        else:
            winnings += (value[symbol]*bet)
            winning_lines.append(line+1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_value in symbols.items():
        for _ in range(symbol_value):
            all_symbols.append(symbol)
    coloms = []

    for col in range(cols):
        colom = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            colom.append(value)
            current_symbols.remove(value)
        coloms.append(colom)

    return coloms


def print_slot_machine(columns):
    for row in range(ROWS):
        for col in range(COLS):
            if col != COLS - 1:
                print(columns[col][row], end=" | ")
            else:
                print(columns[col][row])


def get_deposite():
    while True:
        amount = input("How much would you like to deposite= $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater then Zero")
        else:
            print("amount must be a number")
    return amount


def get_bet():
    while True:
        bet = input("How much would you like to bet on each line= $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("bet must be greater then {} and less then {}".format(
                    MIN_BET, MAX_BET))
        else:
            print("bet must be a number")
    return bet


def get_lines():
    while True:
        lines = input("How many lines you wanna bet on (1-3)= ")
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINES <= lines <= MAX_LINES:
                break
            else:
                print("lines must be greater then {} and less then {}".format(
                    MIN_LINES, MAX_LINES))
        else:
            print("lines must be a number")
    return lines


def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"You do not have enough money in the deposite....Your 1current balance is : {balance}")
            continue
        else:
            break
    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    grid = get_slot_machine_spin(ROWS, COLS, symbols)
    print_slot_machine(grid)
    winnings, winning_lines = check_winnings(lines, bet, symbols_value, grid)
    print(f"You won ${winnings}")
    print(f"You won on lines : ", *winning_lines)

    return winnings - total_bet


def main():
    balance = get_deposite()

    while True:
        print(f"Your current balance is : ${balance}")
        choice = input("Press enter to play (q to quit).")
        if choice == 'q':
            break
        balance += spin(balance)
    print(f"You left with ${balance}")


main()
