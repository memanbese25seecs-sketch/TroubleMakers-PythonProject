import random

def play_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 50.")

    while True:
        secret_number = random.randint(1, 50)
        attempts = 0

        while True:
            try:
                guess = int(input("Enter your guess (1–50): "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            attempts += 1

            if guess < 1 or guess > 50:
                print("Your guess is out of range! Please guess between 1 and 50.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! The number was {secret_number}.")
                print(f"You guessed it in {attempts} attempts.")
                break

        # ask if player wants to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing! Goodbye.")
            break

# run the game if file is executed directly
if __name__ == "__main__":
    play_guessing_game()
