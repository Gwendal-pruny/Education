CREATE TABLE `stadium` (
	`id` BIGINT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(100) NOT NULL,
	`location` VARCHAR(100) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `team` (
	`id` BIGINT NOT NULL AUTO_INCREMENT,
	`country` VARCHAR(100) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `event` (
	`id` BIGINT NOT NULL AUTO_INCREMENT,
	`start` DATETIME NOT NULL,
	`stadium_id` BIGINT NOT NULL,
	`team_home_id` BIGINT,
	`team_away_id` BIGINT,
	PRIMARY KEY (`id`),
	KEY (`stadium_id`),
	CONSTRAINT `fk_stadium_id` FOREIGN KEY (`stadium_id`) REFERENCES `stadium` (id),
	KEY (`team_home_id`),
	CONSTRAINT `fk_team_home_id` FOREIGN KEY (`team_home_id`) REFERENCES `team` (id),
	KEY (`team_away_id`),
	CONSTRAINT `fk_team_away_id` FOREIGN KEY (`team_away_id`) REFERENCES `team` (id)
);

INSERT INTO `team` (country) VALUES ("Angleterre"), ("Fidji"), ("Japon"), ("Samoa"), ("Australie"), ("Tonga"), ("Nouvelle-Zélande"), ("Afrique du Sud");
INSERT INTO `stadium` (name, location) VALUES ("Ajinomoto Stadium", "Tokyo"), ("Toyota Stadium", "Tokyo"), ("Noevir Stadium Kobe", "Kobe"), ("Best Denki Stadium", "Fukuoka");
INSERT INTO `event` (start, stadium_id, team_home_id, team_away_id)
VALUES
('2022-07-12 19:30:00', 1, 1, 2),
('2022-07-13 19:30:00', 1, 3, 4),
('2022-07-14 19:00:00', 2, 5, 6),
('2022-07-15 19:30:00', 2, 7, 8),
('2022-07-18 19:30:00', 3, NULL, NULL),
('2022-07-20 19:30:00', 4, NULL, NULL),
('2022-07-22 18:30:00', 3, NULL, NULL),
('2022-07-22 20:00:00', 4, NULL, NULL);
