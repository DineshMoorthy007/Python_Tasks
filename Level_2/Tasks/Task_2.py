import random

def number_guessing_game():
    try:
        start = int(input("Enter the starting number of the range: "))
        end = int(input("Enter the ending number of the range: "))
        
        if start >= end:
            print("Invalid range. Starting number must be less than ending number.")
            return

        secret = random.randint(start, end)
        attempts = 0

        while True:
            try:
                guess = int(input(f"Guess a number between {start} and {end}: "))
                attempts += 1

                if guess < start or guess > end:
                    print(f"Please enter a number within the range {start} to {end}.")
                elif guess < secret:
                    print("Too low.")
                elif guess > secret:
                    print("Too high.")
                else:
                    print(f"Correct! You guessed it in {attempts} attempt(s).")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    except ValueError:
        print("Invalid range input. Please enter valid integers.")

number_guessing_game()