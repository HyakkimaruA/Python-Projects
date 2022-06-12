import logo
import random

print(logo.guess)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

DIFFICULTY = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if DIFFICULTY == 'easy':
  ITERATION = 10
elif DIFFICULTY == 'hard':
  ITERATION = 5

RANDOM_NUMBER = random.randint(1, 100)

EASY = 10
HARD = 5

def guessing_number():
  global EASY, HARD
  for i in range(ITERATION + 1):
    if DIFFICULTY == 'easy' and EASY != 0:
      print(f"You have {EASY} attempts remaining to guess the number")
      EASY -= 1
      guess = int(input("Make a guess: "))
      guessed = checking_correct_number(guess)
    elif DIFFICULTY == 'hard' and HARD != 0:
      print(f"You have {HARD} attempts remaining to guess the number.")
      HARD -= 1
      guess = int(input("Make a guess: "))
      guessed = checking_correct_number(guess)
    if guessed == False and ITERATION == 0:
      return
    elif guessed == True:
      return

def checking_correct_number(guess):
  if EASY == 0 or HARD == 0:
    print(f"You've run out of guesses, you lose.")
    return False
  elif guess > RANDOM_NUMBER:
    print("Too high.\nGuess again.")
    return False
  elif guess < RANDOM_NUMBER:
    print("Too low.\nGuess again.")
    return False
  elif guess == RANDOM_NUMBER:
    print(f"You got it! The answer was {guess}.")
    return True

guessing_number()
