from turtle import *


def negyzet(meret,szin):
    color(szin)
    i=0
    while (i<4):
        forward(meret)
        right(90)
        i=i+1

def haromszog(meret,szin2):
    color(szin2)
    z=0
    while(z==0):
        forward(meret)
        right(120)
        forward(meret)
        right(120)
        forward(meret)
        right(120)
        z=z+1

def csillag(meret,szin):
    color(szin)
    g=0
    while(g<3):
        forward(meret)
        right(145)
        g=g+1
    forward(meret)
    right(142)
    forward(meret)
    right(142)


















