import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
from ipywidgets import interact, widgets                    #importok,lehet van néhány fölösleges
import plotly.graph_objects as go
from scipy.interpolate import interp1d
from matplotlib.widgets import CheckButtons

with open("ara0033.csv" , "r") as f:
    tartalom=f.readlines()
    sor=37
évek=[]
beruhazas=[]
építés=[]
gép=[]
belföldi_gép=[]
importgép=[]                            #listák készítése
építés.append(100)
gép.append(100)
belföldi_gép.append(100)
importgép.append(100)
évek.append(1990)

szo=[]
i=0
while(i<33):
    szo=[]
    szo=tartalom[sor].split(";")
    évek.append(szo[0])
    sor=sor+1
    i=i+1
sor=37
i=0
beruhazas.append(100)
while(i<33):
    szo=[]
    szo=(tartalom[sor].split(";", ))
    beruhazas.append(szo[1])
    sor=sor+1
    i=i+1
                                                    #listákhoz rendelés

sor=37
i=0
while(i<33):
    szo=[]
    szo=(tartalom[sor].split(";", ))
    építés.append(szo[2])
    sor=sor+1
    i=i+1
sor=37
i=0
while(i<33):
    szo=[]
    szo=(tartalom[sor].split(";", ))
    gép.append(szo[3])
    sor=sor+1
    i=i+1
sor=37
i=0
while(i<33):
    szo=[]
    szo=(tartalom[sor].split(";", ))
    belföldi_gép.append(szo[4])
    sor=sor+1
    i=i+1
sor=37
i=0
while(i<33):
    szo=[]
    szo=(tartalom[sor].split(";", ))
    importgép.append(szo[5])
    sor=sor+1
    i=i+1


ypoints=np.linspace(100,130,34)
xpoints=np.linspace(1990,2023,34)
for i in range(34):
    ypoints[i]=beruhazas[i]


ypoints1=np.linspace(100,130,34)
xpoints1=np.linspace(1990,2023,34)
for i in range(34):
    ypoints1[i]=építés[i]

ypoints2=np.linspace(100,130,34)
xpoints2=np.linspace(1990,2023,34)              #grafikon pontjainak az elhelyezése
for i in range(34):
    ypoints2[i]=gép[i]

ypoints3=np.linspace(100,130,34)
xpoints3=np.linspace(1990,2023,34)
for i in range(34):
    ypoints3[i]=belföldi_gép[i]

ypoints4=np.linspace(100,130,34)
xpoints4=np.linspace(1990,2023,34)
for i in range(34):
    ypoints4[i]=importgép[i]




fig, ax = plt.subplots()
ax.set_xlim(1990,2023)
ax.set_ylim(100,130)
plt.grid()                                                            #grafikon készítése
plt.title("Grafikon",color="red",fontsize=20)
plt.ylabel('százalékok',fontsize=15,color="blue")
plt.xlabel('évek',fontsize=15,color='blue')





beru_hazas = ax.plot(xpoints, ypoints,marker='o',markersize=2,markeredgecolor='yellow',markerfacecolor='yellow',label='beruhazas', color='blue',linestyle='--')
épités = ax.plot(xpoints1, ypoints1,marker='o',markersize=2,markeredgecolor='black',markerfacecolor='black', label='építés', color='red',linestyle='--')
g_ép = ax.plot(xpoints2, ypoints2,marker='o',markersize=2,markeredgecolor='black',markerfacecolor='black', label='gép', color='yellow',linestyle='--')                      #függvények ábrázolása a grafikonban
belg_ép = ax.plot(xpoints3, ypoints3,marker='o',markersize=2,markeredgecolor='black',markerfacecolor='black', label='belföldigép', color='green',linestyle='--')
impg_ép = ax.plot(xpoints4, ypoints4,marker='o',markersize=2,markeredgecolor='black',markerfacecolor='black', label='importgép', color='purple',linestyle='--')
ax.legend()

ax_check = plt.axes([0.05, 0.7, 0.15, 0.2], facecolor='lightgoldenrodyellow')
check = CheckButtons(ax_check, ['beruhazas', 'építés', 'gép','belföldigép','importgép'], [True, True, True, True, True])                 #checkboxok létrehozása

def toggle_func(label):
    for i in range(1):
        if label == 'beruhazas':
            beru_hazas[i].set_visible(not beru_hazas[i].get_visible())
            fig.canvas.draw()
    for i in range(1):
        if label == 'építés':
            épités[i].set_visible(not épités[i].get_visible())                      #chechboxok beállítása
            fig.canvas.draw()
    for i in range(1):
        if label == 'gép':
            g_ép[i].set_visible(not g_ép[i].get_visible())
            fig.canvas.draw()
    for i in range(1):
        if label == 'belföldigép':
            belg_ép[i].set_visible(not belg_ép[i].get_visible())
            fig.canvas.draw()
    for i in range(1):
        if label == 'importgép':
            impg_ép[i].set_visible(not impg_ép[i].get_visible())
            fig.canvas.draw()




check.on_clicked(toggle_func)

plt.show()

fig, ax1 = plt.subplots()
ax1.set_xlim(1990,2023)
ax1.set_ylim(100,130)
plt.title("Regresszió-grafikon",color="red",fontsize=20)
plt.ylabel('százalékok',fontsize=15,color="blue")                                    #linárisregresszio grafikon létrehozása
plt.xlabel('évek',fontsize=15,color='blue')
plt.grid()

n = len(beruhazas)
a = (n * np.sum(ypoints * xpoints) - np.sum(xpoints) * np.sum(ypoints)) / (n * np.sum(xpoints**2) - (np.sum(xpoints))**2)
b = (np.sum(ypoints) - a * np.sum(xpoints)) / n



beruh_regeressz = ax1.plot(xpoints, a * xpoints + b, color='red', label='beruhazas'),ax1.scatter(xpoints, ypoints, color='blue', label='B_Adatok')

n2 = len(építés)
a2= (n2 * np.sum(ypoints1 * xpoints1) - np.sum(xpoints1) * np.sum(ypoints1)) / (n2 * np.sum(xpoints1**2) - (np.sum(xpoints1))**2)
b2 = (np.sum(ypoints1) - a2 * np.sum(xpoints1)) / n2



építés_regeressz = ax1.plot(xpoints1, a2 * xpoints1 + b2, color='red', label='Építés'),ax1.scatter(xpoints2, ypoints2, color='blue', label='É_Adatok')


n3 = len(gép)
a3= (n3 * np.sum(ypoints2 * xpoints2) - np.sum(xpoints2) * np.sum(ypoints2)) / (n3 * np.sum(xpoints2**2) - (np.sum(xpoints2))**2)
b3 = (np.sum(ypoints2) - a3 * np.sum(xpoints2)) / n3



gép_regeressz = ax1.plot(xpoints2, a3 * xpoints2 + b3, color='red', label='Gép'),ax1.scatter(xpoints2, ypoints2, color='blue', label='G_Adatok')                          #linárisregresszió pontjainak a beállítása


n4 = len(belföldi_gép)
a4= (n4 * np.sum(ypoints3 * xpoints3) - np.sum(xpoints3) * np.sum(ypoints3)) / (n4 * np.sum(xpoints3**2) - (np.sum(xpoints3))**2)
b4 = (np.sum(ypoints3) - a4 * np.sum(xpoints3)) / n4



belgép_regeressz = ax1.plot(xpoints3, a4 * xpoints3 + b4, color='red', label='Belföldigép'),ax1.scatter(xpoints2, ypoints2, color='blue', label='BelG_Adatok')

n5 = len(importgép)
a5= (n5 * np.sum(ypoints4 * xpoints4) - np.sum(xpoints4) * np.sum(ypoints4)) / (n5 * np.sum(xpoints4**2) - (np.sum(xpoints4))**2)
b5 = (np.sum(ypoints4) - a5 * np.sum(xpoints4)) / n5


impgép_regeressz = ax1.plot(xpoints4, a5 * xpoints4 + b5, color='red', label='Importgép'),ax1.scatter(xpoints2, ypoints2, color='blue', label='ImpG_Adatok')


ax1.legend()
ax1_check = plt.axes([0.05, 0.7, 0.15, 0.2], facecolor='lightgoldenrodyellow')
check = CheckButtons(ax1_check, ['beruhazas_regressz', 'építés_regressz', 'gép_regressz','belföldigép_regressz','importgép_regressz'], [True, True, True, True, True])                      #lináris regresszió checkboxok létrehozása

def toggle_func(label):
        if label == 'beruhazas_regressz':
            beruh_regeressz[1].set_visible(not beruh_regeressz[1].get_visible())
            fig.canvas.draw()
            (beruh_regeressz[0])[0].set_visible(not (beruh_regeressz[0])[0].get_visible())
            fig.canvas.draw()

        if label == 'építés_regressz':
            építés_regeressz[1].set_visible(not építés_regeressz[1].get_visible())                                  #lináris regresszió checkboxok beállítása
            fig.canvas.draw()
            (építés_regeressz[0])[0].set_visible(not (építés_regeressz[0])[0].get_visible())
            fig.canvas.draw()
        if label == 'gép_regressz':
            gép_regeressz[1].set_visible(not gép_regeressz[1].get_visible())
            fig.canvas.draw()
            (gép_regeressz[0])[0].set_visible(not (gép_regeressz[0])[0].get_visible())
            fig.canvas.draw()
        if label == 'belföldigép_regressz':
            belgép_regeressz[1].set_visible(not belgép_regeressz[1].get_visible())
            fig.canvas.draw()
            (belgép_regeressz[0])[0].set_visible(not (belgép_regeressz[0])[0].get_visible())
            fig.canvas.draw()
        if label == 'importgép_regressz':
            impgép_regeressz[1].set_visible(not impgép_regeressz[1].get_visible())
            fig.canvas.draw()
            (impgép_regeressz[0])[0].set_visible(not (impgép_regeressz[0])[0].get_visible())
            fig.canvas.draw()
check.on_clicked(toggle_func)
plt.show()

b=0
kész=[]
kész2=[]
kész3=[]                                        #változók a fájlba íráshoz
kész4=[]
kész5=[]
for i in range(34):
    szo2=""
    szo2=str(évek[i]) + str(";") + str(beruhazas[b])

    kész.append(szo2)
    szo3 = ""
    szo3 = str(évek[i]) + str(";") + str(építés[b])
    kész2.append(szo3)
    szo4 = ""                                                                   #sorok létrehozása és azt egy változóhoz rendelni
    szo4 = str(évek[i]) + str(";") + str(gép[b])
    kész3.append(szo4)
    szo5 = ""
    szo5 = str(évek[i]) + str(";") + str(belföldi_gép[b])
    kész4.append(szo5)
    szo6 = ""
    szo6 = str(évek[i]) + str(";") + str(importgép[b])
    szo6 = szo6.rstrip()
    kész5.append(szo6)
    b=b+1


c=0
l=0
with open("kész.csv" , "w") as kesz:
    for c in range(34):
        if(c!=0):
            kesz.write(str(kész[c] + "; " + "\n"))

        if(c==0):
            kesz.write("évek-beruházások: " + "\n" + str(kész[c] + "; " + "\n"))                        #végül a fájlba írás
    for l in range(34):
        if (l != 0):
            kesz.write(str(kész2[l] + "; " + "\n"))

        if (l == 0):
            kesz.write("évek-építés: " + "\n" + str(kész2[l] + "; " + "\n"))
    for d in range(34):
        if (d != 0):
            kesz.write(str(kész3[d] + "; " + "\n"))

        if (d == 0):
            kesz.write("évek-gép: " + "\n" + str(kész3[d] + "; "+ "\n"))
    for g in range(34):
        if (g != 0):
            kesz.write(str(kész4[g] + "; " + "\n"))

        if (g == 0):
            kesz.write("évek-belföldigép: " + "\n" +  str(kész4[g] + "; "+ "\n"))
    for z in range(34):
        if (z != 0):
            kesz.write("\n" + str(kész5[z] + "; " ))

        if (z == 0):
            kesz.write("évek-importgép: " +"\n" + str(kész5[z] + "; " ))








