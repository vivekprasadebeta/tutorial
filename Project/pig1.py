import random

def roll_dice():
    return random.randint(1, 6)

def pig_game():
    player_score = 0
    computer_score = 0
    win_score = 100

    def player_turn(current_score):
        turn_score = 0
        while True:
            roll = input("Roll (r) or Hold (h)? ")
            if roll == 'r':
                dice = roll_dice()
                print(f"You rolled a {dice}")
                if dice == 1:
                    print("You rolled a 1. Turn ends.")
                    return 0
                else:
                    turn_score += dice
                    print(f"Current turn score: {turn_score}")
            elif roll == 'h':
                return current_score + turn_score

    def computer_turn(current_score):
        turn_score = 0
        while turn_score < 20:
            dice = roll_dice()
            print(f"Computer rolled a {dice}")
            if dice == 1:
                print("Computer rolled a 1. Turn ends.")
                return 0
            else:
                turn_score += dice
        return current_score + turn_score

    while player_score < win_score and computer_score < win_score:
        print("\nPlayer's turn:")
        player_score = player_turn(player_score)
        print(f"Player's total score: {player_score}\n")
        if player_score >= win_score:
            print("Player wins!")
            break

        print("Computer's turn:")
        computer_score = computer_turn(computer_score)
        print(f"Computer's total score: {computer_score}\n")
        if computer_score >= win_score:
            print("Computer wins!")
            break