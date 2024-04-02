#calculator
# input a number
# pick an operator
# input another number
# get the result
#would you like to continue ("yes" or "no")? 

def add(n1, n2):
  return n1+ n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

#calling the function
function = operations["*"]
#using the function
print(function(2,3))