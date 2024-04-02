#calculator
# input a number
# pick an operator
# input another number
# get the result
# would you like to continue ("yes" or "no")? 
#### 'yes' another operation, 'no' new calculation

#operation functions
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

#dictionary of operations
operations = {
  "+": add, 
  "-": subtract, 
  "*": multiply, 
  "/": divide
}

#calculator fuction call itself to restart the calculator
def calculator():
  num1 = int(input("What's the number?: "))
  
  for symbol in operations:
    print(symbol)
  
  should_continue = True
  
  while should_continue:
    
    operation_symbol = input("Pick an operation: ")
    
    num2 = int(input("What's the next number?: "))
    
    #calling and using the function from dictionary
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    continue_calculation = input("type 'y' to continue or type 'n' to start a new calculation")
    if continue_calculation == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()