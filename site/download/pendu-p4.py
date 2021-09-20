#! /usr/bin/python3
"""
pendu.py

Le code complet du jeu du pendu, avec identification des parties
réalisées dans chacune des activités.

Auteur : Sébastien Hoarau
Date   : 2021.09
"""

# -------------------------------------------
# Activité 1 -- Notebook découverte de turtle
# -------------------------------------------

# --- Importer le module 

import turtle

# --- Les constantes
MOT = "PYTHON"

# --- Créer la feuille et le crayon

feuille = turtle.Screen()
crayon = turtle.Turtle()
feuille.bgcolor('beige')
crayon.speed(10)
crayon.hideturtle()



# -----------------------------------------------
# Activité 2 -- Notebook découverte des fonctions
# -----------------------------------------------

# On reprend une partie du code de l'activité 1
# sous forme de fonctions -- certaines probablement à faire en exercice

def ligne(x1,y1,x2,y2):
    crayon.penup()
    crayon.goto(x1,y1)
    crayon.pendown()
    crayon.goto(x2,y2)

def pendu_1():
    """Les 2 premières barres de la potence"""
    ligne(-200,-150,-100,-150)
    ligne(-150,-150,-150,200)

# --- Exercice 1 (les instructions, pas la fonction pendu_2)

def pendu_2():
    """Les 2 dernières barres de la potence"""
    ligne(-150, 150, -100, 200)
    ligne(-150, 200, 50, 200)    
    

# --- Exercice 2 

def pendu_3():
    """La corde et la tête"""
    crayon.pensize(3)
    crayon.color('black')
    ligne(0, 200, 0, 150)
    crayon.setheading(180)
    crayon.circle(25)

# --- Exercice 3 

def pendu_4():
    """Le corps"""
    ligne(0, 100, 0, 0)

def pendu_5():
    """Les 2 bras"""
    ligne(0, 80, -50, 50)
    ligne(0, 80, 50, 50)

def pendu_6():
    """Les 2 jambes"""
    ligne(0, 0, -50, -75)
    ligne(0, 0, 50, -75)

def carre(x,y):
    crayon.penup()
    crayon.goto(x,y)
    crayon.pendown()
    crayon.setheading(0)
    crayon.forward(40)
    crayon.left(90)
    crayon.forward(40)
    crayon.left(90)
    crayon.forward(40)
    crayon.left(90)
    crayon.forward(40)
    crayon.left(90)



# -----------------------------------------------
# Activité 3 -- Notebook découverte des boucles
# -----------------------------------------------

def carres(n):
    x = -50*n//2
    for i in range(n):
        carre(x,-250)
        x+=50

def affiche_alphabet():
    code_lettre = 65
    abscisse_lettre = -300
    for compteur in range(26):
        crayon.penup()
        crayon.goto(abscisse_lettre, -200)
        crayon.pendown()
        lettre = chr(code_lettre)
        crayon.write(lettre,font=("Arial",16,"bold"),align="center")
        code_lettre += 1
        abscisse_lettre+=25


# Suite

def tracer_pendu(nb_erreur):
    if nb_erreur == 1:
        pendu_1()
    elif nb_erreur == 2:
        pendu_2()
    elif nb_erreur == 3:
        pendu_3()
    elif nb_erreur == 4:
        pendu_4()
    elif nb_erreur == 5:
        pendu_5()
    elif nb_erreur == 6:
        pendu_6()


def get_lettre():
    lettre=feuille.textinput("Proposer une lettre","Quelle lettre proposez-vous ?")
    if len(lettre)==1 and lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        efface_message()
        affiche_message("Lettre acceptée")
        return lettre
    else:
        efface_message()
        affiche_message("Il faut saisir une lettre majuscule")
        return ""

def barre(lettre):
    abscisse_lettre = -300+(ord(lettre)-65)*25
    crayon.penup()
    crayon.goto(abscisse_lettre-10,-195)
    crayon.color("red")
    crayon.pendown()
    crayon.setheading(45)
    crayon.pensize(3)
    crayon.forward(22)
    crayon.color("black")

def ecrit_lettre(MOT,lettre):
    x=-50*len(MOT)//2
    for l in MOT:
        if l==lettre:
            crayon.penup()
            crayon.goto(x+20,-250)
            crayon.pendown()
            crayon.write(lettre,font=("Arial",24,"bold"),align="center")
        x+=50


def verifie(MOT,propositions):
    return all(l in propositions for l in MOT)

def affiche_message(message):
    crayon.penup()
    crayon.goto(0,300)
    crayon.pendown()
    crayon.write(message, font=("Arial",24,"bold"),align="center")

def efface_message():
    crayon.penup()
    crayon.goto(0,300)
    crayon.pendown()
    crayon.color("beige")
    crayon.write(chr(0x2588)*40, font=("Arial",24,"bold"),align="center")
    crayon.color("black")

# Programme principal

carres(6)
affiche_alphabet()
nb_erreur=0
deja_proposees=""
trouve=False
while nb_erreur<7 and not trouve:
    lettre=get_lettre()
    if lettre!="":
        barre(lettre)
        deja_proposees+=lettre
        if lettre in MOT:
            ecrit_lettre(MOT,lettre)
            trouve = verifie(MOT,deja_proposees)
        else:
            nb_erreur += 1
            tracer_pendu(nb_erreur)
if trouve:
    affiche_message("BRAVO ! Vous avez gagné.")
else:
    affiche_message("PERDU... le mot était "+MOT)




# --- A laisser à la fin

feuille.mainloop()
