import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players(1-4): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <=4:
           break
        else:
            print("Must be between 2 - 4 players")
    else:
        print("Invalid, try again")

max_score = 50
player_score = [0 for _ in range(players)]

 while max(player_scores) < max_score:
    for player_idx in range(players):
     print("\nPlayer number", player_idx +1,"turn as just started!\n")
     current_score = 0

      While True:
          should_roll = input("Would you like to roll (y)? ")
          if should_roll.lower() !="y":
             break
             (function) roll() -> int
    value = roll()
    if value == 1:
        print("You rolled a 1! Turn done!")
        break
    else:
        current_score += value
        print("You rolled a:", value)

    print("Your score is:", current_score)
print(player_score)

