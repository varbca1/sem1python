
""" length= 10
breadth= 20
print(length) 
print(breadth)
Average = (length + breadth)/2
print(Average)

stationery = ['paper','Gel Pen', 'Eraser']
print(stationery)
print(type(stationery))

first = 'Mohandas'
second = 'karamchand'
third = 'Gandi'
Fullname = first + ' ' + second + ' ' + third
print(Fullname)

sum = 20 - 10 < 12
print(sum)

num1 = 1
num2 = 10 
n1 = num1 < 6.75 < num2 
print(n1)

num3 = 20
num3 < 24
print(num3)

r4 = (first > second) and (second < third)
print(r4)

n2 = 0 == (1 == 2)
print(n2)

n3 = (2 + 3 == 4 + 5) == 7
print(n3)

n4 = (1 < -1) == (3 > 4)
print(n4) 

num1 = 4
num2 = num1 + 1
print(num1,num2)



# a, b = 2,3 
# c, b = a, c + 1
# print(a,b,c)  

num1 = 4
num2 = 3
num3 = 2

num1 += num2 + num3
print(num1)

num1 = num1 ** (num2 + num3) 
print(num1)

num1 = '5' + '5'
print(num1)

num1 = 24 // 4 // 2
print(num1)

num1 = float(10)
print(num1)

num1 = int(3.14)
print(num1)

print('Bye' == 'BYE')

print((10 != 9) and (20 >= 20))

print(10 + 6 * 2 ** 2 != 9// 4-3 and 29 >= 29/9)

print(5 % 10 + 10 < 50 and 29 <= 29)

print(0 < 6) or (not(10 == 6) and (10 < 0)) 

#25/0

#num1 = 25; num2 = 0; num1/num2

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
print((x <= 10) and (y <= 10))

c = float(input("Enter the value in celsius: "))
f = c ** 9/5 + 3

age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")    

num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: "))

if num1 > num2:
   diff = num1 - num2
else:
   diff = num2 - num1
print("The difference of", num1, "and", num2 , "is" , diff)     
 """

number = int(input("Enter a number: ")) 
if number > 0:
     print("Number is Positive")
elif number < 0:
       print("Number is Negative")
else:
    print("Number is Zero")             