import random

number = random.randint(0, 100)
guess = -1
attempts = 0

while guess != number:
    guess = int(input("Enter your guess (0-100): "))
    attempts += 1

    if guess > number:
        print("Lower number please.")
    elif guess < number:
        print("Higher number please.")

print(f"Correct! You guessed the number {number} in {attempts} attempts.")