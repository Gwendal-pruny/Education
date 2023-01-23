
DROP TABLE IF EXISTS `categorie`;
CREATE TABLE IF NOT EXISTS `categorie` (
  `id` int(11) NOT NULL,
  `libelle` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `categorie`
--

INSERT INTO `categorie` (`id`, `libelle`) VALUES
(1, 'standard'),
(2, 'confort'),
(3, 'premium'),
(4, 'luxe');

-- --------------------------------------------------------

--
-- Structure de la table `chambre`
--

DROP TABLE IF EXISTS `chambre`;
CREATE TABLE IF NOT EXISTS `chambre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nbCouchage` int(11) NOT NULL,
  `porte` varchar(5) NOT NULL,
  `etage` varchar(5) NOT NULL,
  `idCategorie` int(11) NOT NULL,
  `baignoire` tinyint(1) NOT NULL,
  `prixBase` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idCategorie` (`idCategorie`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `chambre`
--

INSERT INTO `chambre` (`id`, `nbCouchage`, `porte`, `etage`, `idCategorie`, `baignoire`, `prixBase`) VALUES
(1, 2, 'A', '2', 1, 1, 60),
(2, 2, 'A', '2', 1, 1, 60),
(3, 2, 'A', '2', 1, 1, 60),
(4, 2, 'B', '2', 1, 0, 60),
(5, 2, 'A', '2', 1, 1, 60),
(6, 2, 'A', '2', 1, 1, 60),
(7, 2, 'A', '2', 1, 1, 60),
(8, 2, 'A', '2', 1, 1, 60),
(9, 2, 'C', '2', 1, 0, 60),
(10, 2, 'A', '2', 1, 1, 60),
(11, 2, 'A', '2', 1, 1, 60),
(12, 2, 'A', '2', 1, 1, 60),
(13, 2, 'D', '2', 1, 0, 60),
(14, 2, 'A', '2', 1, 0, 60),
(15, 2, 'A', '2', 1, 1, 60),
(16, 2, 'A', '2', 1, 1, 60),
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
(39, 2, 'K', '2', 1, 1, 75),
(40, 2, 'J', '2', 2, 1, 120),
(41, 2, 'A', '2', 2, 1, 130),
(42, 2, 'H', '2', 2, 1, 110),
(43, 2, 'C', '2', 2, 0, 175),
(44, 3, 'A', '2', 2, 1, 200),
(45, 4, 'R', '2', 2, 1, 180),
(46, 3, 'A', '2', 3, 1, 250),
(47, 5, 'D', '2', 3, 0, 240),
(48, 4, 'G', '2', 3, 0, 220),
(49, 3, 'C', '2', 3, 1, 220),
(50, 6, 'A', '2', 3, 1, 255),
(51, 4, 'E', '2', 3, 1, 230);

-- --------------------------------------------------------

--
-- Structure de la table `ligne_reservation`
--

DROP TABLE IF EXISTS `ligne_reservation`;
CREATE TABLE IF NOT EXISTS `ligne_reservation` (
  `idchambre` int(11) NOT NULL,
  `idreservation` int(11) NOT NULL,
  KEY `idchambre` (`idchambre`),
  KEY `idreservation` (`idreservation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `ligne_reservation`
--

INSERT INTO `ligne_reservation` (`idchambre`, `idreservation`) VALUES
(1, 1),
(2, 1),
(3, 2);

-- --------------------------------------------------------

--
-- Structure de la table `periode`
--

DROP TABLE IF EXISTS `periode`;
CREATE TABLE IF NOT EXISTS `periode` (
  `id` int(11) NOT NULL,
  `libelle` varchar(20) NOT NULL,
  `coefficient` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `periode`
--

INSERT INTO `periode` (`id`, `libelle`, `coefficient`) VALUES
(1, 'basse', 0.7),
(2, 'moyenne', 1),
(3, 'haute', 2);

-- --------------------------------------------------------

--
-- Structure de la table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
CREATE TABLE IF NOT EXISTS `reservation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dateD` date NOT NULL,
  `dateF` date NOT NULL,
  `idPeriode` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idPeriode` (`idPeriode`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `reservation`
--

INSERT INTO `reservation` (`id`, `dateD`, `dateF`, `idPeriode`) VALUES
(1, '2020-03-25', '2020-03-31', 2),
(2, '2020-04-09', '2020-04-16', 2);

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(60) NOT NULL,
  `nom` varchar(30) NOT NULL,
  `prenom` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`id`, `email`, `nom`, `prenom`) VALUES
(1, 'zorg@sio.fr', 'zorg', 'goz');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `chambre`
--
ALTER TABLE `chambre`
  ADD CONSTRAINT `chambre_ibfk_1` FOREIGN KEY (`idCategorie`) REFERENCES `categorie` (`id`);

--
-- Contraintes pour la table `ligne_reservation`
--
ALTER TABLE `ligne_reservation`
  ADD CONSTRAINT `ligne_reservation_ibfk_1` FOREIGN KEY (`idchambre`) REFERENCES `chambre` (`id`),
  ADD CONSTRAINT `ligne_reservation_ibfk_2` FOREIGN KEY (`idreservation`) REFERENCES `reservation` (`id`);

--
-- Contraintes pour la table `reservation`
--
ALTER TABLE `reservation`
  ADD CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`idPeriode`) REFERENCES `periode` (`id`);
COMMIT;

