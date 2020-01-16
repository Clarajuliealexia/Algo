Projet d'algorithmique réalisé par Yann-Laurick ABE et Clara BOURGOIN - 2018/2019 - 1A Ensimag

Ce fichier a pour vocation de permettre au lecteur d'avoir une vision globale du projet, et de l'organisation des differents fichiers.


## Fichiers initialement presents
- d'un fichier connectes.py qui est le fichier principal contenant la fonction main. C'est ce fichier qui est lance pour les differents tests.
- d'un repertoire geo: module fourni, contenant les classes d'objets et les fonctions permettant leur representations graphique.
- des fichiers exemple_1.pts, exemples_2.pts, exemples_3.pts et exemple_4.pts qui sont les entrees de nos algorithmes.
- d'un fichier hello.py qui est un exemple d'utilisation du module tycat fourni.
- d'un fichier sujet.pdf qui contient l'enonce du projet.


## Fichiers personnels
- du present fichier README.txt
- d'un fichier first_method.py ou sont implementees toutes les
fonctions utilisees dans le cadre de la "premiere approche du probleme"
- d'un fichier second_method.py ou sont implementees toutes les
fonctions utilisees dans le cadre de la "deuxieme approche du probleme"
- d'un fichier third_method.py ou sont implementees toutes les fonctions
utilisees dans le cadre de la "troisieme approche du probleme"
- d'un fichier benchmark.py qui permet d'effectuer des comparaisons
des performances de nos differents algorithmes.
- de deux graphiques de performance realise avec le fichier benchmark.py


## Utilisation 
Pour effectuer le test des differentes methodes, il faudra lancer le programme connectes.py avec un fichier texte du type des fichiers exemple_x.pts en argument : ./connectes exemple_x.pts. Cette fonction renverra le resultat de la methode 3.
Pour afficher les résultats du test de performance sur les differentes methodes, il faut lancer le programme benchmark.py : ./benchmark. Cette fonction va afficher deux graphes de performances : l'un dans un cas moyen et l'autre dans le pire cas c'est a dire quand tous les points sont dans la meme composante connexe. Attention, pour lancer le programme benchmark, il faut ouvrir le fichier source et changer la valeur de PATH_DIR our avoir un affichage correct.
