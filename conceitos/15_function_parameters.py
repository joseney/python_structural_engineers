def my_Func(radius, perimeter = False):
    if perimeter == False:
        return 3.14*radius**2
    else:
        return (3.14*radius**2, 2*3*radius)
print(my_Func(4))
print(my_Func(4, perimeter=True))