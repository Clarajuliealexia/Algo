#!/usr/bin/env python3
"""
Dans ce fichier, seront implementees toutes les fonctions necessaires
a l'execution de la troisieme approche du probleme.
Le principe de cette approche est simple:
- on realise un quadrillage du plan a l'aide d'une (de plusieurs,
en realite) table de hachage (quadrillage conditionne par le seuil s
de proximite defini)
- on range chaque point dans un carre (donc dans une table de
hachage): cette operation est detaillee dans le rapport pdf du projet
- si deux points sont au moins une fois dans le meme carre, on les
connecte par une union command de l'algorithme du WQUPC (cf.
seconde approche)
- on denombre les composantes connexes de la meme façon que dans
la seconde approche
"""


from math import sqrt, ceil
from collections import defaultdict, Counter
from itertools import combinations

from geo.point import Point

from second_method import GraphWQUPC


def hash1(distance, point):
    """
    * cette fonction est l'implementation de la fonction h1 qui
    associe au point de coordonnees x et y le carre d'identifiant:
    int(x/distance)+1, int(y/distance)+1

    * elle retourne donc un couple d'entiers

    pre-conditions:
    - point est une instance de la classe Point
    - distance est un flottant
    """
    # pylint: disable=invalid-name

    # on s'autorise les noms de variables x et y car suffisamment
    # explicites
    x = point.coordinates[0]
    y = point.coordinates[1]

    return (ceil(x/distance),
            ceil(y/distance))


def hash2(distance, point):
    """
    *cette fonction est l'implementation de la fonction h1 qui associe au point de coordonnees
    x et y le carre d'identifiant: int((x+distance/2)/distance)+1, int(y/distance)+1

    * elle retourne donc un couple d'entiers

    pre-conditions:tycat(points, segments)
    - point est une instance de la classe Point
    - distance est un flottant
    """
    # pylint: disable=invalid-name

    # on s'autorise les noms de variables x et y car suffisamment
    # explicites
    x = point.coordinates[0]
    y = point.coordinates[1]

    return (ceil((x+distance/2)/distance),
            ceil(y/distance))


def hash3(distance, point):
    """
    * cette fonction est l'implementation de la fonction h1 qui
    associe au point de coordonnees x et y le carre d'identifiant:
    int(x/distance)+1, int((y+distance/2)/distance)+1

    * elle retourne donc un couple d'entiers

    pre-conditions:
    - point est une instance de la classe Point
    - distance est un flottant
    """
    # pylint: disable=invalid-name

    # on s'autorise les noms de variables x et y car suffisamment
    # explicites
    x = point.coordinates[0]
    y = point.coordinates[1]

    return (ceil(x/distance),
            ceil((y+distance/2)/distance))


def hash4(distance, point):
    """
    * cette fonction est l'implementation de la fonction h1 qui
    associe au point de coordonnees x et y le carre d'identifiant:
    int((x+distance/2)/distance)+1, int((y+distance/2)/distance)+1

    * elle retourne donc un couple d'entiers

    pre-conditions:
    - point est une instance de la classe Point
    - distance est un flottant
    """
    # pylint: disable=invalid-name

    # on s'autorise les noms de variables x et y car suffisamment
    # explicites
    x = point.coordinates[0]
    y = point.coordinates[1]

    return (ceil((x+distance/2)/distance),
            ceil((y+distance/2)/distance))


def divide_into_squares(distance, points):
    """
    * cette fonction retourne un vecteur de quatre tables de hachages
    et les remplit en hachant les points a l'aide des fonctions de
    hachages associees.

    * chaque table de hachage contient tous les points

    pre-conditions:
    - points est un vecteur d'elements de type Point
    - distance est un flottant
    """
    real_distance = 2*distance

    table1 = defaultdict(list)
    table2 = defaultdict(list)
    table3 = defaultdict(list)
    table4 = defaultdict(list)

    for point in points:
        table1[hash1(real_distance, point)].append(point)
        table2[hash2(real_distance, point)].append(point)
        table3[hash3(real_distance, point)].append(point)
        table4[hash4(real_distance, point)].append(point)

    tables = [table1, table2, table3, table4]
    return tables


def third_method(distance, points):
    """
    cette fonction va repondre au probleme pose: elle affiche
    le vecteur trie dans l'ordre decroissant des tailles des
    differentes composantes connexes.

    pre-conditions:
    - points est un vecteur d'elements de type Point
    - distance est un flottant
    """
    # initialisation du graphe
    graph = GraphWQUPC(points)

    # hachage des points dans des carres
    tables = divide_into_squares(distance, points)

    # on cree les composantes connexes
    for table in tables:
        for square in filter(lambda l: len(l) > 1, table.values()):
            for pt1, pt2 in combinations(square, 2):
                id1, id2 = graph.ids[pt1], graph.ids[pt2]
                if graph.root(id1) != graph.root(id2):
                    if pt1.distance_to(pt2) <= distance:
                        graph.union(id1, id2)

    roots = [graph.root(e) for e in graph.vertices]
    result = [e[1] for e in Counter(roots).most_common()]

    print(result)
