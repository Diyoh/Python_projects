from game_data import data
import random 
import art
from replit import clear

print(art.logo)
# create two accounts to compare
choice_A = random.choice(data)
# print(choice_A)
choice_B = random.choice(data)
# print(choice_B)
score = 0
if choice_A == choice_B:
  choice_B = random.choice(data)
# print(choice_B)
# print(choice_A['name'])
#print one account vs the other in the console
continue_game = True
while continue_game:
  print(f"Compare A: {choice_A['name']}, a {choice_A['description']}, from {choice_A['country']} ")
  print(art.vs)
  print(f"Compare B: {choice_B['name']}, a {choice_B['description']}, from {choice_B['country']} ")
  
  
  # ask the player to choose who is higher
  def winner():
    if choice_A['follower_count'] > choice_B['follower_count']:
      return 'a'
    else:
      return 'b'
  answer = input("Who has more followers? Type 'A' or 'B':").lower()
  
  #check if their answer
  if answer == winner():
     score += 1
     clear()
     print(art.logo)
     choice_A = choice_B
     choice_B = random.choice(data)
     print(F"You're right! Current score: {score}.")
  else:
    clear()
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}.")
    continue_game = False
  
 
