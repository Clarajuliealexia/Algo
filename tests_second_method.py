#!/usr/bin/env python3
"""
fichier permettant de realiser des tests pour chacune des fonctions du fichier
second_method.py.
"""
from random import randint

from geo.point import Point
from geo.tycat import tycat
from geo.segment import Segment

from third_method import hash1, hash2, hash3, hash4, divide_into_squares

def point_aleatoire(nombre, bornes):
    """
    fonction retourner un vecteur de nombre objets aleatoires de type Point.
    les abscisses et ordonnees des points generes sont comprises entre bornes[0]
    et bornes[1].

    pre-conditions:
    - nombre est un entier
    """
    points = [Point([randint(bornes[0], bornes[1]), randint(bornes[0], bornes[1])])
              for _ in range(nombre)]
    return points

def test_hashs():
    """
    fonction permettant de tester le hachage des points dans les differents carres.
    elle affiche la syntaxe svg correspondant au plan quadrille et les differents points
    de couleurs differentes selon le carre.

    le cote du carre est une valeur fixee dans le programme.

    pre-conditions:
    - points est un vecteur d'elements de type Point
    """
    distance = 40
    nbr = 400//distance
    points = point_aleatoire(200, [0, 400])

    print("test h1")
    quadrillage_vertical = [Segment([Point([i*distance, 0]), Point([i*distance, 400])])
                            for i in range(nbr+1)]
    quadrillage_horizontal = [Segment([Point([0, j*distance]), Point([400, j*distance])])
                              for j in range(nbr+1)]
    quadrillage = quadrillage_horizontal + quadrillage_vertical
    tycat(points, quadrillage)

    tables = divide_into_squares(distance, points)
    tycat(list(tables[0][carre]) for carre in tables[0])
    print("test h2")
    print("test h3")
    print("test h4")

test_hashs()
