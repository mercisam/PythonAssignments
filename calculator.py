# input the first number
num1=float(input("Enter the first number: "))

#input the second number
num2=float(input("Enter the second number: "))

#input mathematical operation
operation=input("Enter an operator (+, -, *, /): ")
 
#perform operation based on the users input

if operation == "+":
 result = num1 + num2
 print(f"{num1} + {num2} = {result}")  

elif operation == "*":
 result = num1 * num2
 print(f"{num1}* {num2} = {result}")

elif operation == "-":
 result = num1 - num2  
 print(f"{num1} - {num2}= {result}")

elif operation == "/":
 if num2 != 0:
  result = num1 / num2
  print(f"{num1} / {num2}= {result}")
 else:
  print("Error: Cannot divide by zero")

else:
 print("Invalid Operation. Please enter(+,-,/,*)")
 