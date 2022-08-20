from replit import clear
from art import logo
print(logo)
def compare_bids(bids_record):
  winner = ""
  greatest_bid = 0
  for bid in bids_record:
    if bids_record[bid] > greatest_bid:
      greatest_bid = bids_record[bid]
      winner = bid
    else:
      pass
      
  print(f"The greatest bidder is {winner} and his bid is {greatest_bid}")  


  


  
continue_bids = True
bids ={}
while continue_bids:
  name = input("What is your name?: ")
  price = int(input("What is your bid price? $"))
  bids[name] = price
  bid_again = input("are there any other bidders? Yes or No? \n").lower()
  if bid_again == "no":
    continue_bids = False
    clear()
    compare_bids(bids)
  else:
    clear()
    
print (bids)




