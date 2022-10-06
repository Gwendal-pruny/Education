# CHEAT SHEET OWASP
#### [Gwendal PRUNY](mailto:gwendal.pruny@gmail.com), ESIEE-IT
#### Cours Système (BTS - SIO) - 14/10/2021


-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
 

#### Références 

- Site de référence : <https://owasp.org/>
	- TOP 10 : https://owasp.org/www-project-top-ten/
	- Sur Github en Fr : https://github.com/OWASP/Top10/blob/master/2021/docs/index.fr.md

- Vidéos : 
	- TOP 10 (2021) : <https://youtu.be/xe9LN2w7hfE>  
 	- TOP 10 (2017-2021) : <https://youtu.be/Q5KB2KrNzlA> et sa Playlist **explications des failles** : <https://youtube.com/playlist?list=PLr3lUE_48stofSVmN1y0KPiSGYDNxHRvE>



#### Analyse top 10 failles 

* Broken Access Control<details>

	Le contrôle d'accès applique une politique telle que les utilisateurs ne peuvent pas agir en dehors de leurs autorisations prévues. Les défaillances entraînent généralement la divulgation non autorisée d'informations, la modification ou la destruction de toutes les données ou l'exécution d'une fonction commerciale en dehors des limites de l'utilisateur. Les vulnérabilités courantes du contrôle d'accès incluent :
	Violation du principe du moindre privilège ou refus par défaut, où l'accès ne doit être accordé qu'à des capacités, des rôles ou des utilisateurs particuliers, mais est accessible à tous.
	Contourner les contrôles d'accès en modifiant l'URL (falsification des paramètres ou navigation forcée), l'état de l'application interne ou la page HTML, ou en utilisant un outil d'attaque modifiant les requêtes API.
	Autoriser l'affichage ou la modification du compte de quelqu'un d'autre, en fournissant son identifiant unique (références d'objet directes non sécurisées)
	Accès à l'API avec des contrôles d'accès manquants pour POST, PUT et DELETE.
	Élévation de privilège. Agir en tant qu'utilisateur sans être connecté ou agir en tant qu'administrateur lorsqu'il est connecté en tant qu'utilisateur.
	La manipulation des métadonnées, telle que la relecture ou la falsification d'un jeton de contrôle d'accès JSON Web Token (JWT), ou un cookie ou un champ masqué manipulé pour élever les privilèges ou abuser de l'invalidation JWT.
	Une mauvaise configuration CORS permet l'accès à l'API à partir d'origines non autorisées/non approuvées.
	Forcez la navigation vers des pages authentifiées en tant qu'utilisateur non authentifié ou vers des pages privilégiées en tant qu'utilisateur standard.


	Conseil :

		Le contrôle d'accès n'est efficace que dans le code côté serveur de confiance ou l'API sans serveur, où l'attaquant ne peut pas modifier la vérification du contrôle d'accès ou les métadonnées.
		Sauf pour les ressources publiques, refuser par défaut.
		Implémentez des mécanismes de contrôle d'accès une seule fois et réutilisez-les dans l'ensemble de l'application, notamment en minimisant l'utilisation du partage de ressources cross-origin (CORS).
		Les contrôles d'accès modèles doivent appliquer la propriété de l'enregistrement plutôt que d'accepter que l'utilisateur puisse créer, lire, mettre à jour ou supprimer n'importe quel enregistrement.
		Les exigences de limite commerciale d'application unique doivent être appliquées par les modèles de domaine.
		Désactivez la liste des répertoires du serveur Web et assurez-vous que les métadonnées des fichiers (par exemple, .git) et les fichiers de sauvegarde ne sont pas présents dans les racines Web.
		Enregistrez les échecs de contrôle d'accès, alertez les administrateurs le cas échéant (par exemple, les échecs répétés).
		Limitez le débit de l'API et de l'accès au contrôleur pour minimiser les dommages causés par les outils d'attaque automatisés.
		Les identifiants de session avec état doivent être invalidés sur le serveur après la déconnexion. Les jetons JWT sans état devraient plutôt être de courte durée afin que la fenêtre d'opportunité pour un attaquant soit minimisée. Pour les JWT de longue durée, il est fortement recommandé de suivre les normes OAuth pour révoquer l'accès.
		Les développeurs et le personnel d'assurance qualité doivent inclure une unité de contrôle d'accès fonctionnel et des tests d'intégration.
</details>
``En temps que développeur nous devons  suivre norme et instruction de sécurirations et détecter les potentiels erreur ou insécuriter avant même de les crée``

* Cryptographic Failures :
 <details>

	La première chose est de déterminer les besoins de protection des données en transit et au repos. Par exemple, les mots de passe, les numéros de carte de crédit, les dossiers médicaux, les informations personnelles et les secrets commerciaux nécessitent une protection supplémentaire, principalement si ces données relèvent des lois sur la confidentialité, par exemple le règlement général sur la protection des données (RGPD) de l'UE, ou des réglementations, par exemple la protection des données financières. comme la norme de sécurité des données PCI (PCI DSS). Pour toutes ces données :
	Des données sont-elles transmises en texte clair ? Cela concerne les protocoles tels que HTTP, SMTP, FTP utilisant également des mises à jour TLS comme STARTTLS. Le trafic Internet externe est dangereux. Vérifiez tout le trafic interne, par exemple entre les équilibreurs de charge, les serveurs Web ou les systèmes principaux.
	Des algorithmes ou protocoles cryptographiques anciens ou faibles sont-ils utilisés par défaut ou dans un code plus ancien ?
	Des clés de chiffrement par défaut sont-elles utilisées, des clés de chiffrement faibles sont-elles générées ou réutilisées, ou manque-t-il une gestion ou une rotation appropriée des clés ? Les clés de chiffrement sont-elles archivées dans les référentiels de code source ?
	Le cryptage n'est-il pas appliqué, par exemple, des directives de sécurité ou des en-têtes HTTP (navigateur) sont-ils manquants ?
	Le certificat de serveur reçu et la chaîne de confiance sont-ils correctement validés ?
	Les vecteurs d'initialisation sont-ils ignorés, réutilisés ou générés insuffisamment sécurisés pour le mode de fonctionnement cryptographique ? Un mode de fonctionnement non sécurisé tel que l'ECB est-il utilisé ? Le cryptage est-il utilisé lorsque le cryptage authentifié est plus approprié ?
	Les mots de passe sont-ils utilisés comme clés cryptographiques en l'absence d'une fonction de dérivation de la clé de base du mot de passe ?
	Le caractère aléatoire est-il utilisé à des fins cryptographiques qui n'ont pas été conçues pour répondre aux exigences cryptographiques ? Même si la fonction correcte est choisie, doit-elle être ensemencée par le développeur, et si ce n'est pas le cas, le développeur a-t-il écrasé la fonctionnalité d'amorçage forte intégrée avec une graine qui manque d'entropie/imprévisibilité suffisante ?
	Des fonctions de hachage obsolètes telles que MD5 ou SHA1 sont-elles utilisées, ou des fonctions de hachage non cryptographiques sont-elles utilisées lorsque des fonctions de hachage cryptographiques sont nécessaires ?
	Des méthodes de remplissage cryptographique obsolètes telles que PKCS numéro 1 v1.5 sont-elles utilisées ?
	Les messages d'erreur cryptographiques ou les informations de canal auxiliaire sont-ils exploitables, par exemple sous la forme d'attaques oracle de remplissage ?

	Conseils :

		Procédez comme suit, au minimum, et consultez les références :
		Classer les données traitées, stockées ou transmises par une application. Identifiez les données sensibles selon les lois sur la confidentialité, les exigences réglementaires ou les besoins de l'entreprise.
		Ne stockez pas de données sensibles inutilement. Jetez-le dès que possible ou utilisez la tokenisation conforme à la norme PCI DSS ou même la troncature. Les données non conservées ne peuvent pas être volées.
		Assurez-vous de chiffrer toutes les données sensibles au repos.
		S'assurer que des algorithmes, des protocoles et des clés standard à jour et solides sont en place ; utiliser une bonne gestion des clés.
		Chiffrez toutes les données en transit avec des protocoles sécurisés tels que TLS avec des chiffrements de confidentialité persistante (FS), la hiérarchisation des chiffrements par le serveur et des paramètres sécurisés. Appliquez le chiffrement à l'aide de directives telles que HTTP Strict Transport Security (HSTS).
		Désactivez la mise en cache pour les réponses contenant des données sensibles.
		Appliquer les contrôles de sécurité requis selon la classification des données.
		N'utilisez pas de protocoles hérités tels que FTP et SMTP pour le transport de données sensibles.
		Stockez les mots de passe à l'aide de fonctions de hachage adaptatives et salées fortes avec un facteur de travail (facteur de retard), comme Argon2, scrypt, bcrypt ou PBKDF2.
		Les vecteurs d'initialisation doivent être choisis en fonction du mode de fonctionnement. Pour de nombreux modes, cela signifie utiliser un CSPRNG (générateur de nombres pseudo-aléatoires cryptographiquement sécurisé). Pour les modes qui nécessitent un nonce, le vecteur d'initialisation (IV) n'a pas besoin d'un CSPRNG. Dans tous les cas, le IV ne doit jamais être utilisé deux fois pour une clé fixe.
		Utilisez toujours un cryptage authentifié au lieu d'un simple cryptage.
		Les clés doivent être générées cryptographiquement de manière aléatoire et stockées en mémoire sous forme de tableaux d'octets. Si un mot de passe est utilisé, il doit être converti en clé via une fonction de dérivation de clé de base de mot de passe appropriée.
		Assurez-vous que l'aléatoire cryptographique est utilisé le cas échéant et qu'il n'a pas été ensemencé de manière prévisible ou avec une faible entropie. La plupart des API modernes n'exigent pas que le développeur amorce le CSPRNG pour obtenir la sécurité.
		Évitez les fonctions cryptographiques obsolètes et les schémas de remplissage, tels que MD5, SHA1, PKCS numéro 1 v1.5 .
		Vérifier indépendamment l'efficacité de la configuration et des paramètres.
</details>
``En temps que développeur nous devons  suivre norme et instruction de sécurirations et détecter les potentiels erreur ou insécuriter avant même de les crée``

* Injection

<details>

	Une application est vulnérable aux attaques lorsque :
	Les données fournies par l'utilisateur ne sont pas validées, filtrées ou nettoyées par l'application.
	Les requêtes dynamiques ou les appels non paramétrés sans échappement contextuel sont utilisés directement dans l'interpréteur.
	Les données hostiles sont utilisées dans les paramètres de recherche de mappage objet-relationnel (ORM) pour extraire des enregistrements sensibles supplémentaires.
	Les données hostiles sont directement utilisées ou concaténées. Le SQL ou la commande contient la structure et les données malveillantes dans les requêtes dynamiques, les commandes ou les procédures stockées.
	Certaines des injections les plus courantes sont SQL, NoSQL, la commande OS, le mappage relationnel objet (ORM), LDAP et l'injection EL (Expression Language) ou OGNL (Object Graph Navigation Library). Le concept est identique chez tous les interprètes. L'examen du code source est la meilleure méthode pour détecter si les applications sont vulnérables aux injections. Le test automatisé de tous les paramètres, en-têtes, URL, cookies, entrées de données JSON, SOAP et XML est fortement encouragé. Les organisations peuvent inclure des outils de test de sécurité des applications statiques (SAST), dynamiques (DAST) et interactifs (IAST) dans le pipeline CI/CD pour identifier les failles d'injection introduites avant le déploiement en production.

	Conseils:

		Empêcher l'injection nécessite de séparer les données des commandes et des requêtes :
		L'option préférée consiste à utiliser une API sécurisée, qui évite d'utiliser entièrement l'interpréteur, fournit une interface paramétrée ou migre vers des outils de mappage relationnel objet (ORM).
		Remarque : même lorsqu'elles sont paramétrées, les procédures stockées peuvent toujours introduire une injection SQL si PL/SQL ou T-SQL concatène des requêtes et des données ou exécute des données hostiles avec EXECUTE IMMEDIATE ou exec().
		Utilisez la validation positive des entrées côté serveur. Ce n'est pas une défense complète car de nombreuses applications nécessitent des caractères spéciaux, tels que des zones de texte ou des API pour les applications mobiles.
		Pour toute requête dynamique résiduelle, échappez les caractères spéciaux à l'aide de la syntaxe d'échappement spécifique à cet interpréteur.
		Remarque : les structures SQL telles que les noms de table, les noms de colonne, etc. ne peuvent pas être échappées et les noms de structure fournis par l'utilisateur sont donc dangereux. Il s'agit d'un problème courant dans les logiciels de rédaction de rapports.
		Utilisez LIMIT et d'autres contrôles SQL dans les requêtes pour empêcher la divulgation massive d'enregistrements en cas d'injection SQL.
</details>
``En temps que développeur nous devons  suivre norme et instruction de sécurirations et détecter les potentiels erreur ou insécuriter avant même de les crée``
* Insecure Design
<details>


	La conception non sécurisée est une vaste catégorie représentant différentes faiblesses, exprimées comme « conception de contrôle manquante ou inefficace ». La conception non sécurisée n'est pas la source de toutes les autres catégories de risques du Top 10. Il y a une différence entre une conception non sécurisée et une implémentation non sécurisée. Nous différencions les défauts de conception et les défauts de mise en œuvre pour une raison, ils ont des causes profondes et des solutions différentes. Une conception sécurisée peut toujours présenter des défauts de mise en œuvre conduisant à des vulnérabilités susceptibles d'être exploitées. Une conception non sécurisée ne peut pas être corrigée par une implémentation parfaite car, par définition, les contrôles de sécurité nécessaires n'ont jamais été créés pour se défendre contre des attaques spécifiques. L'un des facteurs qui contribuent à une conception non sécurisée est le manque de profilage des risques commerciaux inhérent au logiciel ou au système en cours de développement, et donc l'incapacité à déterminer le niveau de conception de sécurité requis.
	Gestion des exigences et des ressources
	Recueillez et négociez les exigences commerciales pour une application avec l'entreprise, y compris les exigences de protection concernant la confidentialité, l'intégrité, la disponibilité et l'authenticité de tous les actifs de données et la logique commerciale attendue. Tenez compte du degré d'exposition de votre application et si vous avez besoin d'une séparation des locataires (en plus du contrôle d'accès). Compiler les exigences techniques, y compris les exigences de sécurité fonctionnelles et non fonctionnelles. Planifier et négocier le budget couvrant toutes les activités de conception, de construction, de test et d'exploitation, y compris les activités de sécurité.
	Conception sécurisée
	La conception sécurisée est une culture et une méthodologie qui évaluent en permanence les menaces et garantissent que le code est conçu et testé de manière robuste pour empêcher les méthodes d'attaque connues. La modélisation des menaces doit être intégrée dans les séances de perfectionnement (ou activités similaires) ; recherchez les changements dans les flux de données et le contrôle d'accès ou d'autres contrôles de sécurité. Dans le développement de la user story, déterminez le flux correct et les états d'échec, assurez-vous qu'ils sont bien compris et acceptés par les parties responsables et concernées. Analysez les hypothèses et les conditions des flux attendus et d'échec, assurez-vous qu'ils sont toujours précis et souhaitables. Déterminez comment valider les hypothèses et appliquer les conditions nécessaires pour des comportements appropriés. Assurez-vous que les résultats sont documentés dans la user story. Apprenez de vos erreurs et offrez des incitations positives pour promouvoir les améliorations. La conception sécurisée n'est ni un module complémentaire ni un outil que vous pouvez ajouter au logiciel.

	Conseils:
		Comment empêcher
		Établir et utiliser un cycle de vie de développement sécurisé avec des professionnels AppSec pour aider à évaluer et à concevoir des contrôles liés à la sécurité et à la confidentialité
		Établir et utiliser une bibliothèque de modèles de conception sécurisés ou de composants de routes pavées prêts à l'emploi
		Utilisez la modélisation des menaces pour l'authentification critique, le contrôle d'accès, la logique métier et les flux de clés
		Intégrer le langage et les contrôles de sécurité dans les user stories
		Intégrez des contrôles de plausibilité à chaque niveau de votre application (du frontend au backend)
		Rédiger des tests unitaires et d'intégration pour valider que tous les flux critiques résistent au modèle de menace. Compilez des cas d'utilisation et des cas d'utilisation abusive pour chaque niveau de votre application.
		Séparez les couches de niveau sur les couches système et réseau en fonction des besoins d'exposition et de protection
		Séparez solidement les locataires par conception à tous les niveaux
		Limiter la consommation de ressources par utilisateur ou service

</details>
``En temps que développeur nous devons  suivre norme et instruction de sécurirations et détecter les potentiels erreur ou insécuriter avant même de les crée``


* Security Misconfiguration
<details>

	Renforcement de la sécurité approprié manquant sur n'importe quelle partie de la pile d'applications ou autorisations mal configurées sur les services cloud.
	Des fonctionnalités inutiles sont activées ou installées (par exemple, des ports, des services, des pages, des comptes ou des privilèges inutiles).
	Les comptes par défaut et leurs mots de passe sont toujours activés et inchangés.
	La gestion des erreurs révèle des traces de pile ou d'autres messages d'erreur trop informatifs pour les utilisateurs.
	Pour les systèmes mis à niveau, les dernières fonctionnalités de sécurité sont désactivées ou ne sont pas configurées de manière sécurisée.
	Les paramètres de sécurité des serveurs d'applications, des frameworks d'applications (par exemple, Struts, Spring, ASP.NET), des bibliothèques, des bases de données, etc., ne sont pas définis sur des valeurs sécurisées.
	Le serveur n'envoie pas d'en-têtes ou de directives de sécurité, ou ils ne sont pas définis sur des valeurs sécurisées.
	Le logiciel est obsolète ou vulnérable (voir A06:2021-Composants vulnérables et obsolètes).
	Sans un processus de configuration de la sécurité des applications concerté et reproductible, les systèmes courent un risque plus élevé.

	Conseils:

		Des processus d'installation sécurisée doivent être mis en œuvre, notamment :
		Un processus de durcissement reproductible permet de déployer rapidement et facilement un autre environnement correctement verrouillé. Les environnements de développement, d'assurance qualité et de production doivent tous être configurés de manière identique, avec des informations d'identification différentes utilisées dans chaque environnement. Ce processus doit être automatisé afin de minimiser l'effort requis pour mettre en place un nouvel environnement sécurisé.
		Une plate-forme minimale sans fonctionnalités, composants, documentation et exemples inutiles. Supprimez ou n'installez pas les fonctionnalités et les frameworks inutilisés.
		Une tâche pour examiner et mettre à jour les configurations appropriées à toutes les notes de sécurité, mises à jour et correctifs dans le cadre du processus de gestion des correctifs (voir A06:2021-Composants vulnérables et obsolètes). Vérifiez les autorisations de stockage dans le cloud (par exemple, les autorisations de compartiment S3).
		Une architecture d'application segmentée fournit une séparation efficace et sécurisée entre les composants ou les locataires, avec la segmentation, la conteneurisation ou les groupes de sécurité cloud (ACL).
		Envoi de directives de sécurité aux clients, par exemple, des en-têtes de sécurité.
		Un processus automatisé pour vérifier l'efficacité des configurations et des paramètres dans tous les environnements.
	
</details>
``En temps que développeur nous devons  suivre norme et instruction de sécurirations et détecter les potentiels erreur ou insécuriter avant même de les crée``

* Vulnerable and Outdated Components
<details>
	Vous êtes probablement vulnérable :
	Si vous ne connaissez pas les versions de tous les composants que vous utilisez (côté client et côté serveur). Cela inclut les composants que vous utilisez directement ainsi que les dépendances imbriquées.
	Si le logiciel est vulnérable, non pris en charge ou obsolète. Cela inclut le système d'exploitation, le serveur Web/d'applications, le système de gestion de base de données (SGBD), les applications, les API et tous les composants, les environnements d'exécution et les bibliothèques.
	Si vous ne recherchez pas régulièrement les vulnérabilités et que vous vous abonnez aux bulletins de sécurité liés aux composants que vous utilisez.
	Si vous ne corrigez pas ou ne mettez pas à niveau la plate-forme sous-jacente, les infrastructures et les dépendances en temps opportun et en fonction des risques. Cela se produit généralement dans des environnements où l'application de correctifs est une tâche mensuelle ou trimestrielle sous contrôle des modifications, laissant les organisations ouvertes à des jours ou des mois d'exposition inutile à des vulnérabilités corrigées.
	Si les développeurs de logiciels ne testent pas la compatibilité des bibliothèques mises à jour, mises à niveau ou corrigées.
	Si vous ne sécurisez pas les configurations des composants (voir A05:2021-Security Misconfiguration).

	Conseils:

		Un processus de gestion des correctifs doit être en place pour :
		Supprimez les dépendances inutilisées, les fonctionnalités inutiles, les composants, les fichiers et la documentation.
		Inventorier en permanence les versions des composants côté client et côté serveur (par exemple, les frameworks, les bibliothèques) et leurs dépendances à l'aide d'outils tels que les versions, OWASP Dependency Check, retire.js, etc. Surveiller en permanence les sources telles que Common Vulnerability and Exposures (CVE) et National Vulnerability Database (NVD) pour les vulnérabilités des composants. Utilisez des outils logiciels d'analyse de la composition pour automatiser le processus. Abonnez-vous aux alertes par e-mail pour les vulnérabilités de sécurité liées aux composants que vous utilisez.
		N'obtenez des composants que de sources officielles via des liens sécurisés. Préférez les packages signés pour réduire le risque d'inclure un composant malveillant modifié (voir A08:2021-Software and Data Integrity Failures).
		Surveillez les bibliothèques et les composants qui ne sont pas maintenus ou qui ne créent pas de correctifs de sécurité pour les anciennes versions. Si le correctif n'est pas possible, envisagez de déployer un correctif virtuel pour surveiller, détecter ou vous protéger contre le problème découvert.
		Chaque organisation doit garantir un plan continu de surveillance, de triage et d'application des mises à jour ou des modifications de configuration pendant toute la durée de vie de l'application ou du portefeuille.

</details>
``En temps que développeur nous devons  suivre norme et instruction de sécurirations et détecter les potentiels erreur ou insécuriter avant même de les crée``

* Identification and Authentication Failures
<details>
	La confirmation de l'identité de l'utilisateur, l'authentification et la gestion de la session sont essentielles pour se protéger contre les attaques liées à l'authentification. Il peut y avoir des faiblesses d'authentification si l'application :
	Autorise les attaques automatisées telles que le credential stuffing, où l'attaquant dispose d'une liste de noms d'utilisateur et de mots de passe valides.
	Permet la force brute ou d'autres attaques automatisées.
	Autorise les mots de passe par défaut, faibles ou bien connus, tels que "Mot de passe1" ou "admin/admin".
	Utilise des processus de récupération d'informations d'identification faibles ou inefficaces et de mot de passe oublié, tels que les « réponses basées sur les connaissances », qui ne peuvent pas être sécurisées.
	Utilise des magasins de données de mots de passe en texte brut, cryptés ou faiblement hachés (voir A02:2021-Défaillances cryptographiques).
	A une authentification multifacteur manquante ou inefficace.
	Expose l'identifiant de session dans l'URL.
	Réutiliser l'identifiant de session après une connexion réussie.
	N'invalide pas correctement les identifiants de session. Les sessions utilisateur ou les jetons d'authentification (principalement les jetons d'authentification unique (SSO)) ne sont pas correctement invalidés lors de la déconnexion ou d'une période d'inactivité.

	Conseils:

		Comment empêcher
		Dans la mesure du possible, mettez en œuvre une authentification multifacteur pour empêcher le bourrage d'informations d'identification automatisé, la force brute et les attaques de réutilisation d'informations d'identification volées.
		N'expédiez pas ou ne déployez pas avec des informations d'identification par défaut, en particulier pour les utilisateurs administrateurs.
		Mettez en place des contrôles de mots de passe faibles, tels que le test des mots de passe nouveaux ou modifiés par rapport à la liste des 10 000 pires mots de passe.
		Alignez les politiques de longueur, de complexité et de rotation des mots de passe sur les directives 800-63b du National Institute of Standards and Technology (NIST) dans la section 5.1.1 pour les secrets mémorisés ou d'autres politiques de mot de passe modernes et fondées sur des preuves.
		Assurez-vous que l'enregistrement, la récupération des informations d'identification et les voies d'API sont renforcées contre les attaques d'énumération de compte en utilisant les mêmes messages pour tous les résultats.
		Limitez ou retardez de plus en plus les tentatives de connexion infructueuses, mais veillez à ne pas créer de scénario de déni de service. Enregistrez tous les échecs et alertez les administrateurs lorsque le bourrage d'informations d'identification, la force brute ou d'autres attaques sont détectées.
		Utilisez un gestionnaire de session intégré, sécurisé et côté serveur qui génère un nouvel ID de session aléatoire avec une entropie élevée après la connexion. L'identifiant de session ne doit pas figurer dans l'URL, être stocké en toute sécurité et invalidé après la déconnexion, l'inactivité et les délais d'expiration absolus.

</details>
``En temps que développeur nous devons  suivre norme et instruction de sécurirations et détecter les potentiels erreur ou insécuriter avant même de les crée``

* Software and Data Integrity Failures
<details>
	Les défaillances d'intégrité des logiciels et des données concernent le code et l'infrastructure qui ne protègent pas contre les violations d'intégrité. Un exemple de ceci est lorsqu'une application s'appuie sur des plugins, des bibliothèques ou des modules provenant de sources, de référentiels et de réseaux de diffusion de contenu (CDN) non fiables. Un pipeline CI/CD non sécurisé peut introduire un risque d'accès non autorisé, de code malveillant ou de compromission du système. Enfin, de nombreuses applications incluent désormais une fonctionnalité de mise à jour automatique, où les mises à jour sont téléchargées sans vérification d'intégrité suffisante et appliquées à l'application précédemment approuvée. Les attaquants pourraient potentiellement télécharger leurs propres mises à jour à distribuer et à exécuter sur toutes les installations. Un autre exemple est celui où des objets ou des données sont encodés ou sérialisés dans une structure qu'un attaquant peut voir et modifier est vulnérable à la désérialisation non sécurisée.

	Conseils:

		Utilisez des signatures numériques ou des mécanismes similaires pour vérifier que le logiciel ou les données proviennent de la source attendue et n'ont pas été modifiés.
		Assurez-vous que les bibliothèques et les dépendances, telles que npm ou Maven, consomment des référentiels approuvés. Si vous avez un profil de risque plus élevé, envisagez d'héberger un référentiel interne connu et approuvé.
		Assurez-vous qu'un outil de sécurité de la chaîne d'approvisionnement logicielle, tel que OWASP Dependency Check ou OWASP CycloneDX, est utilisé pour vérifier que les composants ne contiennent pas de vulnérabilités connues
		Assurez-vous qu'il existe un processus d'examen des modifications de code et de configuration afin de minimiser les risques d'introduction de code ou de configuration malveillants dans votre pipeline logiciel.
		Assurez-vous que votre pipeline CI/CD dispose d'une séparation, d'une configuration et d'un contrôle d'accès appropriés pour garantir l'intégrité du code circulant dans les processus de génération et de déploiement.
		Assurez-vous que les données sérialisées non signées ou non chiffrées ne sont pas envoyées à des clients non approuvés sans une certaine forme de contrôle d'intégrité ou de signature numérique pour détecter la falsification ou la relecture des données sérialisées

</details>
``En temps que développeur nous devons  suivre norme et instruction de sécurirations et détecter les potentiels erreur ou insécuriter avant même de les crée``

* Security Logging and Monitoring Failures
<details>

	Pour en revenir au Top 10 OWASP 2021, cette catégorie a pour but d'aider à détecter, escalader et répondre aux violations actives. Sans journalisation ni surveillance, les violations ne peuvent pas être détectées. Une journalisation, une détection, une surveillance et une réponse active insuffisantes se produisent à tout moment :
	Les événements auditables, tels que les connexions, les échecs de connexion et les transactions de grande valeur, ne sont pas consignés.
	Les avertissements et les erreurs génèrent des messages de journal inexistants, inadéquats ou peu clairs.
	Les journaux des applications et des API ne sont pas surveillés pour détecter toute activité suspecte.
	Les journaux ne sont stockés que localement.
	Les seuils d'alerte appropriés et les processus d'escalade des réponses ne sont pas en place ou efficaces.
	Les tests d'intrusion et les analyses par les outils de test dynamique de sécurité des applications (DAST) (tels que OWASP ZAP) ne déclenchent pas d'alertes.
	L'application ne peut pas détecter, escalader ou alerter des attaques actives en temps réel ou quasi réel.

	Conseils:

		Les développeurs doivent implémenter tout ou partie des contrôles suivants, selon le risque de l'application :
		Assurez-vous que tous les échecs de connexion, de contrôle d'accès et de validation des entrées côté serveur peuvent être consignés avec un contexte utilisateur suffisant pour identifier les comptes suspects ou malveillants et conservés pendant suffisamment de temps pour permettre une analyse médico-légale différée.
		Assurez-vous que les journaux sont générés dans un format facilement utilisable par les solutions de gestion des journaux.
		Assurez-vous que les données du journal sont correctement codées pour empêcher les injections ou les attaques sur les systèmes de journalisation ou de surveillance.
		Assurez-vous que les transactions de grande valeur disposent d'une piste d'audit avec des contrôles d'intégrité pour empêcher la falsification ou la suppression, telles que les tables de base de données à ajout uniquement ou similaires.
		Les équipes DevSecOps doivent mettre en place une surveillance et des alertes efficaces afin que les activités suspectes soient détectées et traitées rapidement.
		Établissez ou adoptez un plan de réponse aux incidents et de récupération, tel que National Institute of Standards and Technology (NIST) 800-61r2 ou ultérieur.
		Il existe des cadres de protection des applications commerciaux et open source tels que l'ensemble de règles de base OWASP ModSecurity et des logiciels de corrélation de journaux open source, tels que la pile Elasticsearch, Logstash, Kibana (ELK), qui comportent des tableaux de bord personnalisés et des alertes.

</details>
``En temps que développeur nous devons  suivre norme et instruction de sécurirations et détecter les potentiels erreur ou insécuriter avant même de les crée``

* Server-Side Request Forgery (SSRF)
<details>

	Les failles SSRF se produisent chaque fois qu'une application Web récupère une ressource distante sans valider l'URL fournie par l'utilisateur. Il permet à un attaquant de contraindre l'application à envoyer une requête spécialement conçue vers une destination inattendue, même lorsqu'elle est protégée par un pare-feu, un VPN ou un autre type de liste de contrôle d'accès (ACL) réseau.
	Comme les applications Web modernes offrent aux utilisateurs finaux des fonctionnalités pratiques, la récupération d'une URL devient un scénario courant. En conséquence, l'incidence de la SSRF augmente. De plus, la sévérité de SSRF est de plus en plus élevée en raison des services cloud et de la complexité des architectures.

	Conseils:

		Les développeurs peuvent empêcher SSRF en mettant en œuvre tout ou partie des contrôles de défense en profondeur suivants :
		Depuis la couche réseau
		Segmenter la fonctionnalité d'accès aux ressources à distance dans des réseaux séparés pour réduire l'impact de SSRF
		Appliquez des politiques de pare-feu de « refus par défaut » ou des règles de contrôle d'accès au réseau pour bloquer tout le trafic intranet, sauf le trafic essentiel.
		Conseils:
		~ Établissez une propriété et un cycle de vie pour les règles de pare-feu basées sur les applications.
		~ Enregistrez tous les flux réseau acceptés et bloqués sur les pare-feu (voir A09:2021-Security Logging and Monitoring Failures).

</details>
``En temps que développeur nous devons  suivre norme et instruction de sécurirations et détecter les potentiels erreur ou insécuriter avant même de les crée``





