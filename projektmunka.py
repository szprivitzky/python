import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
import random
with open("ara0033.csv" , "r") as f:
    tartalom=f.readlines()
    sor=3
évek=[]
beruhazas=[]
építés=[]
gép=[]
belföldi_gép=[]
importgép=[]
építés.append(100)
gép.append(100)
belföldi_gép.append(100)
importgép.append(100)


szo=[]
i=0
évek.append((tartalom[2].split())[0])
while(i<33):                            #évek
    szo=[]
    szo=tartalom[sor].split(";")
    évek.append(szo[0])
    sor=sor+1
    i=i+1
sor=3
i=0
beruhazas.append(100)                       #beruházás
while(i<33):
    szo=[]
    szo=(tartalom[sor].split(";", ))
    beruhazas.append(szo[1])
    sor=sor+1
    i=i+1

#xpoints = np.array(évek)                                #évek-beruházás diagramm
#ypoints = np.array(beruhazas)
#plt.plot(xpoints, ypoints)
#plt.title('évek-berhuházás', fontdict={'family':'serif','color':'blue','size':20})
#plt.show()
sor=3
i=0
while(i<33):
    szo=[]
    szo=(tartalom[sor].split(";", ))
    építés.append(szo[2])
    sor=sor+1
    i=i+1
sor=3
i=0
while(i<33):
    szo=[]
    szo=(tartalom[sor].split(";", ))
    gép.append(szo[3])
    sor=sor+1
    i=i+1
sor=3
i=0
while(i<33):
    szo=[]
    szo=(tartalom[sor].split(";", ))
    belföldi_gép.append(szo[4])
    sor=sor+1
    i=i+1
sor=3
i=0
while(i<33):
    szo=[]
    szo=(tartalom[sor].split(";", ))
    importgép.append(szo[5])
    sor=sor+1
    i=i+1

b=0
kész=[]
kész2=[]
kész3=[]
kész4=[]
kész5=[]
for i in range(33):
    szo2=""
    szo2=str(évek[i]) + str(":") + str(beruhazas[b])

    kész.append(szo2)
    szo3 = ""
    szo3 = str(évek[i]) + str(":") + str(építés[b])
    kész2.append(szo3)
    szo4 = ""
    szo4 = str(évek[i]) + str(":") + str(gép[b])
    kész3.append(szo4)
    szo5 = ""
    szo5 = str(évek[i]) + str(":") + str(belföldi_gép[b])
    kész4.append(szo5)
    szo6 = ""
    szo6 = str(évek[i]) + str(":") + str(importgép[b])
    kész5.append(szo6)
    b=b+1

#print("évek-beruházás:" + str(kész))
#print("évek-építés:" + str(kész2))
#print("évek-gép:" + str(kész3))
#print("évek-belföldigép:" + str(kész4))
#print("évek-importgép:" + str(kész5))
c=0
l=0
with open("kész.txt" , "w") as kesz:
    for c in range(33):
        if(c!=0):
            kesz.write(str(kész[c] + "; " + "\n"))

        if(c==0):
            kesz.write("évek-beruházások: " + str(kész[c] + "; "))
    for l in range(33):
        if (l != 0):
            kesz.write(str(kész2[l] + "; " + "\n"))

        if (l == 0):
            kesz.write("évek-építés: " + str(kész2[l] + "; " + "\n"))
    for d in range(33):
        if (d != 0):
            kesz.write(str(kész3[d] + "; " + "\n"))

        if (d == 0):
            kesz.write("évek-gép: " + str(kész3[d] + "; "+ "\n"))
    for g in range(33):
        if (g != 0):
            kesz.write(str(kész4[g] + "; " + "\n"))

        if (g == 0):
            kesz.write("évek-belföldigép: " + str(kész4[g] + "; "+ "\n"))
    for z in range(33):
        if (z != 0):
            kesz.write(str(kész5[z] + "; " + "\n"))

        if (z == 0):
            kesz.write("évek-importgép: " + str(kész5[z] + "; "+ "\n"))






ypoints = np.array(évek)                                #évek-építés diagramm
xpoints = np.array(építés)
plt.subplot(4, 4, 1)
plt.plot(xpoints, ypoints,marker='o',
    markersize=2,
    markeredgecolor='black',
    markerfacecolor='red',)
plt.ylabel('évek')
plt.xlabel('építés')
plt.title('évek-építés',fontsize=10, fontdict={'family':'serif','color':'blue','size':20})
plt.xticks([])
plt.yticks([])

ypoints = np.array(évek)                                #évek-beruházás diagramm
xpoints = np.array(beruhazas)
plt.subplot(4, 4, 3)
plt.plot(xpoints, ypoints,marker='o',
    markersize=2,
    markeredgecolor='black',
    markerfacecolor='red',)
plt.ylabel('évek')
plt.xlabel('beruhazas')
plt.title('évek-berhuházás',fontsize=10, fontdict={'family':'serif','color':'blue','size':20})
plt.xticks([])
plt.yticks([])

ypoints = np.array(évek)                                #évek-gép diagramm
xpoints = np.array(gép)
plt.subplot(4, 4, 9)
plt.plot(xpoints, ypoints,marker='o',
    markersize=2,
    markeredgecolor='black',
    markerfacecolor='red',)
plt.ylabel('évek')
plt.xlabel('gép')
plt.title('évek-gép',fontsize=10, fontdict={'family':'serif','color':'blue','size':20})
plt.xticks([])
plt.yticks([])

ypoints = np.array(évek)                                #évek-belföldi-gép diagramm
xpoints = np.array(belföldi_gép)
plt.subplot(4, 4, 11)
plt.plot(xpoints, ypoints,marker='o',
    markersize=2,
    markeredgecolor='black',
    markerfacecolor='red',)
plt.ylabel('évek')
plt.xlabel('belföldigép')
plt.title('évek-belföldigép',fontsize=10, fontdict={'family':'serif','color':'blue','size':20})
plt.xticks([])
plt.yticks([])

ypoints = np.array(évek)                                #évek-építés diagramm
xpoints = np.array(importgép)
plt.subplot(4, 4, 6)
plt.plot(xpoints, ypoints,marker='o',
    markersize=2,
    markeredgecolor='black',
    markerfacecolor='red',)
plt.ylabel('évek')
plt.xlabel('importgép')
plt.title('évek-importgép',fontsize=10, fontdict={'family':'serif','color':'blue','size':20})
plt.xticks([])
plt.yticks([])

plt.show()






x= np.array(beruhazas, dtype='U4')  # <U4 típusú sztringek
y = np.array(évek, dtype='U4')
plt.subplot(4, 4, 1)
x = x.astype(float)
y = y.astype(float)

# Lineáris regresszió képlete:
# y = a * x + b, ahol a a meredekség, b pedig az y-tengely metszéspontja

# Kiszámítjuk a meredekséget (a) és az y-tengely metszéspontját (b)
n = len(beruhazas)
a = (n * np.sum(y * x) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - (np.sum(x))**2)
b = (np.sum(y) - a * np.sum(x)) / n



# Plotolás
plt.scatter(x, y, color='blue', label='Adatok')
# Adatok pontokban
plt.plot(x, a * x + b, color='red', label='Regression Line')  # Regressziós egyenes
plt.xlabel('Beruházás',fontsize=8)
plt.ylabel('Évek',fontsize=8)
plt.title('évek-beruházás',fontsize=10, fontdict={'family':'serif','color':'blue','size':20})
plt.legend(fontsize=6)
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)


x2= np.array(építés, dtype='U4')  # <U4 típusú sztringek
y2 = np.array(évek, dtype='U4')
plt.subplot(4, 4, 3)
x2 = x2.astype(float)
y2 = y2.astype(float)

# Lineáris regresszió képlete:
# y = a * x + b, ahol a a meredekség, b pedig az y-tengely metszéspontja

# Kiszámítjuk a meredekséget (a) és az y-tengely metszéspontját (b)
n2 = len(x2)
a2 = (n2 * np.sum(y2 * x2) - np.sum(x2) * np.sum(y2)) / (n2 * np.sum(x2**2) - (np.sum(x2))**2)
b2 = (np.sum(y2) - a2 * np.sum(x2)) / n2



# Plotolás
plt.scatter(x2, y2, color='blue', label='Adatok')
# Adatok pontokban
plt.plot(x2, a2 * x2 + b2, color='red', label='Regression Line')  # Regressziós egyenes
plt.xlabel('Építés',fontsize=8)
plt.ylabel('Évek',fontsize=8)
plt.title('évek-építés',fontsize=10, fontdict={'family':'serif','color':'blue','size':20})
plt.legend(fontsize=6)
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)

x3= np.array(gép, dtype='U4')  # <U4 típusú sztringek
y3 = np.array(évek, dtype='U4')
plt.subplot(4, 4, 9)
x3 = x3.astype(float)
y3 = y3.astype(float)

# Lineáris regresszió képlete:
# y = a * x + b, ahol a a meredekség, b pedig az y-tengely metszéspontja

# Kiszámítjuk a meredekséget (a) és az y-tengely metszéspontját (b)
n3 = len(x3)
a3 = (n3 * np.sum(y3 * x3) - np.sum(x3) * np.sum(y3)) / (n3 * np.sum(x3**2) - (np.sum(x3))**2)
b3 = (np.sum(y3) - a3 * np.sum(x3)) / n3



# Plotolás
plt.scatter(x3, y3, color='blue', label='Adatok')
# Adatok pontokban
plt.plot(x3, a3 * x3 + b3, color='red', label='Regression Line')  # Regressziós egyenes
plt.xlabel('Gép',fontsize=8)
plt.ylabel('Évek',fontsize=8)
plt.title('évek-gép',fontsize=10, fontdict={'family':'serif','color':'blue','size':20})
plt.legend(fontsize=6)
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)

x4= np.array(belföldi_gép, dtype='U4')  # <U4 típusú sztringek
y4 = np.array(évek, dtype='U4')
plt.subplot(4, 4, 11)
x4 = x4.astype(float)
y4 = y4.astype(float)

# Lineáris regresszió képlete:
# y = a * x + b, ahol a a meredekség, b pedig az y-tengely metszéspontja

# Kiszámítjuk a meredekséget (a) és az y-tengely metszéspontját (b)
n4 = len(x4)
a4 = (n4 * np.sum(y4 * x4) - np.sum(x4) * np.sum(y4)) / (n4 * np.sum(x4**2) - (np.sum(x4))**2)
b4 = (np.sum(y4) - a4 * np.sum(x4)) / n4



# Plotolás
plt.scatter(x4, y4, color='blue', label='Adatok')
# Adatok pontokban
plt.plot(x4, a4 * x4 + b4, color='red', label='Regression Line')  # Regressziós egyenes
plt.xlabel('belföldigépek',fontsize=8)
plt.ylabel('Évek',fontsize=8)
plt.title('évek-belföldigépek',fontsize=10, fontdict={'family':'serif','color':'blue','size':20})
plt.legend(fontsize=6)
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)

x5= np.array(importgép, dtype='U4')  # <U4 típusú sztringek
y5 = np.array(évek, dtype='U4')
plt.subplot(4, 4, 6)
x5 = x5.astype(float)
y5 = y5.astype(float)

# Lineáris regresszió képlete:
# y = a * x + b, ahol a a meredekség, b pedig az y-tengely metszéspontja

# Kiszámítjuk a meredekséget (a) és az y-tengely metszéspontját (b)
n5 = len(x5)
a5 = (n5 * np.sum(y5 * x5) - np.sum(x5) * np.sum(y5)) / (n5 * np.sum(x5**2) - (np.sum(x5))**2)
b5 = (np.sum(y5) - a5 * np.sum(x5)) / n5



# Plotolás
plt.scatter(x5, y5, color='blue', label='Adatok')
# Adatok pontokban
plt.plot(x5, a5 * x5 + b5, color='red', label='Regression Line')  # Regressziós egyenes
plt.xlabel('importgépek',fontsize=8)
plt.ylabel('Évek',fontsize=8)
plt.title('évek-importgép',fontsize=10, fontdict={'family':'serif','color':'blue','size':20})
plt.legend(fontsize=6)
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)


plt.show()








