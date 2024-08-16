a=int(input("Kérek egy számot: "))
b=int(input("Kérek még 1 számot: "))
n=1
vege=0
szoveg=("A 3 es az 5 tobbszoroseinek az összege: " + str(a) +  " és a(z) " + str(b) + " korlatjan belul: ")

while(n<=a or n<=b):
    if(a<=n):
        while(n%3==0 and n%5==0 and n<=b):
            vege=vege+n
            n=n+1
        if(b==n):
            print(str(szoveg) + str(vege))
        n=n+1

    elif(b<=n):
        while(n%3==0 and n%5==0 and n<=a):
            vege=vege+n
            n=n+1
        if(n==a):
            print(str(szoveg) + str(vege) )

    else:
        n=n+1

























