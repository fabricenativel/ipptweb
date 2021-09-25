# Finalisation du jeu

## Rappel des épisodes précédents

* ~~Programme à télécharger (version 4)~~ _pas pour l'instant_


## Fin du jeu lorsque le joueur gagne

Pour le moment notre boucle de jeu s'arrête lorsque le joueur a commis 7 erreurs :

```python
nb_erreurs = 0
while nb_erreurs < 7:
    # suite de notre boucle
```

On doit aussi tester la victoire du joueur et  sortir de la boucle lorsqu'elle survient. On introduit la variable booléenne `trouve` qui vaut `True` lorsque le mot a été entièrement trouvé et `False` sinon.

```python
nb_erreurs = 0
trouve = False
while nb_erreurs < 7 and not trouve:
    # suite de notre boucle
```

Comme pour le nombre d'erreurs, la mise à jour de la variable `trouve` s'effectue après chaque lettre proposée via une fonction `verifie` que nous écrirons par la suite.   

On redonne ci-dessous la boucle principale à compléter :

```python linenums="1"
nb_erreurs = 0
trouve = False
deja_proposees = ...
while nb_erreurs<7 and not trouve:
    lettre=get_lettre()
    if lettre!="":
        barre_lettre(lettre)
        deja_proposees = ...
        if lettre in MOT:
            ecrit_lettre(MOT, lettre)
            ... = verifie(MOT, deja_proposees)
        else:
            nb_erreurs+=1
            tracer_pendu(nb_erreurs)
```

1. Ligne 3 : initialiser `deja_proposees` avec la chaîne de caractères vide
2. Ligne 8 : ajouter la lettre à celles déjà proposées
3. Ligne 11 : compléter avec le nom de la variable à mettre à jour

## La fonction `verifie`

La mise à jour consiste à mettre la variable à `True` lorsque toutes les lettres du mot font partie des lettres déjà proposées qu'il nous faut donc mémoriser.

L'algorithme est donc le suivant :

- On parcourt les lettres du mot à découvrir :
    - si la lettre testée n'est pas parmi celles déjà proposées alors la fonction s'arrête et renvoie `False`
- Quand on sort de la boucle c'est qu'on n'a pas renvoyé `False`, on peut donc renvoyer `True`

!!! exercice "A faire vous-même"

    Compléter le code de la fonction `verifie` et l'intégrer à votre programme. Tester.

    ```python linenums="1"
    def verifie(..., ...):
        for lettre in ...:
            ... :
                return ...
        ...
    ```


