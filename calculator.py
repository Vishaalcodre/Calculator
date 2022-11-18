from art import logo
def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2

def calculator():
  print(logo)

  operations = {'+':add,'-':sub,'*':mul,'/':div}

  n1 = float(input("Enter your first number: "))

  for symbol in operations:
    print(symbol)

  should_continue = True

  while should_continue:
    operation_symbol = input("Select what kind of operation would you like to perform: ")

    n2 = int(input("Enter the next number: "))

    operation = operations[operation_symbol]

    answer = operation(n1,n2)
    print(f"{n1} {operation_symbol} {n2} = {answer}")

    if input(f"Type 'y' if u want to continue with {answer} or type 'n' to start new calculation ") == 'y':
      n1 = answer

    else:
      should_continue = False
      calculator()
calculator()
