#Logo


#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Devided
def devided(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": devided,
}

n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))
operation_symbol= input(f"Choose operation '+' '-' '*' '/': ")

answer = operations[operation_symbol]
print(answer)


