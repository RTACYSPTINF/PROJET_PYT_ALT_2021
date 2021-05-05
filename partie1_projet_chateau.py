"""
Création : spitoni JP
Date : mars 2021
Sources : Apprendre à coder avec Python mooc fun
"""
import os
from CONFIGS import *
import turtle
from math import *




"""
Cette partie va permettre de tranformer le fichier texte  suivant :
H:\Doc_jspit\Travail-2010-2011\cours-TD-TP_JP\cours\Algo-RT1-Python\python_avance_S2\Projet-chateau\plan_chateau.txt
contenant :
1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 0 0 0 1 0 0 0 1 0 1 0 0 0 1 4 0 0 1
1 1 1 0 1 0 1 0 1 0 1 0 1 0 1 1 1 0 1       
1 0 0 0 3 0 1 0 0 0 1 0 1 0 0 0 0 0 1
1 0 1 1 1 1 1 0 1 0 1 0 1 1 1 1 1 1 1
1 0 0 0 1 0 0 0 1 0 3 0 0 0 0 0 0 0 1
1 1 1 0 1 0 1 1 1 1 1 1 1 0 1 1 1 0 1
1 4 1 0 1 0 0 0 1 0 0 0 0 0 1 0 0 0 1
1 0 1 0 1 1 1 0 1 0 1 1 1 0 1 1 1 1 1
1 0 0 0 1 0 0 0 1 0 0 0 1 0 3 0 0 0 1
1 1 1 1 1 0 1 1 1 0 1 1 1 1 1 0 1 0 1
1 0 0 0 3 0 1 4 0 0 1 0 0 0 1 0 0 4 1
1 0 1 1 1 1 1 1 1 1 1 0 1 0 1 1 1 1 1
1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 1
1 0 1 0 1 0 1 0 1 0 1 1 1 1 1 1 1 0 1
1 0 1 0 1 0 1 0 1 0 0 0 0 0 1 0 0 0 1
1 1 1 3 1 0 1 0 1 1 1 1 1 3 1 0 1 1 1
1 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 0 0 1
1 0 1 1 1 1 1 0 1 1 1 0 1 1 1 1 1 0 1
1 0 0 0 1 0 0 0 1 0 1 0 0 0 0 0 1 0 1
1 1 1 0 1 0 1 1 1 0 1 1 1 0 1 0 1 0 1
1 0 0 0 3 0 0 0 3 0 1 0 0 0 1 0 1 0 1
1 0 1 1 1 1 1 1 1 0 1 0 1 1 1 1 1 0 1
1 0 0 0 1 4 0 0 1 0 3 0 0 0 1 0 0 0 1
1 1 1 0 1 1 1 0 1 0 1 0 1 1 1 0 1 1 1
1 4 0 0 0 0 1 0 0 0 1 0 0 0 1 0 3 0 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1

en une liste de listes ou chaque éléments est une liste des nombres de chacunes des lignes du fichier :
[[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 4, 0, 0, 1],
etc]

"""


##########################################################################
##########################################################################
##################     Fonction lire_matrice
##########################################################################
##########################################################################

def lire_matrice(fichier):
    """
    cette fonction répond à la première question du projet
    """
    os.chdir(r"H:\Doc_jspit\Travail-2010-2011\cours-TD-TP_JP\cours\Algo-RT1-Python\python_avance_S2\Projet-chateau")
    with open(fichier,'r',encoding="utf-8") as f:
        matrice=f.readlines()
    L=[] # liste vide qui accueilera le résultat final
    for element in matrice:
        L.append(element.strip().split())
    return L




##########################################################################
##########################################################################
##################     Fonction trace_cadre(p_origine, delta_X, delta_Y)
##########################################################################
##########################################################################
def trace_cadre(p_origine, delta_X, delta_Y):
    turtle.penup()
    turtle.goto(x=p_origine[0], y=p_origine[1])

    turtle.pendown()
    turtle.goto(-240,-240)
    """
    turtle.left(90)
    turtle.forward(480)
    turtle.left(90)
    turtle.forward(480)
    turtle.left(90)
    turtle.forward(480)
    turtle.left(90)
    turtle.forward(480)
    turtle.pendown()
    turtle.goto(0,0)
    """


    turtle.mainloop()
    print(ZONE_PLAN_MINI)

##########################################################################
##########################################################################
##################     Fonction calcul_pas(matrice)
##########################################################################
##########################################################################
def calcul_pas(matrice):
    """
    cette fonction prend en entrée matrice, elle renvoie en sortie la valeur du pas 
    pour que le dession du labyrinthe rentre dans la zone graphique qui lui est réservé.
    """
    # on récupère les dimensions de la matrice
    nb_case_hauteur=len(matrice)
    nb_case_largeur=len(matrice[0])
    pas_largeur=(ZONE_PLAN_MAXI[0]-ZONE_PLAN_MINI[0])/nb_case_largeur
    pas_hauteur=(ZONE_PLAN_MAXI[1]-ZONE_PLAN_MINI[1])/nb_case_hauteur
    #print(nb_case_hauteur, nb_case_largeur)
    #print(pas_hauteur, pas_largeur)
    return int(min(pas_hauteur,pas_largeur)) # on prend le min des deux





##########################################################################
##########################################################################
##################     Fonction coordonnees(case, pas)
##########################################################################
##########################################################################
def coordonnees(case, pas):
    """
    case=(0,0)
    pas =15
    """
    
    # calcul des coordonées 
    x=-240+pas*case[0]
    y=-240+(26-case[1])*pas
    return x,y

    



##########################################################################
##########################################################################
##################     Fonction tracer_carre(dimension)
##########################################################################
##########################################################################
def tracer_carre(dimension):
    """
    Fonction qui tracer u carré de dimension 15 si 
    la valeur de la variable 'dimension' vaut 15
    """
    turtle.hideturtle()
    turtle.penup()
    turtle.pendown()
    turtle.color("black","red")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(dimension)
        turtle.left(90)
    turtle.end_fill()
    

    turtle.mainloop()


##########################################################################
##########################################################################
##################     Fonction tracer_case(case, couleur, pas)
##########################################################################
##########################################################################
def trace_case(case, couleur, pas):
    """
    """
    matrice=lire_matrice(fichier_plan)
    x,y=coordonnees(case,pas)
    print(x,y)
    turtle.color("black","yellow")
    turtle.begin_fill()
    pas =calcul_pas(matrice)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    tracer_carre(pas)
    turtle.end_fill()




##########################################################################
##########################################################################
##################     Fonction afficher_plan(matrice)
##########################################################################
##########################################################################



##########################################################################
##########################################################################
##################     PROGRAMME PRINCIPAL DE TEST PARTIE 1
##########################################################################
##########################################################################
if __name__=="__main__":
    matrice=lire_matrice(fichier_plan)
    """
    print(calcul_pas(matrice))
    print(coordonnees((0,0),15))
    #trace_case((0,0),'yellow',15)
    trace_case((26,0),'yellow',15)
    trace_case((25,17),'yellow',15)
    trace_case((0,17),'yellow',15)
"""
    