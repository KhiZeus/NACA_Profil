""" Le présent programme permet de tracé une représentation d'un profilNACA symétrique et
    de donner son épaisseure maximum et la position du maximum """
import numpy as np
import matplotlib.pyplot as plt

# récupération des informations sur le profil NACAXX

valeur_fournie_epaisseur= int(input("Donnez le numero (xx) de votre profil NACA symmetrique NACA00XX : "))
corde = float(input("Quelle est la corde en mètre de votre profil NACA :"))
distribution = input("Quelle distribution de point souhaitez vous avoir : lineaire (l) ou non-lineaire (n)")
nombre_points = int(input("Combien de point voulez vous le long de la corde :"))

#epaisseur de profil t

t = valeur_fournie_epaisseur / 100

#Maillage de la corde
xc = np.linspace(0, 1, num=nombre_points)

# Extrados adimensionné
yt = 5*t*(0.2969*xc**0.5-.1260*xc-.3516*xc**2+.2843*xc**3-.1036*xc**4)

# extrados intrados réels
yup = yt*corde
ydown = -yt*corde
x_reel= corde*xc
Maximum =(0.5, 0.05)
Graph_naca = plt.figure(figsize=(8, 5))
plt.plot(x_reel, yup, 'g--', label='Extrados')
plt.plot(x_reel, ydown, 'r--', label='Intrados')
#plt.text(0.5, 0.05, 'Point de fonctionnement')
plt.xlabel('position de corde (m)')
plt.ylabel('épaisseur (m)')
plt.title('Représentation graphique du profil NACA 00' + str(valeur_fournie_epaisseur))
plt.legend()
plt.annotate('Maximum', xy=Maximum,xytext=(0.5,0.0),arrowprops=dict(facecolor='blue',arrowstyle='<-'))
plt.show()
