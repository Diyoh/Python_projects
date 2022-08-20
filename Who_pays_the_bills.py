# Split string method
names_string = input("Give me everybody's names, separated by a comma and space. ")
names = names_string.split(", ")

import random
lenght = len(names)
number = random.randint(0, (lenght-1))
print(f"{names[number]} is going to buy the meal today!")


