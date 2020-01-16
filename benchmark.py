#!/usr/bin/env python3
"""
Fichier permettant de realiser les mesures de performance des
differents algorithmes implementes dans le cadre du projet.
"""


from os import system
from timeit import timeit
from random import random
import matplotlib.pyplot as mpl

from geo.point import Point

from first_method import first_method
from second_method import second_method
from third_method import third_method


PATH_DIR = "/home/ensimag/algo_abey_bourgoic"


def random_input_generator(nb_points, cas_general=1):
    """
    fonction permettant de generer un couple (distance, points)
    où distance est un flottant aleatoire entre 0 et 0.2 et points
    un vecteur de nb_points objets de type Point.
    """
    distance = random()/6 if cas_general else 1
    points = [Point([random(), random()]) for _ in range(nb_points)]
    return distance, points


def perf_measure(info, method, repetition=1):
    """
    fonction permettant de realiser une mesure de performance de la
    methode method.
    """
    final_time = 0.0
    for _ in range(repetition):
        distance_max, points = info
        final_time += timeit(lambda: method(distance_max, points), number=1)
    return final_time/repetition


def main():
    """
    benchmark des algorithmes.

    ATTENTION: il faut changer la valeur de PATH_DIR en debut de fichier
    pour un affichage correct.
    """

    ## Cas général ##
    methode1 = []
    methode2 = []
    methode3 = []
    r = range(1, 100, 10)

    for nb_pts in r:
            info = random_input_generator(nb_pts, 1)
            methode1.append(perf_measure(info, first_method, 10))
            methode2.append(perf_measure(info, second_method, 10))
            methode3.append(perf_measure(info, third_method, 10))
    mpl.subplot(211)
    mpl.plot(r, methode1, label="Méthode 1")
    mpl.plot(r, methode2, label="Méthode 2")
    mpl.plot(r, methode3, label="Méthode 3")
    mpl.legend()
    mpl.title("Cas général")

    ## Cas connexe ##
    methode1 = []
    methode2 = []
    methode3 = []
    r = range(1, 100, 10)

    for nb_pts in r:
            info = random_input_generator(nb_pts, 0)
            methode1.append(perf_measure(info, first_method, 10))
            methode2.append(perf_measure(info, second_method, 10))
            methode3.append(perf_measure(info, third_method, 10))
    mpl.subplot(212)
    mpl.plot(r, methode1, label="Méthode 1")
    mpl.plot(r, methode2, label="Méthode 2")
    mpl.plot(r, methode3, label="Méthode 3")
    mpl.title("Cas connexe")

    mpl.legend()
    mpl.xlabel("Nombre de points")
    mpl.ylabel("Temps d'exécution (s)")
    mpl.savefig(PATH_DIR +"/comparaison.png")
    system("tycat "+ PATH_DIR + "/comparaison.png")


if __name__ == '__main__':
    main()
