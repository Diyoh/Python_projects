#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 nulmber = JduE&!91
import random
choice_l = []
for n in range(0, (nr_letters)):
    choose_l = random.choice(letters)
    choice_l.append(choose_l)
choice_s = []
for n in range(0, nr_symbols):
  choose_s = random.choice(symbols)
  choice_s.append(choose_s)
choice_n = []
for n in range(0, nr_numbers):
  chose_n = random.choice(numbers)
  choice_s.append(chose_n)
pass_n = []
pass_n.extend(choice_n)
pass_n.extend(choice_l)
pass_n.extend(choice_s)
random.shuffle(pass_n)
# or say
password=""
for char in pass_n:
  password += str(char)
print(password)  
print(*pass_n)

  


   


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
