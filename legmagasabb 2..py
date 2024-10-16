
ADATOK=[560,780,96,344,566,770]
N=len(ADATOK)
max2=0
tesztelo=1
szamolo=0
g=max(ADATOK)
while(szamolo<N-1):
    if(ADATOK[szamolo]<ADATOK[tesztelo] and g!=ADATOK[tesztelo]):
        max2=ADATOK[tesztelo]
        szamolo=szamolo+1
        tesztelo=tesztelo+1

    elif(ADATOK[szamolo]>ADATOK[tesztelo]):
        szamolo=szamolo+1
        tesztelo=tesztelo+1
        max2=ADATOK[szamolo]

    elif(g==ADATOK[tesztelo]):
        szamolo=szamolo+2
        tesztelo=tesztelo+2



print(max2)





