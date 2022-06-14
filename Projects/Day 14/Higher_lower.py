import art
import game_data
import random
import os

DATA = game_data.data

def first_person():
  random_number = random.randint(0, len(DATA)-1)
  person = DATA[random_number]
  
  print(f"Compare A: {person['name']}, a {person['description']}, from {person['country']}.")

  return person['follower_count']
  
def second_person():
  random_number = random.randint(0, len(DATA)-1)
  
  person = DATA[random_number]
  
  print(f"Against B: {person['name']}, a {person['description']}, from {person['country']}.")

  return person['follower_count']

def checker(first_count, second_count):
  if first_count > second_count:
    return 'A'
  elif second_count > first_count:
    return 'B'
  


GAME = True
CORRECT = 0

print(art.logo)
FIRST_COUNT = first_person()

while GAME:
  if CORRECT > 0:
    os.system('clear')
    print(art.logo)
  
  if CORRECT > 0:
    print(f"You're right! Current score: {CORRECT}.")
    for i in DATA:
      if i['follower_count'] == FIRST_COUNT:
        print(f"Compare A: {i['name']}, a {i['description']}, from {i['country']}.")
  print(art.vs)
  second_count = second_person()

  
  random_number = random.randint(0, len(DATA)-1)
  person = DATA[random_number]

  correct_answer = checker(FIRST_COUNT, second_count)
  answer = input("Who has more followers? Type 'A' or 'B': ").upper()
  if answer != correct_answer:
    os.system('clear')
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {CORRECT}")
    GAME = False
  elif answer == 'A':
    GAME = True
    CORRECT += 1
  elif answer == 'B':
    GAME = True
    CORRECT += 1
    FIRST_COUNT = second_count
