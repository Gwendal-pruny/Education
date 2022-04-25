-- ARTICLE : refa, designation, prixht, tauxtva, categorie, qtestock, numF
-- Clef primaire : refa
-- Clef étrangère : numF en référence à Fournisseur.numF

-- COMMANDE : nocde, nocli, datecde, etat
-- Clef primaire : nocde
-- Clef étrangère : nocli en référence à Client.nocli

-- CLIENT : nocli, nomcli, prenomcli, adrcli, codePostal, ville
-- Clef primaire : nocli

-- FOURNISSEUR : numF, nom, adresse, numtel, datecreation
-- Clef primaire : numF

-- LIGCDE : nocde, refart, qtecde
-- Clef primaire : nocde, refart
-- Clef étrangère : nocde en référence à Commande.nocde, refart en référence à Article.refa

-- Donner des droits de sélection sur la table articles à tous les utilisateurs
-- Donner des droits d’insertion et de modification sur la table fournisseur à admin1
-- Donner des droits de suppression et de modification sur la table fournisseur, ligcde à admin2 avec la possibilité de transmettre ces droits.
-- Enlever les droits de modification sur la table fournisseur à admin1.

-----------------------------------------------------------

-- Créer un groupe d’administrateur, donner les droits d’insertion, de modification, de suppression sur les tables commandes et fournisseurs au groupe puis inclure les deux utilisateurs admin1 et admin2 au groupe.

-----------------------------------------------------------
