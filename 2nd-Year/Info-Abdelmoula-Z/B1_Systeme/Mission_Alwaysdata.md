#### [Gwendal PRUNY](mailto:gwendal.pruny@gmail.com), ESIEE-IT
#### Mission Alwaysdata (BTS - SIO) - 14/03/2022

## Etape 0 : Créer un espace sur Alwaysdata

Créer un compte sur Alwaysdata gratuit (100 Mo). ok


Quels services sont offerts par Alwaysdata ?

alwaysdata est un site de hosting, particulièrement de hosting web a haut trafique
    -serveurs haute performance 100% SSD
    -SSL automatique et gratuit
    -langages et versions configurables par site
    -installation en 1 clic de dizaines d’applications
    -sauvegardes quotidiennes conservées 30 jours
    -cache HTTP et WAF intégrés
    -solution e-mails complète
    -support avancé, rapide et efficace

Quels services seront nécessaires pour déployer un site web (HTML, CSS, JS et PHP) ?

Étape 1 : délimiter votre projet 
Étape 2 : mise en ligne des fichiers du site sur l’espace de stockage
Étape 3 : lier le site internet à une base de données
Étape 4 : accéder à votre site internet


Quel est le nom de domaine choisi pour le déploiement de votre site ?

.fr

## Etape 1 : Activer SSH

Pour ajouter les fichiers de votre site web à votre espace, il faut activer votre accès ssh.

- Expliquer l'intérêt du protocole SSH. Sur quel port est-il actif par défaut ? 

 Il permet la connexion d'une machine distante (serveur) via une liaison sécurisée dans le but de transférer des fichiers ou des commandes en toute sécurité
 Par défaut le protocole SSH est sur le port 22

- Quel autre protocole semble avoir les mêmes fonctionnalités ? Que fait SSH qui n'est pas possible avec le 2e ? 

FTP, cependant

- Activer un accès au serveur via ce protocole. Quelles étapes sont nécessaires ? 

Avoir l'ip 

- Se connecter à votre espace dédié sur le serveur via ce protocole. Quelle est la ligne de commande nécessaire pour y arriver ? 

connect ssh-pruny.alwaysdata.net

- Dans quel repertoire faut-il déposer vos fichiers du site si vous voulez le voir en ligne ? (chemin complet sur le serveur) 

www

## Etape 2 : Copier notre contenu sur Alwaysdata

Ajouter les fichiers du site sauvegardé en local au répertoire distant dédié.

- Quel est le chemin local absolu pour accéder à votre site ?

home/server/www/

- Quel est le chemin absolu du repertoire dédié sur le serveur Alwaysdata ?

/www/

- Les commandes `scp` et `rsync` peuvent être d'une grande aide à cette étape. Pourquoi ? 

transfert de fichier à travers une connexion ssh et rsync syncrhonise le répertoire local aux distan

- Quelle est la différence entre les deux commandes ?

transférer un fichier précis n'acctualise pas le répertoire local

- Quelle est la commande complète pour ajouter les fichiers sauvegardés en local sur le serveur dédié ?

rsync -a ssh-pruny@.alwaysdata.net:/www/media/ /home/www/media/
rsync -a /home/www/media/ ssh-pruny@.alwaysdata.net:/www/media/

- Comment vérifier que l'ajout a bien été effectué ? Détailler la procédure et les résultats attendus.

rsync -a -P /home/www/media/ ssh-pruny@.alwaysdata.net:/www/media/ (pour voir l'avencer du téléchargement)
Ou vérifier sur l'api du répo distant

- Quelle URL permet de voir votre site en ligne ? 

ssh-pruny.alwaysdata.net