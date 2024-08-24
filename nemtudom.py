
def karakterSzam(ca,ch):
    szamolo=int(0)
    a=len(ch)
    b=0
    while(b<=a-1):
        if(ch[int(b)]==ca):
            szamolo=szamolo+1

        b=b+1
    return print(str(szamolo) + " db " + str(ca) + " betu van a(z) " + str(ch) + " stringben " )


karakterSzam('a','alma')
