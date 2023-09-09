""" number = int(input("Enter a number: ")) 
if number > 0:
     print("Number is Positive")
elif number < 0:
       print("Number is Negative")
else:
    print("Number is Zero")


signal = input("Enter the colour: ")
if signal == "red" or signal == "RED":
      print("STOP")
elif signal == "Orange" or signal == "ORANGE":
       print("Be Slow")
elif signal == "green" or signal == "GREEN":           
       print("Gol") 

"""

result = 0
val1 = float(input("Enter value 1: "))
val2 = float(input("Enter value 2: "))

op = input("Enter any one of the operator(+,-,*,/): ")
if op == "+":
    result = val1 + val2
elif op == "-":
    if val1 > val2:
        result = val1 - val2
    else:
        result = val2 - val1 
elif op == "*":
    result = val1 * val2 
elif op == "/":
    if val2 == 0:
        print("Error! Division by zero not allowed.Program terminated")
    else:
        result = val1/val2 
else:
    print("Wrong input, program terminated")
print("The result is ", result)                           