# Choice Player 1
print("Player 1! Choose your weapon:\nrock, paper, scissors")
player1_pick = input()

# Low Tier Anti-Cheat-Mechanism
print("* * * * * NO CHEATING * * * * *\n\n"*30)

# Choice Player 2
print("Player 2! Choose your weapon:\nrock, paper, scissors")
player2_pick = input()

# Both players choose same weapon
if player1_pick == player2_pick:
    print("DRAW!")

# Player 1 picks ROCK
elif player1_pick == "rock":
    if player2_pick == "paper":
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")

# Player 1 picks PAPER
elif player1_pick == "paper":
    if player2_pick == "scissors":
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")

# Player 1 picks SCISSORS
elif player1_pick == "scissors":
    if player2_pick == "rock":
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")

else:
    print("something went wrong!")