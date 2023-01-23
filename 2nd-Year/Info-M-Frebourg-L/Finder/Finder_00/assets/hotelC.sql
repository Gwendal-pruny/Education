DROP TABLE IF EXISTS `categorie`;
CREATE TABLE IF NOT EXISTS `categorie` (
  `id` integer NOT NULL,
  `libelle` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
);



INSERT INTO `categorie` (`id`, `libelle`) VALUES
(1, 'standard'),
(2, 'confort'),
(3, 'premium');


DROP TABLE IF EXISTS `chambre`;
CREATE TABLE IF NOT EXISTS `chambre` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `nbCouchage` integer NOT NULL,
  `porte` varchar(5) NOT NULL,
  `etage` varchar(5) NOT NULL,
  `idCategorie` integer NOT NULL,
  `baignoire` tinyint(1) NOT NULL,
  `prixBase` double NOT NULL,
  FOREIGN KEY (`idCategorie`) REFERENCES `categorie` (`id`)
) ;



INSERT INTO `chambre` (`id`, `nbCouchage`, `porte`, `etage`, `idCategorie`, `baignoire`, `prixBase`) VALUES
(1, 2, 'G', '2', 1, 1, 62),
(2, 2, 'G', '2', 1, 1, 62),
(3, 2, 'G', '2', 1, 1, 62),
(4, 2, 'B', '2', 1, 0, 62),
(5, 2, 'G', '2', 1, 1, 62),
(6, 2, 'G', '2', 1, 1, 62),
(7, 2, 'G', '2', 1, 1, 62),
(8, 2, 'G', '2', 1, 1, 62),
(9, 2, 'C', '2', 1, 0, 60),
(10, 2, 'A', '2', 1, 1, 62),
(11, 2, 'G', '2', 1, 1, 62),
(12, 2, 'A', '2', 1, 1, 60),
(13, 2, 'D', '2', 1, 0, 60),
(14, 2, 'G', '2', 1, 0, 62),
(15, 2, 'A', '2', 1, 1, 60),
(16, 2, 'G', '2', 1, 1, 60),
(17, 2, 'A', '2', 1, 1, 60),
(18, 2, 'Z', '2', 1, 1, 60),
(19, 2, 'N', '2', 1, 1, 60),
(20, 2, 'A', '2', 1, 1, 70),
(21, 2, 'M', '2', 1, 0, 72),
(22, 2, 'K', '2', 1, 1, 75),
(23, 2, 'J', '2', 1, 1, 80),
(24, 2, 'A', '2', 1, 1, 70),
(25, 2, 'H', '2', 1, 1, 80),
(26, 2, 'C', '2', 1, 0, 150),
(27, 3, 'A', '2', 1, 1, 160),
(28, 4, 'R', '2', 1, 1, 135),
(29, 3, 'A', '2', 1, 1, 150),
(30, 5, 'D', '2', 1, 0, 140),
(31, 4, 'G', '2', 1, 0, 120),
(32, 3, 'C', '2', 1, 1, 120),
(33, 6, 'A', '2', 1, 1, 155),
(34, 4, 'E', '2', 1, 1, 130),
(35, 2, 'Z', '2', 1, 1, 60),
(36, 2, 'N', '2', 1, 1, 60),
(37, 2, 'A', '2', 1, 1, 70),
(38, 2, 'M', '2', 1, 0, 72),
(39, 2, 'N', '2', 1, 1, 74),
(40, 2, 'J', '2', 2, 1, 120),
(41, 2, 'A', '2', 2, 1, 130),
(42, 2, 'H', '2', 2, 1, 110),
(43, 2, 'N', '2', 2, 0, 165),
(44, 3, 'N', '2', 2, 1, 200),
(45, 4, 'R', '2', 2, 1, 180),
(46, 3, 'A', '2', 3, 1, 250),
(47, 5, 'D', '2', 3, 0, 240),
(48, 4, 'G', '2', 3, 0, 220),
(49, 3, 'C', '2', 3, 1, 220),
(50, 6, 'A', '2', 3, 1, 255),
(51, 4, 'E', '2', 3, 1, 230);

DROP TABLE IF EXISTS `periode`;
CREATE TABLE IF NOT EXISTS `periode` (
  `id` integer NOT NULL,
  `libelle` varchar(20) NOT NULL,
  `coefficient` double NOT NULL,
  PRIMARY KEY (`id`)
) ;



INSERT INTO `periode` (`id`, `libelle`, `coefficient`) VALUES
(1, 'basse', 0.7),
(2, 'normal', 1),
(3, 'intense', 2);

DROP TABLE IF EXISTS `reservation`;
CREATE TABLE IF NOT EXISTS `reservation` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `dateD` date NOT NULL,
  `dateF` date NOT NULL,
  `idPeriode` integer NOT NULL,
  FOREIGN KEY (`idPeriode`) REFERENCES `periode` (`id`)
) ;


INSERT INTO `reservation` (`id`, `dateD`, `dateF`, `idPeriode`) VALUES
(1, '2020-03-25', '2020-03-31', 2),
(2, '2020-04-09', '2020-04-16', 2);


DROP TABLE IF EXISTS `ligne_reservation`;
CREATE TABLE IF NOT EXISTS `ligne_reservation` (
  `idchambre` integer NOT NULL,
  `idreservation` integer NOT NULL,
   FOREIGN KEY (`idchambre`) REFERENCES `chambre` (`id`),
 FOREIGN KEY (`idreservation`) REFERENCES `reservation` (`id`)) ;


INSERT INTO `ligne_reservation` (`idchambre`, `idreservation`) VALUES
(1, 1),
(2, 1),
(3, 2);



DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `email` varchar(60) NOT NULL,
  `nom` varchar(30) NOT NULL,
  `prenom` varchar(30) NOT NULL
) ;


INSERT INTO `user` (`id`, `email`, `nom`, `prenom`) VALUES
(1, 'zorg@sio.fr', 'zorg', 'goz');
