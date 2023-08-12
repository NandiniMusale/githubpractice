#this is addition function
def addition(a,b,c):
    print(a+b+c)
    return a+b+c
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def sub(a,b):
    return a-b
def fact(a):
    f=1
    for i in range(1,a+1):
        f=f*i
    return f
def addandsubb(a,b):
    add=a+b
    sub=a-b
    return add,sub
