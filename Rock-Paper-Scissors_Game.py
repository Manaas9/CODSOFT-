import random

def get_computer_choice():
    """
    Randomly select rock, paper, or scissors for the computer.

    Returns:
        str: The computer's choice (rock, paper, or scissors).
    """
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner based on user and computer choices.

    Parameters:
        user_choice (str): The user's choice (rock, paper, or scissors).
        computer_choice (str): The computer's choice (rock, paper, or scissors).

    Returns:
        str: The result ("win", "lose", or "tie").
    """
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "win"
    else:
        return "lose"

def play_game():
    """
    Main function to play the Rock-Paper-Scissors game.
    """
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors Game!")
    print("Instructions: Enter 'rock', 'paper', or 'scissors' to play. Enter 'quit' to exit the game.")

    while True:
        # Get user input
        user_choice = input("\nYour choice (rock/paper/scissors): ").lower()

        if user_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        # Get computer's choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)

        if result == "win":
            print("You win!")
            user_score += 1
        elif result == "lose":
            print("You lose!")
            computer_score += 1
        else:
            print("It's a tie!")

        # Display scores
        print(f"\nCurrent Scores:")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")

if __name__ == "__main__":
    play_game()
