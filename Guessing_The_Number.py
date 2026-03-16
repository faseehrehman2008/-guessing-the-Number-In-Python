import random

def guessing_the_number():
    print("Welcome to Guessing the Number!")
    print("I have selected a number between 1 and 100. Can you guess it?")

secret_number= random.randint (1, 100)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number")

    remmaining_attempts = max_attempts - attempts
    
    if remmaining_attempts > 0:
        print(f"You have {remmaining_attempts} attempts left behind.")
    else:
        print("No more attempts left.")
        attempts -= 1  # Don't count invalid attempts
        break
#game Over
print(f"Game Over! The secret number was {secret_number}.")