import random

options = ("rock", "paper", "scissor")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice between Rock, Paper, Scissor ")

    print(f"Player chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissor":
        print("you win!")
    elif player == "paper" and computer == "rock":
        print("you win!")
    elif player == "scissors" and computer == "paper":
        print("you win!")
    else:
        print("you lose!")

    play_again = input("Do you want to play again? (y/n) ").lower()
    if not play_again == "y":
        running = False

print("Thank you for playing!")