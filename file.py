with open("playlist.csv","r") as f:
    tartalom=f.readlines()
nevek=[]
cimek=[]
mufajok=[]
szoveg=[]
n=0
ido=[]
szo=""
for i in range(0,len(tartalom)):
    n=0
    sor=tartalom[i]
    while(str(sor[n])!=str(";")):
        szo+=str(sor[n])
        n=n+1
    if(sor[n]==";"):
        nevek.append(szo)
        szo=""
        n=n+1
        while (str(sor[n]) != str(";")):
            szo += str(sor[n])
            n = n + 1
        if (sor[n] == ";"):
            cimek.append(szo)
            szo = ""
            n=n+1
            while (str(sor[n]) != str(";")):
                szo += str(sor[n])
                n = n + 1
            if (sor[n] == ";"):
                mufajok.append(szo)
                szo = ""
                n=n+1
                while (n<len(sor)):
                    szo += str(sor[n])
                    n = n + 1
                    if(n==len(sor)):
                        szo=szo.rstrip()
                        ido.append(szo)
                        szo=""
kész=""
file=open("megoldas.txt" , "w")
for t in range(0,len(cimek)):
    a=("előadó:" + nevek[t] , "cim:" + cimek[t] , "műfaj:" + mufajok[t] , "hossza:" + ido[t])
    file.write(str(a) + "\n")













