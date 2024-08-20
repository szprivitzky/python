x1=input(str("Kérek egy számot:"))
x2=input(str("Kérek egy számot:"))
x3=input(str("Kérek egy számot:"))
lista=[x1,x2,x3]
def maximum(x1,x2,x3):
    n=0
    n=x1
    if (n<x2):
        n=x2
        if(n<x3):
            n=x3
    elif(n<x3):
        n=x3
    else:
        n=x1

    return n
print(maximum(x1,x2,x3))





























