CREATE TABLE IF NOT EXISTS player (
player_name VARCHAR(30) INT PRIMARY KEY,
player_id INT NULL,
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS personnage (
classes_id INT primary key,
PRIMARY KEY(player_name),
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO personnage VALUES
(1,"BANNED"),
(1,"St Brieure"),


-- QUESTION 1

CREATE TABLE IF NOT EXISTS armure (
armure_name VARCHAR(20) INT,
armure_rarity INT NULL,
armure_ilvl INT NULL,
armure_position int NULL,
races_id INT,
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- QUESTION 2

ALTER TABLE armure ADD FOREIGN KEY(idrace) REFERENCES race(id) ;

-- QUESTION 3

INSERT INTO armure VALUES
("Iron Chestplate",1,10,2,1),
("Diamond Chestplate",3,30,2,2),
 
 --

CREATE TABLE IF NOT EXISTS race (
races_mask INT NULL,
races_name VARCHAR(20) NULL,
races_side VARCHAR(8) NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8; 

-- QUESTION 4

DELETE FROM personnage WHERE player_name = ’BANNED’;

-- QUESTION 5

UPDATE armure SET armure_ilvl=15 WHERE armure_ilvl < 15;

-- QUESTION 6

SELECT armure_name FROM armure;

-- QUESTION 7

UPDATE armure SET armure_ilvl*1.1 WHERE armure_ilvl like `Za%`;

-- QUESTION 8

INSERT INTO player SELECT classe_id FROM personnage;

-- QUESTION 9

ALTER TABLE armure CHANGE armure_position idP TEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;
ALTER TABLE armure DROP nom;

