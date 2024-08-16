ev=int(input("Kerek egy ev szamot:"))

if(ev%4==0 and ev%100==0 and ev%400==0):
    print("szokoev")
elif(ev%4==0 and ev%100==0):
    print("simaev")
elif(ev%4==0):
    print("szokoev")
else:
    print("simaev")

























