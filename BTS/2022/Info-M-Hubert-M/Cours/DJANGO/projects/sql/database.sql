/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour djangosql
CREATE DATABASE IF NOT EXISTS `djangosql` /*!40100 DEFAULT CHARACTER SET utf8mb3 */;
USE `djangosql`;

-- Listage de la structure de la table djangosql. event
CREATE TABLE IF NOT EXISTS `event` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `start` datetime(6) NOT NULL,
    `stadium_id` bigint(20) NOT NULL,
    `team_home_id` bigint(20) DEFAULT NULL,
    `team_away_id` bigint(20) DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `k_mainapp_stadium_id` (`stadium_id`),
    KEY `k_mainapp_team_home_id` (`team_home_id`),
    KEY `k_mainapp_team_away_id` (`team_away_id`),
    CONSTRAINT `fk_mainapp_stadium_id` FOREIGN KEY (`stadium_id`) REFERENCES `stadium` (`id`),
    CONSTRAINT `fk_mainapp_team_home_id` FOREIGN KEY (`team_home_id`) REFERENCES `team` (`id`),
    CONSTRAINT `fk_mainapp_team_away_id` FOREIGN KEY (`team_away_id`) REFERENCES `team` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3;

-- Listage des données de la table djangosql.event : ~8 rows (environ)
/*!40000 ALTER TABLE `event` DISABLE KEYS */;
INSERT INTO `event` (`id`, `start`, `stadium_id`, `team_away_id`, `team_home_id`) VALUES
	(1, '2022-07-02 19:30:00.000000', 1, 1, 2),
	(2, '2022-07-03 19:30:00.000000', 3, 3, 4),
	(3, '2022-07-05 19:00:00.000000', 2, 5, 6),
	(4, '2022-07-06 19:30:00.000000', 4, 7, 8),
	(5, '2022-07-09 19:30:00.000000', 3, NULL, NULL),
	(6, '2022-07-10 19:30:00.000000', 3, NULL, NULL),
	(7, '2022-07-12 18:30:00.000000', 3, NULL, NULL),
	(8, '2022-07-12 20:00:00.000000', 1, NULL, NULL);
/*!40000 ALTER TABLE `event` ENABLE KEYS */;

-- Listage de la structure de la table djangosql. stadium
CREATE TABLE IF NOT EXISTS `stadium` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `name` varchar(100) NOT NULL,
    `location` varchar(100) NOT NULL,
    `latitude` decimal(9,6) NOT NULL,
    `longitude` decimal(9,6) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;

-- Listage des données de la table djangosql.stadium : ~4 rows (environ)
/*!40000 ALTER TABLE `stadium` DISABLE KEYS */;
INSERT INTO `stadium` (`id`, `name`, `location`, `latitude`, `longitude`) VALUES
	(1, 'Eden Park', 'Auckland', -36.875488, 174.744684),
	(2, 'Sky Stadium', 'Wellington', -41.273002, 174.785872),
	(3, 'Mt Smart Stadium', 'Auckland', -36.918429, 174.812345),
	(4, 'FMG Stadium Waikato', 'Hamilton', -37.781670, 175.269632);
/*!40000 ALTER TABLE `stadium` ENABLE KEYS */;

-- Listage de la structure de la table djangosql. team
CREATE TABLE IF NOT EXISTS `team` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `country` varchar(100) NOT NULL,
    `country_alpha2` varchar(2) NOT NULL,
    `nickname` varchar(100) NOT NULL,
    `color_first` varchar(6) NOT NULL,
    `color_second` varchar(6) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;

-- Listage des données de la table djangosql.team : ~8 rows (environ)
/*!40000 ALTER TABLE `team` DISABLE KEYS */;
INSERT INTO `team` (`id`, `country`, `country_alpha2`, `nickname`, `color_first`, `color_second`) VALUES
	(1, 'Nouvelle-Zélande', 'nz', 'All Blacks', 'FFFFFF', '000000'),
	(2, 'Russie', 'ru', 'Les Ours', 'FFFFFF', 'D52B1E'),
	(3, 'Japon', 'jp', 'The Cherry Blossoms', 'FFFFFF', 'E70012'),
	(4, 'Australie', 'au', 'Les Wallabies', 'FAD068', '8C6505'),
	(5, 'Samoa', 'ws', 'Manu Samoa', '264282', '181A1B'),
	(6, 'Afrique du Sud', 'za', 'Les Springboks', 'FFB300', '0C3D1B'),
	(7, 'Tonga', 'to', 'Ikale Tahi', 'FF0000', '181A1B'),
	(8, 'Fidji', 'fj', 'The Flying Fijians', 'FFFFFF', '99B7E8');
/*!40000 ALTER TABLE `team` ENABLE KEYS */;

-- Listage de la structure de la table djangosql. ticket
CREATE TABLE IF NOT EXISTS `ticket` (
    `id` char(36) NOT NULL,
    `event_id` bigint(20) NOT NULL,
    `category` varchar(1) NOT NULL,
    `seat` longtext NOT NULL,
    `price` int(11) NOT NULL,
    `currency` varchar(3) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `k_mainapp_event_id` (`event_id`),
    CONSTRAINT `fk_mainapp_event_id` FOREIGN KEY (`event_id`) REFERENCES `event` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Listage des données de la table djangosql.ticket : ~16 rows (environ)
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
INSERT INTO `ticket` (`id`, `event_id`, `category`, `seat`, `price`, `currency`) VALUES
	('02f33283-ea69-4754-8fd0-cf4276227d79', 4, 'B', 'B-39', 6200, 'JPY'),
	('035bc638-e2b2-49fa-81da-16625e800862', 7, 'B', 'B-53', 80, 'NZD'),
	('3756421a-1cb9-443c-bd8b-85c4f542dddd', 4, 'C', 'free', 39, 'EUR'),
	('385be3be-e762-4b2c-9396-a105fd59d001', 2, 'B', 'B-23', 80, 'NZD'),
	('396aa8ff-1a49-4711-b3a6-8fbfb79c2c8a', 6, 'B', 'B-5', 48, 'EUR'),
	('69c0cbd3-ad1d-4390-968c-3bc4839dff70', 7, 'A', 'A-18', 100, 'NZD'),
	('6b153fab-408e-4998-b7df-009d6f57a948', 5, 'C', 'free', 65, 'NZD'),
	('859d1c4a-41ef-49d1-bb5e-45d162c8c623', 2, 'A', 'A-12', 7800, 'JPY'),
	('9b5d242f-9839-4f72-96d3-5c202f4a2c47', 5, 'A', 'A-15', 100, 'NZD'),
	('a7e9f367-e90d-41ec-8db1-5f5ca84f3c77', 8, 'A', 'A-51', 60, 'EUR'),
	('aa8c60f7-9c3d-4f95-8283-945d9262a366', 3, 'A', 'A-8', 7800, 'JPY'),
	('b05aba93-3c7e-467c-8f61-25bc2660c1f7', 8, 'A', 'A-12', 7800, 'JPY'),
	('b48e85a5-a506-4d52-a759-a1d52a7ee8a6', 6, 'B', 'B-4', 48, 'EUR'),
	('b9504759-5c2f-4ac6-b61a-1bb6bada861d', 3, 'A', 'A-11', 60, 'EUR'),
	('bd34f611-899d-4643-b893-6a576a5d95c2', 1, 'A', 'A-51', 60, 'EUR'),
	('e98e7628-961d-4839-b03a-bec399348716', 1, 'C', 'free', 65, 'NZD');
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;

-- Listage de la structure de la table djangosql. ticket
CREATE TABLE IF NOT EXISTS `newsletter` (
    `email` char(100) NOT NULL,
    `name` char(100) NOT NULL,
    `consent` boolean NOT NULL DEFAULT 0,
    PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

INSERT INTO `newsletter` (`email`, `name`, `consent`) VALUES
	('seblebest@mail.dev', 'Sébastien CHANAL', 1),
	('guy@liguerugby.dev', 'Guy NODESS', 0);

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
