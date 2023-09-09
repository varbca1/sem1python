def my_function(mylist):
    for i in mylist:
        print(i)
    
i = 1
L = []
n = int(input("Enter no. of elements  "))
while i <= n:
    value =  int(input(f'Enter {i} no->'))
    L.append(value)
    i += 1
my_function(L)