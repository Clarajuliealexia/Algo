#!/usr/bin/env python3
"""
Dans ce fichier, seront implementees toutes les fonctions necessaires
a l'execution de la premiere approche du probleme.

Le principe de cette approche est basee sur l'algorithme du Quick Find
, utilisant une representation particuliere d'un graphe (voir section
correspondante du rapport).
"""


from collections import defaultdict, Counter

from geo.point import Point
from geo.tycat import tycat
from geo.segment import Segment


class GraphQF:
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
        for i in range(self.degree):
            self.vertices.append(i)
            self.ids[points[i]] = i

    def union(self, id1, id2):
        """
        * union-command: cette fonction permet de "connecter" l'objet
        d'indice id1 a l'objet d'indice id2, en lui attribuant
        l'id de la composante connexe de l'objet d'indice id2.

        pre-conditions:
        - id1 et id2 sont deux entiers compris entre 0 et self.degree-1
        """
        old_connected_component_id = self.vertices[id1]
        new_connected_component_id = self.vertices[id2]
        for k, elt in enumerate(self.vertices):
            if elt == old_connected_component_id:
                self.vertices[k] = new_connected_component_id


def first_method(distance, points):
    graph = GraphQF(points)

    # on cree les composantes connexes
    for i in range(graph.degree):
        point1 = points[i]
        for j in range(i+1, graph.degree):
            point2 = points[j]
            if point1.distance_to(point2) <= distance:
                graph.union(i, j)

    result = [e[1] for e in Counter(graph.vertices).most_common()]

    print(result)
