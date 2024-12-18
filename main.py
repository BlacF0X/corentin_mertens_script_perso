"""importation des modules csv | os | argparse"""

import csv
import os
import argparse

def obtenir_noms_fichiers(dossier):
    """
    Récupère tous les noms de fichiers dans un dossier spécifié.

    Args:
        dossier (str): Chemin du dossier.

    Returns:
        list: Liste des noms de fichiers dans le dossier.
    """
    try:
        if not os.path.isdir(dossier):
            raise ValueError(f"Le chemin spécifié n'est pas un dossier : {dossier}")
        return [os.path.join(dossier,f) for f in os.listdir(dossier)]

    except Exception as e:
        print(f"Erreur lors de la récupération des fichiers : {e}")



def combiner_csv(liste_fichiers, fichier_sortie):
    """
        Combine plusieurs fichiers CSV de même taille en un seul fichier.

        PRE:
            liste_fichiers (list): Liste des chemins des fichiers CSV à combiner.
            fichier_sortie (str): Chemin du fichier CSV de sortie.
    """
    liste_sortie = []
    ordre = [1,2,0,3,4]
    liste_fichier = []
    try:
        # Vérifier si la liste est vide
        if not liste_fichiers:
            raise ValueError("La liste des fichiers est vide.")
        for fichier in liste_fichiers:
            with open(fichier,'r') as file:
                print(f'load {str(fichier)} : OK')
                csv_reader = csv.reader(file, delimiter=',')
                liste_csv = list(csv_reader)
                liste_fichier.append(liste_csv[0])
            print(liste_fichier)
        print('-----------------------------------')
        for i in range(len(liste_fichier[0])-1):
            liste_elem = []
            for j in ordre:
                liste_elem.append(liste_fichier[j][i])
            print(liste_elem)
            liste_sortie.append(liste_elem)
        with open(fichier_sortie, "w",newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',')
            csv_writer.writerows(liste_sortie)
        return liste_sortie
    except Exception:
        print(f'Il y a eu un problème')


def arg_parse_program(csv_dossier,output_fichier):
    '''
    cette fonction recupère la commande avec le argparse,et affiche les infos en consequence
    PRE :
    :param csv_dossier: le dossier dans lequel on va chercher les différents fichier csv
    :param output_fichier: fichier ou on va potentiellement ecrire le resumé du tableau
    POST : cette fonction ne retourne rien

    '''
    exit_file = os.path.join(csv_dossier,output_fichier)
    print("-------IMPORTATION DES FICHIERS-------")
    # Création de l'analyseur d'arguments
    parser = argparse.ArgumentParser(
        description="Trouver des éléments dans les stocks selon diférents critère"
    )
    parser.add_argument("--action",
                        type=str,
                        required=True,
                        help='que voulez vous faire ')
    # Définir les arguments
    parser.add_argument("--sorted_by",
                        action="store_true",
                        help="si on doit renvoyée de manière triée ou pas"
                        )
    parser.add_argument(
        "--max_elements",
        type=int,
        default=5,
        required= True,
        help="Le nombre maximum d'éléments à afficher (défaut : 5)."
    )


    # Analyse des arguments
    args = parser.parse_args()
    methode = args.action.lower()
    main_method(methode,args.max_elements,args.sorted_by,csv_dossier,exit_file)

# Programme principal
def main_method(methode,el_max,sorted_by,csv_dossier,output_fichier):
    print('--------Actions possible------')
    print('rechercher afficher resumer')
    liste_methode = ['rechercher', 'afficher', 'resumer']
    meth_ind = 0
    liste_fichier = obtenir_noms_fichiers(csv_dossier)
    liste_sortie = combiner_csv(liste_fichier, output_fichier)
    if liste_sortie == None:
        raise TypeError
    try:
        if methode in liste_methode:
            meth_ind = liste_methode.index(methode)
    except IndexError:
        pass
    if meth_ind == 0:
        produit = input("quel est le produit que vous voulez voir" )
        for prod in liste_sortie:
            if produit in prod:
                print(prod)
        try:
            os.remove(output_fichier)
        except FileNotFoundError:
            raise FileNotFoundError("le fichier n'est pas correct")
    elif meth_ind == 1:
        if el_max > len(liste_sortie):
            max_el = len(liste_sortie)
        else:
            max_el = el_max
        if sorted_by:
            liste_cat = {'categorie':2,'prix_produit':4,'nom':1}
            cat_input = input('indiquez une catégorie categorie,id_produit,nom')
            if cat_input not in liste_cat:
                print('this is not a category')
                liste_temp = liste_sortie[:]
            else:
                liste_temp = sorted(liste_sortie[:], key=lambda x: x[liste_cat[cat_input]])
        else:
            liste_temp = liste_sortie[:]
        for i in range(max_el):
            l_prod = liste_temp[i]
            print(l_prod)
        os.remove(output_fichier)
    elif meth_ind == 2:
        for i in liste_sortie:
            print(i)



# Exemple d'utilisation
if __name__ == "__main__":
    DOSS_CSV = 'csv_files'
    FICH_SORTIE = 'sortie.csv'
    arg_parse_program(DOSS_CSV, FICH_SORTIE)