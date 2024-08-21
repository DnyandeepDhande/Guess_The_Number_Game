import random
from Guess_The_Number_Art import Logo

print(Logo)
number = random.choice(range(1,101))
attempts = 0

def guess_checker(attempt):
    guess_correct = False
    while not guess_correct:
        user_guess = int(input("Make a Guess:"))
        if user_guess < number:
            print("Too Low")
            attempt-=1
            print(f"You {attempt} attempts remaining to guess the number ")
        elif user_guess > number :
            print("Too High")
            attempt -= 1
            print(f"You {attempt} attempts remaining to guess the number ")
        elif user_guess == number:
            print("You Guessed it Correct, You Won!")
            guess_correct = True

game_over = False
while not game_over:
    print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 to 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'").lower()
    print(number)
    if difficulty == "easy":
        print("You have 10 attempts remaining to guess the number")
        attempts = 10
        guess_checker(attempts)

    elif difficulty == "hard":
        print("You have 5 attempts remaining to guess the number")
        attempts = 5
        guess_checker(attempts)

    guess_again = input("Want to play again Y or N").lower()
    if guess_again == "n":
        game_over = True
        print("GoodBye")
        break
