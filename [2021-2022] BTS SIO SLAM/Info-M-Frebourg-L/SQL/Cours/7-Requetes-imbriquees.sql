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

-- Afficher les dates des commandes du client 324 qui sont plus récentes que certaines commandes du client 24.
-- Afficher les dates de commandes du client 325 qui sont égales aux dates de commandes du client 328.
-- Afficher les dates de commandes du client 326 qui sont inférieurs à toutes les commandes du client 529.
-- Afficher tous les fournisseurs qui n’ont pas d’articles.
-- Afficher les noms des fournisseurs qui ont la même date de création que le fournisseur Zarg.