#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from sys import argv
from geo.point import Point
from first_method import first_method
from second_method import second_method
from third_method import third_method


def load_instance(filename):
    """
    loads .pts file.
    returns distance limit and points.
    """
    with open(filename, "r") as instance_file:
        lines = iter(instance_file)
        distance = float(next(lines))
        points = [Point([float(f) for f in l.split(",")]) for l in lines]

    return distance, points


def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    # premiere approche du probleme
    # first_method(distance, points)

    # deuxieme approche du probleme
    # second_method(distance, points)

    # troisieme methode
    third_method(distance, points)


def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)


main()
