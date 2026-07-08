def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winnner(board, player):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    for condition in winning_combinations:
        if board[condition[0]-1] == board[condition[1]-1] == board[condition[2]-1] == player:
            return True
    return False


def check_draw(borad):
    cnt = 0
    for i in borad:
        if i == " ":
            cnt += 1
    return True if cnt <= 0 else False


def game():
    player = "X"
    board = [" "]*9
    game_running = True
    print("This is the tic-tac-toe Game.\n")
    while game_running:

        print_board(board)
        print(f"It's player {player}'s turn.")
        try:
            move = int(input("Now choose where u wanna put your mark(1-9): "))-1
        except ValueError:
            print("Invalid Input!! Please enter a number.")
            continue

        if 1 <= move+1 <= 9:
            if board[move] != " ":
                print("This spot is already taken. Try a valid move...")
                continue
            board[move] = player
            if check_winnner(board, player):
                print_board(board)
                print(
                    f"\nContratulation!! Player {player} has won the game....\n")
                game_running = False

            elif check_draw(board):
                print_board(board)
                print(f"It's a Draw.")
                game_running = False

            else:
                player = "O" if player == "X" else "X"
        else:
            print("you can only have move between 1 to 9.")
            continue


if __name__ == "__main__":
    game()
