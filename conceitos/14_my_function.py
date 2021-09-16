myVariable = 5
def myFunc(a):
    myVariable = 1
    return a ** 2
res = myFunc(4)

print(myVariable)
print(res)