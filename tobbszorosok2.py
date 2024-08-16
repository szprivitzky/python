a=int(input("Kérek egy számot: "))
b=int(input("Kérek még 1 számot: "))
n=1
vege=0
szoveg=("A 3 es az 5 tobbszoroseinek az összege: " + str(a) +  " és a(z) " + str(b) + " korlatjan belul: ")

while(n<=a or n<=b):
    if(a<=n and n<=b):
        if(n%3==0 or n%5==0):
            vege=vege+n
        n=n+1
    elif(b<=n and n<=a):
        if(n%3==0 or n%5==0):
            vege=vege+n
        n=n+1

print(vege)























