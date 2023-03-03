from calcart import logo
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

#dictionary to store functions
dict1 = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
  print(logo)
  one_moreask = "y"
  num1 = int(input("Enter the first number:"))
  for i in dict1:
      print(i)
  while one_moreask == "y":
      opr_symb = input("Pick an operation: ")
      num2 = int(input("Enter the second number:"))
      opr_func = dict1[opr_symb]
      answer = opr_func(num1, num2)
      print(answer)
      one_moreask = input(
          f"type 'y' to continue calculating with {answer}, or type 'n' to exit: "
      )
      num1 = answer
  else:
      one_moreask == "n"
      calculator()
calculator()
