
import random
max_num = 6
min_num = 1


def roll():
    return random.randint(min_num, max_num)


while True:
    players = input("how mant players want to play (2-4) :")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Only 2 to 4 palyers can play the game. Try again...")
    else:
        print("Please enter a number. Try again...")

player_scores = [0]*players
# print(player_scores)
max_score = 50

while max(player_scores) < max_score:
    for player in range(players):
        print(
            f"\nIt's player number {player+1}'s turn\n Your total score is = {player_scores[player]}\n")
        current_score = 0
        while True:
            choice = input("Do u want to roll the dice? (y/n) ")
            if choice != 'y':
                break
            value = roll()
            if value == 1:
                print(">>>>>>You rolled a 1! You lose your turn!<<<<<<")
                current_score = 0
                break
            else:
                print(f"You rolled a {value}")
                current_score += value
                print(f"Your current score is {current_score}")
        player_scores[player] += current_score
        print(f"Your total score is {player_scores[player]}")

max_scr = max(player_scores)
winner = player_scores.index(max_scr)

print(
    f"\nthe winner is player number {winner+1} with a total score of {max_scr}\n")
