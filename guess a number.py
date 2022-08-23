from art import logo
import random
from replit import clear

BEGINNER = 10
AMATEUR = 8
PROFFESIONAL = 6
SUPERSTAR = 4
number_range = []
lives = 0
for i in range(1, 101):
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


def play_again():
    """restarts or ends the game"""
    continue_playing = input("type 'p' too continue playing or 'q' to quit: ").lower()
    if continue_playing == "p":
        clear()
        game(lives)
    else:
        clear()


def game(lives):
    print(logo)
    print("Welcome to my guess a number game")
    print("i am thinking of a number between 1-100")
    number = choose_number()
    chose_level = input(
        "choose a level of difficulty. Type: 'beginner', 'Amateur', 'professional', 'superstar'\n\n"
    ).lower()
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

    while lives > 0:
        print(f"you have {lives} attempts remaining to guess the number")
        guess = int(input("make a guess:"))
        if guess > number:
            lives -= 1
            print(
                f"Too high.\nGuess again.\nYou have {lives} attempts remaining to guess the number"
            )
        elif guess < number:
            lives -= 1
            print(
                f"Too low.\nGuess again.\nYou have {lives} attempts remaining to guess the number."
            )
        elif guess == number:
            print(f"Yes! you won.The correct number is {number}")
            play_again()
    play_again()

game(lives)










# new one 
from random import randint
from replit import clear
def game():
  answer = randint(1, 100)
  print(f"psst the answer is {answer}")
  print("welcome to my game of guess a number")
  print("I am thinking of a number between 1 - 100")
  def level():
    level = input("choose a level: type 'hard' or 'easy': ").lower()
    if level == "hard":
      return 5
    elif level == "easy":
      return 10
      
  def check():
    if guess > answer:
      return f"Too high\nGuess again: \nyou have {lives -1} attempts remaining to make a guess"
    elif guess < answer:
      return f"Too low\nGuess again: \nyou have {lives -1} attempts remaining to make a guess" 
    else:
      return "You win"
      
     
  lives= level()
  while lives > 0:
    guess = int(input("Guess a number: "))
    compare = check()
    if compare == "You win":
      print(f"{compare} the right number is {answer}")
      play_again = input("type 'p' to play again or 'q' to quit: ").lower()
      if play_again == "p":
        clear()
        game()
      else:  
        clear()
    else:    
      lives -= 1    
      print(compare)
    
  print("You lose but all hope os not lost")
  play_again = input("type 'p' to play again or 'q' to quit: ").lower()
  if play_again == "p":
    clear()
    game()
  else:  
    clear() 


game()
