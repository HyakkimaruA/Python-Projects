import os
import random
import art
############### Blackjack Project #####################
#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run
def taking_card():
  random_card = random.randint(0, (len(cards))-1)
  another_card = cards[random_card]
  return another_card

def first_two_cards_user():
  your_cards = []
  current_score = 0
  for i in range(2):
    random_card = taking_card()
    current_score += random_card
    your_cards.append(random_card)
  print(f"  Your cards: {your_cards}, current score: {current_score}")
  return your_cards

def first_card_computer():
  computer_cards = []
  computer_cards.append(taking_card())
  print(f"  Computer's first card: {computer_cards[0]}")
  return computer_cards

def taking_another_two_cards_computer():
  computer_cards = first_card_computer()
  for i in range(2):
    computer_cards.append(taking_card())
  return computer_cards

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if playing == 'y':
  os.system('clear')
  print(art.logo)


again = True

while again:
  your_cards = first_two_cards_user()
  computer_cards = first_card_computer()
  total = 0
  computer_total = 0
  another = input("Type 'y' to get another card, type 'n' to pass: ")
  if another == 'n':
    again = False
  elif another == 'y':
    computer_cards = taking_another_two_cards_computer()
    your_cards.append(taking_card())
    for i in your_cards:
      total += i
    for z in computer_cards:
      computer_total += z
    print(f"  Your final hand: {your_cards}, final score: {total}")
    print(f"  Computer's final hand: {computer_cards}, final score: {computer_total}")
    
    if total > 21:
      print("You went over. You lose \U0001F624")
    elif total <= 21:
      if total > computer_total:
        print("You win.")
  playing_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if playing_again == 'n':
    again = False
      
