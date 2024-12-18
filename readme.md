# Projet : Combinaison et Manipulation de Fichiers CSV

Ce projet est une application Python permettant de combiner des fichiers CSV, d'effectuer des analyses sur les données combinées, et de gérer des actions spécifiques en fonction des arguments fournis par l'utilisateur via la ligne de commande.

## Fonctionnalités principales

1. **Récupération des fichiers d'un dossier**  
   La fonction `obtenir_noms_fichiers` permet de lister tous les fichiers d'un dossier spécifié.

2. **Combinaison des fichiers CSV**  
   La fonction `combiner_csv` combine plusieurs fichiers CSV en un seul, selon un ordre défini des colonnes. Les fichiers doivent avoir le même format pour garantir une combinaison correcte.

3. **Analyse et interaction via ligne de commande**  
   La fonction `arg_parse_program` interprète les arguments fournis par l'utilisateur et permet :
   - La recherche d'un produit spécifique.
   - L'affichage de plusieurs produits (avec tri facultatif).
   - Un résumé des données combinées.

## Structure du Projet

```
.
├── main.py                  # Le script principal contenant les fonctions
├── test.py                  # Tests unitaires pour le script
├── README.md                # Dossier contenant les fichiers CSV
└── csv_files/               # Fichier de sortie généré après combinaison
   └── sortie.csv            # Documentation du projet
   └── ... .csv              # Différents fichiers csv
```

## Prérequis

- Python 3.7 ou supérieur
- Modules utilisés :
  - `csv`
  - `os`
  - `argparse`

## Installation

1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone <url_du_dépôt>
   cd <nom_du_dossier>
   ```
   ```

## Utilisation

### Exécution du programme principal

Le script principal est conçu pour fonctionner avec des arguments de ligne de commande. Voici les étapes générales :

1. Placez vos fichiers CSV dans un dossier (par défaut `csv_files/`).
2. Lancez le script avec les arguments nécessaires. Exemple :
   ```bash
   python script.py --action afficher --max_elements 10 --sorted_by
   ```

### Arguments disponibles

- `--action` : Détermine l'action à effectuer parmi :
  - `rechercher` : Recherche un produit spécifique.
  - `afficher` : Affiche un nombre défini de produits.
  - `resumer` : Affiche toutes les données combinées.
- `--max_elements` : (Optionnel) Limite le nombre d'éléments affichés (par défaut : 5).
- `--sorted_by` : (Optionnel) Trie les données par une catégorie choisie (exemple : `nom`, `categorie`, `prix_produit`).

### Exemple d'exécution

#### Affichage trié
```bash
python script.py --action afficher --max_elements 10 --sorted_by
```
#### Recherche de produit
```bash
python script.py --action 
input : rechercher
```

## Tests

Des tests unitaires sont inclus pour garantir la fiabilité des fonctions principales. Les tests se trouvent dans le fichier `test_csv_combiner.py`.

### Exécution des tests

Lancez les tests avec la commande suivante :
```bash
python -m unittest test_csv_combiner.py
```

### Cas de tests couverts

1. Vérification des noms de fichiers dans un dossier valide ou vide.
2. Gestion des erreurs (dossier invalide, permissions manquantes).
3. Tests de combinaison de fichiers CSV avec différents formats.
4. Validation des arguments de ligne de commande.

## Limitations

- Tous les fichiers CSV doivent avoir le même format.
- Aucun traitement avancé des erreurs pour des fichiers CSV corrompus ou mal formés.

## Contributeurs

- **Votre Nom**  
  Mertens Corentin
