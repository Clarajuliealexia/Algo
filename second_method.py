#!/usr/bin/env python3
"""
Dans ce fichier, seront implementees toutes les fonctions necessaires
a l'execution de la seconde approche du probleme.

Le principe de cette approche est base sur l'algorithme du Weighted
Quick Union with Path Compression, utilisant une representation
particuliere d'un graphe (voir section correspondante du rapport).
"""


from collections import defaultdict, Counter

from geo.segment import Segment
from geo.tycat import tycat


class GraphWQUPC:
    """
    representation particuliere d'un graphe.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, points):
        """
        constructeur de la classe.
        """
        self.degree = len(points)
        self.vertices = []
        self.ids = defaultdict(int)
        self.sizes = [1 for _ in range(self.degree)]
        for i in range(self.degree):
            self.vertices.append(i)
            self.ids[points[i]] = i

    def root(self, index):
        """
        * retourne l'indice de la racine de l'arbre representant
        la composante connexe à laquelle appartient l'objet d'indice
        index.

        pre-conditions:
        - index est un entier compris entre 0 et self.degree-1 (inclus)
        """
        while index != self.vertices[index]:
            self.vertices[index] = self.vertices[self.vertices[index]]
            index = self.vertices[index]
        return index

    def union(self, id1, id2):
        """
        * union-command: cette fonction permet de "connecter" l'objet
        d'indice id1 a l'objet d'indice id2, en lui attribuant
        l'id de la composante connexe de l'objet d'indice id2.

        pre-conditions:
        - id1 et id2 sont deux entiers compris entre 0 et self.degree-1 (inclus)
        """
        root1, root2 = self.root(id1), self.root(id2)

        if root1 == root2:
            return

        if self.sizes[root1] <= self.sizes[root2]:
            self.vertices[root1] = root2
            self.sizes[root2] += self.sizes[root1]

        else:
            self.vertices[root2] = root1
            self.sizes[root1] += self.sizes[root2]


def second_method(distance, points):
    """
    * cette fonction peut etre consideree comme la fonction main
    associee a la deuxieme approche du probleme.

    pre-conditions:
    - distance est un flottant
    - points est un vecteur d'elements de type Point
    """
    graph = GraphWQUPC(points)

    # on cree les composantes connexes
    for i in range(graph.degree):
        point1 = points[i]
        for j in range(i+1, graph.degree):
            point2 = points[j]
            if point1.distance_to(point2) <= distance:
                graph.union(i, j)

    # on mesure leur taille
    connected_components_ids = [graph.root(edge) for edge in graph.vertices]
    result = [size for connected_component_id, size \
              in Counter(connected_components_ids).most_common()]

    print(result)
