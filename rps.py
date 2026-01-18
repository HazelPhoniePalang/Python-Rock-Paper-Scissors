import random

OPTIONS = ("rock", "paper", "scissors")
SHORTCUTS = {
    "r": "rock",
    "p": "paper",
    "s": "scissors"
}

def get_player_choice():
    """Safely get and validate player input."""
    while True:
        choice = input("Enter Rock, Paper, or Scissors (r/p/s): ").strip().lower()

        if not choice:
            print("❌ Input cannot be empty. Please try again.")
            continue

        # Convert shortcut to full word
        if choice in SHORTCUTS:
            return SHORTCUTS[choice]

        if choice in OPTIONS:
            return choice

        print("❌ Invalid choice. Please enter Rock, Paper, or Scissors.")

def play_again_prompt():
    """Safely ask if the user wants to play again."""
    while True:
        answer = input("Do you want to play again? (y/n): ").strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("❌ Invalid input. Please enter 'y' or 'n'.")

print("🎮 Welcome to Rock, Paper, Scissors!")

running = True
while running:
    player = get_player_choice()
    computer = random.choice(OPTIONS)

    print(f"\nPlayer chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("🤝 It's a tie!")
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("🎉 You win!")
    else:
        print("💥 You lose!")

    running = play_again_prompt()
    print()

print("👋 Thank you for playing!")
