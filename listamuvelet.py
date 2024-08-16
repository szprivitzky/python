from math import *

lista=[]
a=str(input("Kérek egy számot: "))
lista.append(a)
b=str(0)

while(a!=int and b<a):
    if (a == int):
        exit()
    a=str(input("Kérek egy számot: "))
    lista.append(a)
l=len(lista) - 1
lista.remove(lista[l])
print(lista)






















