from replit import clear
from art import logo
import random as r
def game():
  print(logo)
  dealer_cards = []
  user_cards = []
  sum_of_dealer_cards = 0
  sum_of_user_cards = 0
  
  
  def deal_card():
      """Returns a random card from the deck."""
      cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
      card = r.choice(cards)
      return card
  
  
  # distributing two cards each and displaying
  
  
  def calculate_score(cards):
      """takes the cards and add their value"""
      if 11 in cards and sum(cards) > 21:
          cards.remove(11)
          cards.append(1)
      return sum(cards)
  
  
  # def check_Ace()
  
  
  def compare_score(sum_of_dealer_cards, sum_of_user_cards):
      if sum_of_user_cards >= 21 and sum_of_dealer_cards == 21:
          return "Computer"
      elif sum_of_user_cards == 21:
          return "User"
  
  def play_again():
    play_again = input("type \"p\" to play again or \"q\" to quit \n").lower()
    if play_again == "p":
      clear()
      game()
    else:
      clear()
      print("Thank you for playing")
  
  

  
  
  user_cards.append(deal_card())
  user_cards.append(deal_card())
  sum_of_user_cards = calculate_score(user_cards)
  print(f"Your cards are {user_cards}")
  print(f"The sum of your card is {sum_of_user_cards}")
  dealer_cards.append(deal_card())
  print(f"the dealer's cards are {dealer_cards}")
  dealer_cards.append(deal_card())
  sum_of_dealer_cards = calculate_score(dealer_cards)
  
  compare_score(sum_of_dealer_cards, sum_of_user_cards)
  if compare_score(sum_of_dealer_cards, sum_of_user_cards) == "Computer":
    print(f"your score is {sum_of_user_cards}")
    print(f"Blackjack! Computer Score = {sum_of_dealer_cards}. You lose")
    play_again()
    
  
  elif compare_score(sum_of_dealer_cards, sum_of_user_cards) == "User":
    print(f"The dealer cards are {dealer_cards}")
    print(f"Computer score is {sum_of_dealer_cards}")
    print(f"Blackjack! Your Score = {sum_of_user_cards}. You Win")
    play_again() 
  else:
    user_deal = True
    dealer_deal = False
    while user_deal:
        deal_new_card = input(
            "type \"y\" to deal a new card or \"n\" to stop and calculate ").lower()
        if deal_new_card == "y":
            user_cards.append(deal_card())
            print(f"Your cards are {user_cards}")
            sum_of_user_cards = calculate_score(user_cards)
            print(f"Your score is {sum_of_user_cards}")
            if sum_of_user_cards > 21:
              user_deal = False
        elif deal_new_card == "n":
            user_deal = False
            dealer_deal = True
        else:
          print("invalid input")

    if sum_of_user_cards > 21:
      print(F"The delear's cards are {dealer_cards}")
      print(f"The dealer's score is {sum_of_dealer_cards}")
      print(f"You Lose!") 
      play_again()
      
    
    while dealer_deal and sum_of_dealer_cards < 16:
       print(f"The dealer's cards are {dealer_cards}")
       print(f"The dealer's score is {sum_of_dealer_cards}")
       dealer_cards.append(deal_card())
       sum_of_dealer_cards = calculate_score(dealer_cards)
       print(F"The delear's cards are {dealer_cards}")
       print(f"The dealer's score is {sum_of_dealer_cards}")
       if sum_of_dealer_cards >= 21:
          dealer_deal = False
  
    if sum_of_dealer_cards > 21:
      print(f"Your cards are {user_cards}")
      print(f"Your score is {sum_of_user_cards}")
      print(F"The delear's cards are {dealer_cards}")
      print(f"The dealer's score is {sum_of_dealer_cards}")
      print(f"You Win!")
      play_again()
    
    elif sum_of_user_cards > sum_of_dealer_cards:
      print(f"Your cards are {user_cards}")
      print(f"Your score is {sum_of_user_cards}")
      print(F"The delear's cards are {dealer_cards}")
      print(f"The dealer's score is {sum_of_dealer_cards}")
      print(f"You Win!")
      play_again()
    
    elif sum_of_user_cards == sum_of_dealer_cards:
      print(f" Your cards are {user_cards}")
      print(f"Your score is {sum_of_user_cards}")
      print(F"The delear's cards are {dealer_cards}")
      print(f"The dealer's score is {sum_of_dealer_cards}")
      print(f"Draw try again!")
      play_again()
      
    else:
      print(f" Your cards are {user_cards}")
      print(f"Your score is {sum_of_user_cards}")
      print(F"The delear's cards are {dealer_cards}")
      print(f"The dealer's score is {sum_of_dealer_cards}")
      print(f"You Lose!")
      play_again()
    
  
game()
