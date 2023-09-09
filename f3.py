def print_kwargs(**kwargs):
    for key, value in kwargs.items():
       print(f"{key} : {value}")

print_kwargs(name="Alice", age= 30) 

print_kwargs(city="New York", occupation="Engineer")

def mixed_args(a,b, **kwargs):
    print("First argument:  ", a   )
    print("Second argument: ", b   )
    print("Third argument:  ", kwargs)

mixed_args(1,2)
mixed_args(1,2, city= "New York")
mixed_args(1,2,occupation= "Engineer") 