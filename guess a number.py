from art import logo
import random
from replit import clear
BEGINNER = 10
AMATEUR = 8
PROFFESIONAL = 6
SUPERSTAR = 4
number_range = []
lives = 0
for i in range(1,101):
  number_range.append(i)
print(number_range)
number = 0
def choose_number():
  """returns a random number"""
  number = random.choice(number_range)
  return number

# def choose_level():
#   """asigns the number of lives with respect to the level the player choses"""
#   chose_level = input("choose a level of your choice\n biginner \n Amateur\n professional,\n superstar").lower()
#   if chose_level == "biginner":
#     lives = BEGINNER
#   elif chose_level == "amateur":
#     lives = AMATEUR
#   elif chose_level == "professional":
#     lives = PROFFESIONAL
#   elif chose_level == "superstar":
#     lives = SUPERSTAR
#   return lives
  
 

  
def game():
  print(logo)
  print("Welcome to my guess a number game")
  print("i am thinking of a number between 1-100")
  number = choose_number()
  chose_level = input("choose a level of difficulty. Type: 'beginner', 'Amateur', 'professional', 'superstar'\n\n").lower()
  if chose_level == "beginner":
    lives = BEGINNER
  elif chose_level == "amateur":
    lives = AMATEUR
  elif chose_level == "professional":
    lives = PROFFESIONAL
  elif chose_level == "superstar":
    lives = SUPERSTAR
  else:
    print("howdy you missed something ")

  can_guess = True
  while can_guess:
    print(f"you have {lives} attempts remaining to guess the number")
    guess = int(input("make a guess:"))
    if guess > number:
      lives -= 1
      if lives == 0:
         can_guess = False
      print(f"Too high.\nGuess again.\nYou have {lives} attempts remaining to guess the number")
    elif guess < number:
       lives -=1
       if lives == 0:
         can_guess = False
       print(f"Too low.\nGuess again.\nYou have {lives} attempts remaining to guess the number.")
    elif guess == number:
       print(f"Yes! you won the correct number is {number}")
 
game()  
