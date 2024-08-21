from negyzet import*

up()
goto(-300,50)
down()
meret=50
szin='red'
szin2='blue'



n=0
while(n<5):
    down()
    negyzet(meret,szin)
    up()
    forward(60)
    down()
    haromszog(meret,szin2)
    up()
    forward(60)
    n=n+1
    meret=meret-10