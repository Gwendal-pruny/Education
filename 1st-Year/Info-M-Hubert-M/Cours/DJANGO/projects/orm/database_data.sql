INSERT INTO `mainapp_team` (`id`, `country`, `country_alpha2`, `nickname`, `color_first`, `color_second`) VALUES (1, 'Nouvelle-Zélande', 'nz', 'All Blacks', 'FFFFFF', '000000');
INSERT INTO `mainapp_team` (`id`, `country`, `country_alpha2`, `nickname`, `color_first`, `color_second`) VALUES (2, 'Russie', 'ru', 'Les Ours', 'FFFFFF', 'D52B1E');
INSERT INTO `mainapp_team` (`id`, `country`, `country_alpha2`, `nickname`, `color_first`, `color_second`) VALUES (3, 'Japon', 'jp', 'The Cherry Blossoms', 'FFFFFF', 'E70012');
INSERT INTO `mainapp_team` (`id`, `country`, `country_alpha2`, `nickname`, `color_first`, `color_second`) VALUES (4, 'Australie', 'au', 'Les Wallabies', 'FAD068', '8C6505');
INSERT INTO `mainapp_team` (`id`, `country`, `country_alpha2`, `nickname`, `color_first`, `color_second`) VALUES (5, 'Samoa', 'ws', 'Manu Samoa', '264282', '181A1B');
INSERT INTO `mainapp_team` (`id`, `country`, `country_alpha2`, `nickname`, `color_first`, `color_second`) VALUES (6, 'Afrique du Sud', 'za', 'Les Springboks', 'FFB300', '0C3D1B');
INSERT INTO `mainapp_team` (`id`, `country`, `country_alpha2`, `nickname`, `color_first`, `color_second`) VALUES (7, 'Tonga', 'to', 'Ikale Tahi', 'FF0000', '181A1B');
INSERT INTO `mainapp_team` (`id`, `country`, `country_alpha2`, `nickname`, `color_first`, `color_second`) VALUES (8, 'Fidji', 'fj', 'The Flying Fijians', 'FFFFFF', '99B7E8');

INSERT INTO `mainapp_stadium` (`id`, `name`, `location`, `latitude`, `longitude`) VALUES (1, 'Eden Park', 'Auckland', -36.875488, 174.744684);
INSERT INTO `mainapp_stadium` (`id`, `name`, `location`, `latitude`, `longitude`) VALUES (2, 'Sky Stadium', 'Wellington', -41.273002, 174.785872);
INSERT INTO `mainapp_stadium` (`id`, `name`, `location`, `latitude`, `longitude`) VALUES (3, 'Mt Smart Stadium', 'Auckland', -36.918429, 174.812345);
INSERT INTO `mainapp_stadium` (`id`, `name`, `location`, `latitude`, `longitude`) VALUES (4, 'FMG Stadium Waikato', 'Hamilton', -37.781670, 175.269632);

INSERT INTO `mainapp_event` (`id`, `start`, `stadium_id`, `team_away_id`, `team_home_id`) VALUES (1, '2022-07-02 19:30:00.000000', 1, 1, 2);
INSERT INTO `mainapp_event` (`id`, `start`, `stadium_id`, `team_away_id`, `team_home_id`) VALUES (2, '2022-07-03 19:30:00.000000', 3, 3, 4);
INSERT INTO `mainapp_event` (`id`, `start`, `stadium_id`, `team_away_id`, `team_home_id`) VALUES (3, '2022-07-05 19:00:00.000000', 2, 5, 6);
INSERT INTO `mainapp_event` (`id`, `start`, `stadium_id`, `team_away_id`, `team_home_id`) VALUES (4, '2022-07-06 19:30:00.000000', 4, 7, 8);
INSERT INTO `mainapp_event` (`id`, `start`, `stadium_id`, `team_away_id`, `team_home_id`) VALUES (5, '2022-07-09 19:30:00.000000', 3, NULL, NULL);
INSERT INTO `mainapp_event` (`id`, `start`, `stadium_id`, `team_away_id`, `team_home_id`) VALUES (6, '2022-07-10 19:30:00.000000', 3, NULL, NULL);
INSERT INTO `mainapp_event` (`id`, `start`, `stadium_id`, `team_away_id`, `team_home_id`) VALUES (7, '2022-07-12 18:30:00.000000', 3, NULL, NULL);
INSERT INTO `mainapp_event` (`id`, `start`, `stadium_id`, `team_away_id`, `team_home_id`) VALUES (8, '2022-07-12 20:00:00.000000', 1, NULL, NULL);

INSERT INTO `mainapp_ticket` (`id`, `event_id`, `category`, `seat`, `price`, `currency`) VALUES ('02f33283-ea69-4754-8fd0-cf4276227d79', 4, 'B', 'B-39', 6200, 'JPY');
INSERT INTO `mainapp_ticket` (`id`, `event_id`, `category`, `seat`, `price`, `currency`) VALUES ('035bc638-e2b2-49fa-81da-16625e800862', 7, 'B', 'B-53', 80, 'NZD');
INSERT INTO `mainapp_ticket` (`id`, `event_id`, `category`, `seat`, `price`, `currency`) VALUES ('3756421a-1cb9-443c-bd8b-85c4f542dddd', 4, 'C', 'free', 39, 'EUR');
INSERT INTO `mainapp_ticket` (`id`, `event_id`, `category`, `seat`, `price`, `currency`) VALUES ('385be3be-e762-4b2c-9396-a105fd59d001', 2, 'B', 'B-23', 80, 'NZD');
INSERT INTO `mainapp_ticket` (`id`, `event_id`, `category`, `seat`, `price`, `currency`) VALUES ('396aa8ff-1a49-4711-b3a6-8fbfb79c2c8a', 6, 'B', 'B-5', 48, 'EUR');
INSERT INTO `mainapp_ticket` (`id`, `event_id`, `category`, `seat`, `price`, `currency`) VALUES ('69c0cbd3-ad1d-4390-968c-3bc4839dff70', 7, 'A', 'A-18', 100, 'NZD');
INSERT INTO `mainapp_ticket` (`id`, `event_id`, `category`, `seat`, `price`, `currency`) VALUES ('6b153fab-408e-4998-b7df-009d6f57a948', 5, 'C', 'free', 65, 'NZD');
INSERT INTO `mainapp_ticket` (`id`, `event_id`, `category`, `seat`, `price`, `currency`) VALUES ('859d1c4a-41ef-49d1-bb5e-45d162c8c623', 2, 'A', 'A-12', 7800, 'JPY');
INSERT INTO `mainapp_ticket` (`id`, `event_id`, `category`, `seat`, `price`, `currency`) VALUES ('9b5d242f-9839-4f72-96d3-5c202f4a2c47', 5, 'A', 'A-15', 100, 'NZD');
INSERT INTO `mainapp_ticket` (`id`, `event_id`, `category`, `seat`, `price`, `currency`) VALUES ('a7e9f367-e90d-41ec-8db1-5f5ca84f3c77', 8, 'A', 'A-51', 60, 'EUR');
INSERT INTO `mainapp_ticket` (`id`, `event_id`, `category`, `seat`, `price`, `currency`) VALUES ('aa8c60f7-9c3d-4f95-8283-945d9262a366', 3, 'A', 'A-8', 7800, 'JPY');
INSERT INTO `mainapp_ticket` (`id`, `event_id`, `category`, `seat`, `price`, `currency`) VALUES ('b05aba93-3c7e-467c-8f61-25bc2660c1f7', 8, 'A', 'A-12', 7800, 'JPY');
INSERT INTO `mainapp_ticket` (`id`, `event_id`, `category`, `seat`, `price`, `currency`) VALUES ('b48e85a5-a506-4d52-a759-a1d52a7ee8a6', 6, 'B', 'B-4', 48, 'EUR');
INSERT INTO `mainapp_ticket` (`id`, `event_id`, `category`, `seat`, `price`, `currency`) VALUES ('b9504759-5c2f-4ac6-b61a-1bb6bada861d', 3, 'A', 'A-11', 60, 'EUR');
INSERT INTO `mainapp_ticket` (`id`, `event_id`, `category`, `seat`, `price`, `currency`) VALUES ('bd34f611-899d-4643-b893-6a576a5d95c2', 1, 'A', 'A-51', 60, 'EUR');
INSERT INTO `mainapp_ticket` (`id`, `event_id`, `category`, `seat`, `price`, `currency`) VALUES ('e98e7628-961d-4839-b03a-bec399348716', 1, 'C', 'free', 65, 'NZD');

INSERT INTO `mainapp_newsletter` (`email`, `name`, `consent`) VALUES ('seblebest@mail.dev', 'Sébastien CHANAL', 1);
INSERT INTO `mainapp_newsletter` (`email`, `name`, `consent`) VALUES ('guy@liguerugby.dev', 'Guy NODESS', 0);
