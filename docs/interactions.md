# Vers la boucle principale du jeu

## Rappel des épisodes précédents

* Programme à télécharger (version 3).
* Rappel des notions.
* Introduction à l'éditeur

## Interaction avec le joueur

Pour demander une lettre  on utilise `feuille.textinput(titre,question)` qui crée une fenêtre dans laquelle l'utilisateur peut taper sa réponse. Les paramètres `titre` et `question` permettent de spécifier le titre de cette fenêtre et d'écrire le texte de la question.
Par exemple :

```python
lettre=feuille.textinput("Proposer une lettre","Quelle lettre proposez-vous ?")
```
 affichera :
![textinput](./images/textinput.png){.imgcentre}

1. Tester cette instruction en l'intégrant dans le programme.
2. Cette instruction n'accepte-t-elle qu'une lettre comme voulu dans le programme ?
3. Pour vérifier que le joueur propose bien une unique lettre, on écrit une fonction qui renverra la saisie de l'utilisateur seulement si elle est valide. On introduit donc ici l'instruction `return` (**renvoyer** en français), qui permet à une fonction de transmettre un résultat au reste du programme :
```python linenums="1"
def demander_lettre():
    lettre=feuille.textinput("Proposer une lettre","Quelle lettre proposez-vous ?")
    # On ajoutera ici la validation de la saisie
    return lettre
```
Il nous reste à valider la saisie avant de renvoyer la lettre via l'utilisation d'une **instruction conditionnelle**.

## Instruction conditionnelle
L'instruction conditionnelle permet de traduire en python le traitement suivant :
> **si** la saisie est une lettre de l'alphabet 
**alors** afficher le message "lettre acceptée" et renvoyer cette lettre
**sinon** afficher un avertissement et renvoyer une chaîne de caractères vide
```python linenums="1"
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
```

Ecrire une boucle `for` dans votre programme permettant d'appeler `get_lettre` à cinq reprises pour tester cette fonction.

## Boucle non bornée

La boucle `for`, déjà rencontrée permet de répéter des instructions un nombre **déterminé** de fois, on parle dans ce cas, de **boucles bornées**. La situation ici est différente, on ne connaît pas le nombre d'erreurs que va commettre le joueur avant de découvrir le mot. On utilise une **boucle non bornée** en spécifiant sa condition d'arrêt, en français cela donne : *tant que* le nombre d'erreurs possibles (limité à 6), n'est pas atteint répéter la demande d'une lettre. Ou encore en Python:

```python
nb_erreurs = 0
while nb_erreurs<7:
    lettre=get_lettre()
```

Inclure ces lignes dans le programme du pendu et constater que la boucle est pour le moment infinie puisque la variable `nb_erreurs` reste à 0. 

## Encore des instructions conditionnelles ...

Il faut donc mettre à jour l'affichage du jeu en fonction de la réponse du joueur :
* si la lettre fait  partie du mot, alors on écrit cette lettre dans la case ou les cases correspondantes ; cette tâche est réalisée par la fonction `ecrit_lettre` dont la définition vous est donnée :
```python
def ecrit_lettre(mot, lettre):
    x=-50*len(mot)//2
    for l in mot:
        if l==lettre:
            crayon.penup()
            crayon.goto(x+20,-250)
            crayon.pendown()
            crayon.write(lettre,font=("Arial",24,"bold"),align="center")
        x+=50
```

* sinon on incrémente le nombre d'erreurs :
```python
nb_erreurs = 0
while nb_erreurs<7:
    lettre=get_lettre()
    # On teste si une lettre a bien été proposée (sinon c'est la chaine vide qui est renvoyée)
    if lettre!="":
        if lettre in MOT:
            ecrit_lettre(MOT, lettre)
        else:
            nb_erreurs+=1
```
Remplacer la boucle précédente par celle-ci dans le programme du pendu, et vérifier qu'à présent la boucle se termine après 7 erreurs.

## Dessin du pendu correspondant au nombre d'erreurs

Après la mise à jour de `nb_erreurs`, on voudrait modifier en conséquence le dessin du pendu. On doit donc écrire une fonction `tracer_pendu` qui prend en paramètre le nombre d'erreurs commises par le joueur et trace le dessin correspondant. Compléter la définition de cette fonction :

```python
def tracer_pendu(nb):
    if nb == 1:
        pendu_1()
    elif nb == 2:
        pendu_2()
    elif nb == ...:
        pendu_....
    ......
```
Remarquer l'instruction `elif` contraction de `else if`.

## Appel de cette fonction dans la boucle
Compléter la boucle `while` en y incluant l'appel à cette fonction lorsque le nombre d'erreurs augmente.

## Ce qu'il reste à faire

Le jeu commence à prendre forme. Il nous manque encore la prise en compte de la victoire du joueur.