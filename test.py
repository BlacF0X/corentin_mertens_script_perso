import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
import csv
from io import StringIO
import argparse
from xml.dom import NotFoundErr

import main
# Import des fonctions du script
from main import obtenir_noms_fichiers,main_method,combiner_csv

class TestScriptFunctions(unittest.TestCase):

    def setUp(self):
        """Initialisation des données pour les tests."""
        self.dossier_test = "test_folder"
        self.fichiers_csv = ["fichier1.csv", "fichier2.csv", "fichier3.csv"]
        self.contenu_csv = [
            ["id", "nom", "categorie", "id_produit", "prix"],
            ["1", "produit1", "cat1", "123", "10.5"],
            ["2", "produit2", "cat2", "456", "20.0"],
            ["3", "produit3", "cat3", "789", "30.0"]
        ]

    @patch('os.path.isdir')
    @patch('os.listdir')
    def test_obtenir_noms_fichiers(self, mock_listdir, mock_isdir):
        """Test pour obtenir_noms_fichiers."""
        mock_isdir.return_value = True
        mock_listdir.return_value = self.fichiers_csv

        resultat = obtenir_noms_fichiers(self.dossier_test)

        attendu = [os.path.join(self.dossier_test, f) for f in self.fichiers_csv]
        self.assertEqual(resultat, attendu)

        mock_isdir.assert_called_once_with(self.dossier_test)
        mock_listdir.assert_called_once_with(self.dossier_test)

    @patch('os.path.isdir')
    def test_obtenir_noms_fichiers_dossier_invalide(self, mock_isdir):
        """Test pour obtenir_noms_fichiers avec un dossier invalide."""
        mock_isdir.return_value = False
        resultat = obtenir_noms_fichiers(self.dossier_test)

        self.assertEqual(resultat, None)

    def test_combiner_csv_liste_vide(self):
        """Test pour combiner_csv avec une liste de fichiers vide."""
        resultat = combiner_csv([], "sortie.csv")
        self.assertEqual(resultat, None)

    @patch("builtins.open", new_callable=mock_open)
    def test_combiner_csv_incorrect_format(self, mock_file):
        """Test pour combiner_csv avec des fichiers ayant des formats incorrects."""
        fichiers_contenu = [
            StringIO("id,nom,categorie\n1,produit1,cat1\n"),  # Manque des colonnes
            StringIO("id,nom,categorie,id_produit,prix\n2,produit2,cat2,456,20.0\n"),
        ]

        mock_file.side_effect = fichiers_contenu

        liste_fichiers = ["fichier1.csv", "fichier2.csv"]
        fichier_sortie = "sortie.csv"

        with patch("builtins.print") as mock_print:
            resultat = combiner_csv(liste_fichiers, fichier_sortie)
            mock_print.assert_called_with("Il y a eu un problème")
            self.assertEqual(resultat, None)


    @patch('os.path.isdir')
    @patch('os.listdir')
    def test_obtenir_noms_fichiers_dossier_vide(self, mock_listdir, mock_isdir):
        """Test pour obtenir_noms_fichiers avec un dossier vide."""
        mock_isdir.return_value = True
        mock_listdir.return_value = []

        resultat = obtenir_noms_fichiers(self.dossier_test)
        self.assertEqual(resultat, [])

    @patch('os.listdir')
    def test_obtenir_noms_fichiers_permission_error(self, mock_listdir):
        """Test pour obtenir_noms_fichiers avec une erreur de permission."""
        mock_listdir.side_effect = PermissionError("Permission denied")

        resultat = obtenir_noms_fichiers(self.dossier_test)
        self.assertEqual(resultat, None)

    def test_main_methode_creation_supression_fichier_sortie(self):
        max_el = 2
        csv_doss = 'csv_files'
        meth = 'resumer'
        sort_by = True
        #verifie la creation d'un fichier resultat
        main.main_method(meth,max_el,sort_by, csv_doss,'csv_files/sortie.csv')
        self.assertIn('sortie.csv', os.listdir(csv_doss))
        #verifier la suppresion du fichier si le mode n'est pas resumer
        meth = 'afficher'
        max_el = 2
        sort_by = True
        main.main_method(meth,max_el,sort_by, csv_doss,'csv_files/sortie.csv')
        self.assertNotIn('sortie.csv', os.listdir(csv_doss))

    def test_main_methode_argument_incorrect(self):
        max_el = -2
        csv_doss = 'csv'
        meth = 'ouvrir'
        sort_by = True
        self.assertRaises((Exception,TypeError),main.main_method,meth,max_el,sort_by, csv_doss, 'sortie.csv')

    def test_main_action(self):
        csv_doss = 'csv_files'
        meth = 'aficher'
        sort_by = True
        self.assertEqual(main.main_method(meth,3,sort_by, csv_doss, 'sortie.csv'), None)


if __name__ == "__main__":
    unittest.main()
