""" Le présent programme permet de tracé une représentation d'un profilNACA symétrique et
    de donner son épaisseure maximum et la position du maximum """
import numpy as np
import matplotlib.pyplot as plt


def maximum_profil_naca00xx(epaisseur,corde,precision):
    """ cette fonction permet de retourner les coordonnées de l'épaisseur maximum de profil avec une précision donnée
    """
    xc = np.linspace(0, 1, num=1+round(corde/precision))
    yt = 5*epaisseur*(0.2969*xc**0.5-.1260*xc-.3516*xc**2+.2843*xc**3-.1036*xc**4)
    max_epaisseur = max(yt)
    max_position = np.argmax(yt)
    return (corde*xc[max_position],max_epaisseur*corde)


""" ----------------------------------------------------------------------------------------------------------
MAIN
-------------------------------------------------------------------------------------------------------------"""

# récupération des informations sur le profil NACAXX

valeur_fournie_epaisseur= int(input("Donnez le numero (xx) de votre profil NACA symmetrique NACA00XX : "))
corde = float(input("Quelle est la corde en mètre de votre profil NACA :"))
distribution = input("Quelle distribution de point souhaitez vous avoir : lineaire (l) ou non-lineaire (n)")
nombre_points = int(input("Combien de points voulez vous le long de la corde :"))
precision = 10**(-1-int(input("Quelle précision désirez vous pour l'épaisseur maximum :\n "
                      "\t\t\t\t1 : cm\n"
                      "\t\t\t\t2 : mm\n")))



#epaisseur de profil t

epaisseur = valeur_fournie_epaisseur / 100

#Maillage de la corde
xc = np.linspace(0, 1, num=nombre_points)

# Extrados adimensionné
yt = 5*epaisseur*(0.2969*xc**0.5-.1260*xc-.3516*xc**2+.2843*xc**3-.1036*xc**4)

# extrados intrados réels
yup = yt*corde
ydown = -yt*corde

x_reel= corde*xc
Maximum = maximum_profil_naca00xx(epaisseur,corde,precision)
print(precision,Maximum)
plt.figure(figsize=(10, 10*epaisseur+3))
plt.plot(x_reel, yup, 'g--', label='Extrados')
plt.plot(x_reel, ydown, 'r--', label='Intrados')
plt.axis([-.01*corde, 1.01*corde, -1.02*Maximum[1]-0.1, 1.02*Maximum[1]+0.1])
plt.xlabel('position de corde (m)')
plt.ylabel('épaisseur (m)')
plt.title('Représentation graphique du profil NACA 00' + str(valeur_fournie_epaisseur))
plt.legend()
bbox = dict(boxstyle="round", fc="0.8")
arrowprops = dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=90,rad=10")

offset = 18
plt.annotate('Maximum', xy=Maximum,
             xytext=(-2*offset, offset), textcoords='offset points', bbox=bbox, arrowprops=arrowprops)

plt.show()




