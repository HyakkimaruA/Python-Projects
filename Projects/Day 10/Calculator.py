#Calculator
from art import logo
from replit import clear
#Add
def add(n1, n2):
  return n1 + n2

#Substract
def substract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2


operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  going_through = True
  answer = 0
  for keys in operations:
    print(keys)
  
  while going_through:
    if answer != 0:
      num1 = answer
    operation_symbol = input("Pick an operation: ")
    
    num2 = float(input("What's the next number?: "))
    
    for keys in operations:
      if operation_symbol == keys:
        answer = operations[keys](num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    through = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
    if through == "n":
      going_through = False
      clear()
      calculator()


calculator()
