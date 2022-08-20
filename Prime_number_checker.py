
def prime_checker(number):
  if number > 1:
    is_prime = True
    for i in range(2, number):
      if number % i == 0:
        is_prime = False
    if is_prime:
      print("Numbe is prime")
    else:
      print("Number is not prime")
  else:
    print("enter a number greater than 1")





n = int(input("Check this number: "))
prime_checker(number=n)



