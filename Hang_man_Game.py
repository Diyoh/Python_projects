#Step 3
def Convert(string):
    chose_word=[]
    chose_word[:0]=string
    return chose_word

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(Convert(chosen_word))
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
word_string = Convert(chosen_word)

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while word_string != display:
  guess = input("Guess a letter: ").lower()
  
  #Check guessed letter
  for position in range(word_length):
    if chosen_word[position] == guess:
      display[position] = letter
  
  print(display)
print("You Win!")



#final code


import random
import hangman_words
from hangman_words import word_list
import hangman_art
from hangman_art import stages
from hangman_art import logo


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position] 
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
      
    print(stages[lives])



#OR




import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
  display += "_"

end_of_game = False
while not end_of_game:
  guess = input("Guess a letter: ").lower()
  for index in range(len(chosen_word)):
      if chosen_word[index] == guess:
          display[index] = guess
  print(display)
  if "_" not in display:
    end_of_game = True
print("You Win")

