print("Welcome to the tip calculator!")
total_bill = float(input("what was the total bill?  $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("how many people to split the bill? "))
final_bill = round((total_bill/people)*(1+(tip/100)), 2)
bill_per_person = round(final_bill, 2)
#or use this format to round ot 2 decimal places
#bill_per_person = "{:.2f}".format(final_bill)
print(f"Each person should pay: ${bill_per_person}")
