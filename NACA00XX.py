""" Le présent programme permet de tracé une représentation d'un profilNACA symétrique et
    de donner son épaisseure maximum et la position du maximum """
import numpy as np
import matplotlib.pyplot as plt

# récupération des informations sur le profil NACAXX

valeur_fournie_epaisseur= int(input("Donnez le numero (xx) de votre profil NACA symmetrique NACA00XX : "))
corde = float(input("Quelle est la corde en mètre de votre profil NACA :"))
distribution = input("Quelle distribution de point souhaitez vous avoir : lineaire (l) ou non-lineaire (n)")
nombre_points = int(input("Combien de point voulez vous le long de la corde :"))
