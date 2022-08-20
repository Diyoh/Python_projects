def add(n1, n2):
  """returns the sum of two numbers"""
  return n1 + n2
def subtract(n1, n2):
  """return the difference between two numbers"""
  return n1 - n2

def divide(n1, n2):
  """divides n1 by n2"""
  return n1/n2

def multiply(n1, n2):
  """multiplies n1 by n2 and returns the result"""
  return n1*n2

operands = {
"+" : add,
"-": subtract, 
"/": divide,
"*" : multiply,
}

num1 = int(input("what is the first number?: "))
num2 = int(input("what is the second number?: "))

for operand in operands:
  print(operand)

operation = input("input the operation you want to carry out from the list above: ")

if operation in operands:
  result = operands[operation](num1, num2)

print(f"{num1} {operation} {num2} = {result}")


#or you can use this other code



def add(n1, n2):
  """returns the sum of two numbers"""
  return n1 + n2
def subtract(n1, n2):
  """return the difference between two numbers"""
  return n1 - n2

def divide(n1, n2):
  """divides n1 by n2"""
  return n1/n2

def multiply(n1, n2):
  """multiplies n1 by n2 and returns the result"""
  return n1*n2

operands = {
"+" : add,
"-": subtract, 
"/": divide,
"*" : multiply,
}

num1 = int(input("what is the first number?: "))
num2 = int(input("what is the second number?: "))

for operand in operands:
  print(operand)

operation = input("input the operation you want to carry out from the list above: ")
calculation = operands[operation]
result = calculation(num1, num2)
print(f"{num1} {operation} {num2} = {result}")


#update cod


#Calculator
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

num1 = int(input("What's the next number?: "))
for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation: ")
num2 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
previous_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {previous_answer}")

continue_calculating = (input(
    "Do you want to use the previous results for further calculatioins? type \"y\" pr \"n\" for No "
)).lower()

if continue_calculating == "y":
    solve_further = True
    while solve_further:
        operation_symbol = input("Pick an operation: ")

        calculation_function = operations[operation_symbol]
        num3 = int(input("What's the next number?: "))

        second_answer = calculation_function(previous_answer, num3)

        print(f"{previous_answer} {operation_symbol} {num3} = {second_answer}")
        previous_answer = second_answer

        continue_calculating = (input(
            "Do you want to use the previous results for further calculatioins? type \"y\" pr \"n\" for No "
        )).lower()

        if continue_calculating == "n":
            solve_further = False
            break



# another touches

#Calculator
from replit import clear()
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operation: ")
    num2 = int(input("What's the second number?: "))
    calculation_function = operations[operation_symbol]
    previous_answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {previous_answer}")

    continue_calculating = (input(
        "Do you want to use the previous results for further calculatioins? type \"y\" pr \"n\" for No "
    )).lower()

    if continue_calculating == "y":
        solve_further = True
        while solve_further:
            operation_symbol = input("Pick an operation: ")

            calculation_function = operations[operation_symbol]
            num3 = int(input("What's the next number?: "))

            second_answer = calculation_function(previous_answer, num3)

            print(
                f"{previous_answer} {operation_symbol} {num3} = {second_answer}"
            )
            previous_answer = second_answer

            continue_calculating = (input(
                "Do you want to use the previous results for further calculatioins? type \"y\" pr \"n\" for No "
            )).lower()

            if continue_calculating == "n":
                solve_further = False
                clear()
                calculator()
                break


calculator()





