""" def fun(a,b):
    return(a*b)  

p= 2
q= 3
result= fun(p,q)
print(result) """


def fun1(*args):
   mul= 1 
   for i in args:
       mul *= i 
   return mul

result= fun1(1,2,3,4,5,6) 
print(result)
result1= fun1(23,34,55,66,88,99,11,34,56,78,99)
print(result1)