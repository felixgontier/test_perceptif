# -*- coding: cp1252 -*-
import os
import random


#
#
#

while True:
    try:
        while True:
            try:
                nb_test=int(raw_input("Entrez le nombre de fichiers audio etalon : "))
                break
            except ValueError:
                print "Not a number"

        while True:
            try:
                nb_of_files=int(raw_input("Entrez le nombre total de fichiers audio : "))
                break
            except ValueError:
                print "Not a number"
        if (nb_test>nb_of_files):
            raise ValueError
        break
    except ValueError:
        print ("Incoherent")

    


fichier = open("rnd_Agr_Point.txt","w")
liste_fichiers = [i for i in range (1,nb_of_files+1)]
for nb_lignes in range (51):

    for fichier_nb in range (1,nb_test+1):
        fichier.write(str(fichier_nb)+" ")

    liste_rnd = random.sample(liste_fichiers,len(liste_fichiers))
    while liste_rnd[0] == nb_test or liste_rnd[0] == nb_test-1:
        liste_rnd = random.sample(liste_fichiers,len(liste_fichiers))             
                              
    for fichier_nb in (liste_rnd):
        fichier.write(str(fichier_nb)+" ")
    fichier.write('\n')
print("Le fichier a été généré")
fichier.close()
