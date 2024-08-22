from negyzet import *

up()
goto(-300,50)
meret=30
szin='blue'
b=0
tavolsag=40
while(b<=8):
    down()
    csillag(meret,szin)
    up()
    forward(tavolsag)
    b=b+1
    if(5<=b):
        meret=meret-10
        tavolsag=tavolsag-10
    elif(b<=4):
        meret=meret+10
        tavolsag=tavolsag+10






