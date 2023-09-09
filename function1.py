def mixed_args(a,b, *args):
    print("First argument:  ", a   )
    print("Second argument: ", b   )
    print("Third argument:  ", args)

mixed_args(1,2)
mixed_args(2,3,4)
mixed_args(1,2,'a','b')
