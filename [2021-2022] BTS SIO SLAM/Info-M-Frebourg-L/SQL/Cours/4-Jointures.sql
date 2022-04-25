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

-- Afficher les dates de commande du ou des clients John
-- Afficher le prix des articles de la commande 324.
-- Afficher les adresses des fournisseurs pour l’article 328.
-- Afficher le nom des clients qui ont commandé chez le fournisseur WAMTER.

---------------------------------------------------------

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

-- Afficher le nombre de commandes par clients.
-- Afficher le nombre d’articles par code tva
-- Afficher le nombre de commandes pour le client 324
-- Afficher le nombre de commandes pour le client 325 et le client 326
-- Afficher le nombre de commandes du client 328 groupé par date.
-- Afficher le nombre de commandes du client 328 chaque jour.
-- Afficher le prix maximum des articles par fournisseur
-- Afficher la somme du prix des articles

---------------------------------------------------------

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

-- Afficher les commandes du client 400 groupé par date à partir du 18/09/2011
-- Afficher les nombres de commandes supérieurs à 7 groupé par date à partir de 2011
-- Afficher les articles groupés par catégorie dont les prix totaux sont supérieurs à 25 euros

---------------------------------------------------------

