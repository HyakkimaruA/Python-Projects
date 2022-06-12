from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
bidders = {}

highest_bidder = ""
highest = 0
people = True

while people:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bidders[name] = bid
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  clear()
  if other_bidders == "no":
    people = False
    for key in bidders:
      for key2 in bidders:
        if bidders[key2] > bidders[key]:
          highest = bidders[key2]
          highest_bidder += key2
    print(f"The winner is {key2} with a bid of ${highest}.")
    
