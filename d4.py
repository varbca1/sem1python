def my_function(mylist):
    mylist.append(999)
    for i in mylist:
        print(i)
    print(mylist)

L = [1,2,3,4,5,6,7,8]
my_function(L) 