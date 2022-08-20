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

import random
computer = [rock, paper, scissors]
computer_random = random.choice(computer)
user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user = int(user_input)
if user>=0 and user <=2:
  print(computer[user])
  if computer[user] == computer_random:
     print(f"the computer chose {computer_random}, and its a draw")
  elif user == 0 and computer_random == scissors or user == 2 and computer_random == paper or user == 1 and computer_random == rock: 
     print(f"the computer chose {computer_random}, and you win")
  elif computer_random > computer[user]:
     print(f"the computer chose {computer_random}, and you lose")
else:
  print("choice is invalid")
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.


