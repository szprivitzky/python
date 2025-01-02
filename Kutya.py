from random import*
import random
import keyboard

class Kutyak():
    def __init__(self,nev,nem,eletkor):
        self.nev = nev
        self.nem = nem
        self.eletkor = eletkor

while True:
        nev = input("Kérek egy nevet:")
        if (nev == 'vege'):
            break
        nem = random.randint(1 , 2)
        if(nem == 1):
            nem='Fiú'
        elif(nem == 2):
            nem = 'Lány'
        eletkor = random.randint(1, 20)
        Kutya=Kutyak(nev,nem,eletkor)
        print(Kutya.nev,Kutya.eletkor,Kutya.nem)
        print(Kutya)












