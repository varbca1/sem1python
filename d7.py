def my_function(mylist):
    my_function[4] = 999
    for i in mylist:
        print(i)
    
i = 1
L = []
n = int(input("Enter no. of elements  "))
while i <= n:
    L.append (int(input(f'Enter {i} no->')))
    i += 1
my_function(L)