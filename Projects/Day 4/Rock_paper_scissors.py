import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choosing = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

options = ["rock", "paper", "scissors"]

if options[choosing] == "rock":
  print(rock)
elif options[choosing] == "paper":
  print(paper)
elif options[choosing] == "scissors":
  print(scissors)

print("Computer chose:")

random_number = random.randint(0, len(options)-1)

if options[random_number] == "rock":
  print(rock)
elif options[random_number] == "paper":
  print(paper)
elif options[random_number] == "scissors":
  print(scissors)

if options[random_number] == options[choosing]:
  print("It's a draw.")
elif options[choosing] == "rock" and options[random_number] == "paper":
  print("You lose.")
elif options[choosing] == "paper" and options[random_number] == "scissors":
  print("You lose.")
elif options[choosing] == "paper" and options[random_number] == "rock":
  print("You win.")
elif options[choosing] == "rock" and options[random_number] == "scissors":
  print("You win.")
elif options[choosing] == "scissors" and options[random_number] == "rock":
  print("You lose.")
elif options[choosing] == "scissors" and options[random_number] == "paper":
  print("You win.")
