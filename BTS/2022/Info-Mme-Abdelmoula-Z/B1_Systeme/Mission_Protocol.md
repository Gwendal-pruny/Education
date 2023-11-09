#### [Gwendal PRUNY](mailto:gwendal.pruny@gmail.com), ESIEE-IT
## Mission : Wireshark et découvertes des protocoles (BTS - SIO) - 14/03/2022

### Objectif

Analyser le trafic réseau généré par des clients et serveurs - zoom sur les messages HTTP,  HTTPS, FTP et SSH à l’aide du logiciel Wireshark.

Un **compte rendu** devra être déposé sur GitLab sous les formats Markdown et PDF -> `B1_Systeme/Mission_Protocoles.md` et `B1_Systeme/Mission_Protocoles.pdf`

Liens utiles :

- Doc officielle wireshark : <https://www.wireshark.org/docs/wsug_html_chunked/ChapterUsing.html>
- Pour un ping facilité : <https://manage.accuwebhosting.com/knowledgebase/2609/How-to-Enable-PingorICMP-Echo-Request-in-Windows-Server.html>

Quelques tutoriels Wireshark :

- <https://leprogrammeurmarocain.com/comment-utiliser-wireshark/>
- <http://razik.univ-tln.fr/misc/I42/Wireshark/index.html>
- <https://astuces-informatique.com/wireshark-capturer-filtrer-inspecter-paquets/>

## Etape 1 - Installer Wireshark

- Télécharger ou récupérer le logiciel Wireshark (<https://www.wireshark.org/>) (Gnu Linux : `# apt update` et ensuite `# apt install wireshark` en tant que superutilisateur).

ok

- Résumer en quelques phrases, l'utilité de ce logiciel et ce qu'il permettra de réaliser

Wireshark is the world’s foremost and widely-used network protocol analyzer.
It lets you see what’s happening on your network at a microscopic level and is the de facto (and often de jure) standard across many commercial and non-profit enterprises,
government agencies, and educational institutions.
Wireshark development thrives thanks to the volunteer contributions of networking experts around the globe and is the continuation of a project started by Gerald Combs in 1998.

Wireshark est un analyseur de paquets libre et gratuit.
Il est utilisé dans le dépannage et l’analyse de réseaux informatiques,
le développement de protocoles, l’éducation et la rétro-ingénierie

- Installer Wireshark sur votre machine hôte (en cochant toutes les options utiles)

OK

- Démarrer l'application et essayer de la prendre en main
  - Quelles fonctionnalités de wireshark semblent intéressantes ?

 Capture
 Analyze
 Statistiques
 Telephony

**Pour les étapes suivantes représenter votre expérimentation via un diagramme de déploiement comme celui-ci**

![diagramme de déploiement minimal](DiagDeploiement.png)

## Etape 2 - Analyser le trafic généré par un serveur http

1. Que fait-on pour provoquer l'envoi d'une requête HTTP ? Préciser tous les détails pertinents.

Dès que un échange entre Client / Server sont fait une requête HTTP est envoyer

1. Identifier avant chaque capture l'IP du client et l'IP du serveur.

Client : 172.16.97.154
Server : 3.251.111.180

1. Démarrer votre capture sur la bonne interface réseau.

OK

1. Réaliser quelques requêtes HTTP
 a. vers un serveur web local (localhost)
 b. vers un serveur web distant (le vôtre configuré sur AlwaysData)

4. Enregistrer la capture sous `captureHTTP.pcapng`.
4. Filtrer les paquets HTTP échangés

- Comment différencier les requêtes des réponses ?

 Une réponses contient forcément un status (200, 401..) une requête recevera toujours une réponses

- Combien de paires (requête et réponse) ont été échangées suite à votre action décrite en 1. ?

3

## Etape 3 - Analyser le trafic généré par un serveur https

1. Que fait-on pour provoquer l'envoi d'une requête HTTPS ? Préciser tous les détails pertinents.

	Envoi d'une requête vers un serveur sécurisée

1. Identifier avant chaque capture l'IP du client et l'IP du serveur.



1. Démarrer votre capture sur la bonne interface réseau.
1. Réaliser quelques requêtes HTTPS :
 a. vers un serveur web distant configuré en HTTPS (le vôtre configuré sur AlwaysData)

4. Enregistrer la capture sous `captureHTTPS.pcapng`.
4. Filtrer les paquets HTTPS échangés

- Comment différencier les requêtes des réponses ?
- Combien de paires (requête et réponse) ont été échangées suite à votre action décrite en 1. ?

2. Quelles différences remarquez-vous avec le protocole HTTP ?

## Etape 4 - Analyser le trafic généré par un serveur ftp

Voici un accès vers un serveur FTP de test : <https://dlptest.com/ftp-test/>. Il est aussi possible de se connecter en FTP à votre serveur sur AlwaysData.

1. Quel type de client faut-il installer pour vous y connecter ? Installez-le !

1. Que fait-on pour provoquer l'envoi d'une requête FTP ? Préciser tous les détails pertinents.
1. Identifier avant chaque capture l'IP du client et l'IP du serveur.
1. Démarrer votre capture sur la bonne interface réseau.
1. Réaliser quelques requêtes FTP (avec envoi de fichier) :
 a. vers un serveur FTP distant (le vôtre configuré sur AlwaysData ou celui de dlptest)

4. Enregistrer la capture sous `captureFTP.pcapng`.
4. Filtrer les paquets FTP échangés

- Comment différencier les requêtes des réponses ?
- Combien de paires (requête et réponse) ont été échangées suite à votre action décrite en 1. ?

## Etape 5 - Analyser le trafic généré par un serveur SSH

On accèdera à votre serveur AlwaysData via le serveur SSH.

1. Quel type de client faut-il installer pour vous y connecter ? Installez-le !

1. Que fait-on pour provoquer l'envoi d'une requête SSH ? Préciser tous les détails pertinents.
1. Identifier avant chaque capture l'IP du client et l'IP du serveur.
1. Démarrer votre capture sur la bonne interface réseau.
1. Réaliser quelques requêtes SSH :
 a. vers un serveur SSH distant (le vôtre configuré sur AlwaysData)

4. Enregistrer la capture sous `captureSSH.pcapng`.
4. Filtrer les paquets SSH échangés

- Comment différencier les requêtes des réponses ?
- Combien de paires (requête et réponse) ont été échangées suite à votre action décrite en 1. ?

5. Que pouvez-vous noter de différent entre les serveurs SSH et FTP ?
