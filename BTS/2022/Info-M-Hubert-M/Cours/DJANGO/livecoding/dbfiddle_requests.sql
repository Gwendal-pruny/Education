-- Sélection simple de tous les champs d'une table
SELECT * FROM `stadium`;

-- Sélection d'un champ en particulier
SELECT `name` FROM `stadium`;

-- Sélection de plusieurs champs
SELECT `name`, `location` FROM `stadium`;

-- Sélection des matchs avec trois jointures
SELECT event.id, event.start, stadium.name, stadium.location, home.country AS `country_home`, away.country AS `country_away`
FROM `event`
INNER JOIN `stadium` ON `event`.`stadium_id` = `stadium`.`id`
LEFT JOIN `team` AS `home` ON `event`.`team_home_id` = `home`.`id`
LEFT JOIN `team` AS `away` ON `event`.`team_away_id` = `away`.`id`;

-- Tri des résultats d'une requête sur un champ
SELECT * FROM `stadium` ORDER BY `location`;

-- Tri dans l'ordre descendant (décroissant)
SELECT * FROM `stadium` ORDER BY `location` DESC;

-- Filtrage des résultats selon la valeur d'un champ
-- Pour rappel, on entoure les noms de table/cham par des backticks `` et on entour les valeurs par des ""
SELECT * FROM `stadium` WHERE `location`="Auckland";

-- Limiter les résultats à 3 entrées
SELECT * FROM `team` LIMIT 3;
-- Limiter les résultats à 3 entrées, en sautant les 3 premiers résultats (équivalent à une pagination)
SELECT * FROM `team` LIMIT 3 OFFSET 3;
