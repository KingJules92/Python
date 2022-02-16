from random import choice

player_wins = 0
computer_wins = 0
tie = 0

winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    score = f"Player Score: {player_wins} Computer Score: {computer_wins}"
    print(score)
    # Computer Player Choice
    symbol = ["rock", "paper", "scissors"]
    computer_pick = choice(symbol)

    # Human Player Choice
    print("Pick a weapon:\nrock, paper or scissors")
    user_pick = input()

    # Event of a Draw
    if user_pick == computer_pick:
        print("TIE!")
        tie += 1
    # Player picks ROCK
    elif user_pick == "rock":
        print(f"Your opponent chose {computer_pick}")
        if computer_pick == "paper":
            print("YOU LOSE!")
            computer_wins += 1
        elif computer_pick == "scissors":
            print("YOU WIN!")
            player_wins += 1

    # Player picks PAPER
    elif user_pick == "paper":
        print(f"Your opponent chose {computer_pick}")
        if computer_pick == "rock":
            print("YOU WIN!")
            player_wins += 1
        elif computer_pick == "scissors":
            print("YOU LOSE!")
            computer_wins += 1

    # Player picks SCISSORS
    elif user_pick == "scissors":
        print(f"Your opponent chose {computer_pick}")
        if computer_pick == "paper":
            print("YOU WIN!")
            player_wins += 1
        elif computer_pick == "rock":
            print("YOU LOSE!")
            computer_wins += 1
    
    else:
        print("something went wrong")
    
    print("********")

print("You won a match of Rock-Paper-Scissors")
print(score)