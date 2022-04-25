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

-- Afficher les différentes désignations d’articles.
-- Afficher les différentes dates des commandes


-----------------------------------------------------

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

-- Afficher les articles dont les prix sont supérieurs à 150 euros.
-- Afficher le client numéro 200
-- Afficher les commandes du client numéro 20

-----------------------------------------------------

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

-- Afficher le nom et le prénom des clients par ordre alphabétique.
-- Afficher les articles par ordre de prix décroissant.

-----------------------------------------------------

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

-- Afficher le prix TTC des articles.