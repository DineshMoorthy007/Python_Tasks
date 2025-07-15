import random

def guess_number_game():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number within the range 1 to 100.")
            elif guess < number:
                print("Too low.")
            elif guess > number:
                print("Too high.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempt(s).")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

guess_number_game()