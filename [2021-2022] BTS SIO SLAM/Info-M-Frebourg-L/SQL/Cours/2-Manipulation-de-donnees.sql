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

-- Ajouter un fournisseur et un article


----------------------------------------


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

-- Supprimer les commandes qui ont une date à NULL
-- Supprimer tous les fournisseurs

----------------------------------------

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

-- Modifier le nom du fournisseur 425 par Harrys
-- Modifier l’adresse du client Dufour Liliane par 14 rue du Tilleuls Cergy 95300