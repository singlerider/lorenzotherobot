import warnings

import globals
import MySQLdb as mdb


def get_connection():
    login = globals.mysql_credentials
    con = mdb.connect(login[0], login[1], login[2], login[3])
    return con


def initialize():
    con = get_connection()
    with con:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            cur = con.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS `users` (
                  `username` varchar(50) NOT NULL DEFAULT '',
                  `lastbattle` datetime DEFAULT '2016-01-01 21:00:00',
                  `wins` int(11) DEFAULT '0',
                  `losses` int(11) DEFAULT '0',
                  `time_in_chat` int(11) DEFAULT '0',
                  `points` int(11) DEFAULT '0',
                  PRIMARY KEY (`username`),
                  KEY `treats` (`points`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8
                """)
            cur.close()
            cur = con.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS `custom_commands` (
                  `id` int(11) NOT NULL AUTO_INCREMENT,
                  `channel` varchar(20) NOT NULL,
                  `command` varchar(20) NOT NULL,
                  `creator` varchar(20) NOT NULL,
                  `user_level` varchar(10) NOT NULL,
                  `time` datetime DEFAULT NULL,
                  `response` varchar(200) NOT NULL,
                  `times_used` int(11) NOT NULL DEFAULT '0',
                  PRIMARY KEY (`id`)
                ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1
                """)
            cur.close()
            cur = con.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS `messages` (
                  `id` int(11) NOT NULL AUTO_INCREMENT,
                  `username` varchar(30) NOT NULL,
                  `channel` varchar(30) NOT NULL,
                  `message` varchar(2000) NOT NULL,
                  `time` datetime DEFAULT NULL,
                  `uploaded` bool NOT NULL DEFAULT false,
                  PRIMARY KEY (`id`)
                ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8
                """)
            cur.close()
            cur = con.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS `quotes` (
                  `id` int(11) NOT NULL AUTO_INCREMENT,
                  `channel` varchar(30) NOT NULL,
                  `created_by` varchar(30) NOT NULL,
                  `quote` varchar(2000) NOT NULL,
                  `quote_number` int(11) NOT NULL,
                  `game` varchar(100) NOT NULL,
                  PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=latin1
                """)
            cur.close()
            cur = con.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS `useritems` (
                  `username` varchar(50) CHARACTER SET utf8 NOT NULL DEFAULT '',
                  `item_id` int(11) unsigned NOT NULL,
                  `quantity` tinyint(4) NOT NULL,
                  PRIMARY KEY (`username`,`item_id`),
                  KEY `item_id` (`item_id`),
                  KEY `username` (`username`),
                  CONSTRAINT `useritems_ibfk_1` FOREIGN KEY (`item_id`) REFERENCES `items` (`id`),
                  CONSTRAINT `useritems_ibfk_2` FOREIGN KEY (`username`) REFERENCES `users` (`username`)
                ) ENGINE=InnoDB DEFAULT CHARSET=latin1
                """)
            cur.close()
            cur = con.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS `userpokemon` (
                  `username` varchar(50) CHARACTER SET utf8 NOT NULL DEFAULT '',
                  `caught_by` varchar(50) CHARACTER SET utf8 NOT NULL DEFAULT '',
                  `position` tinyint(1) NOT NULL,
                  `pokemon_id` int(4) unsigned NOT NULL,
                  `nickname` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
                  `level` int(3) NOT NULL,
                  `for_trade` tinyint(1) DEFAULT NULL,
                  `time_trade_set` datetime DEFAULT '2011-01-26 14:30:00',
                  `for_sale` tinyint(1) DEFAULT NULL,
                  `time_sale_set` datetime DEFAULT '2011-01-26 14:30:00',
                  `asking_price` int(11) DEFAULT NULL,
                  `asking_trade` int(4) unsigned DEFAULT NULL,
                  `asking_level` int(3) DEFAULT NULL,
                  PRIMARY KEY (`username`,`position`),
                  KEY `pokemon_id` (`pokemon_id`),
                  KEY `asking_trade` (`asking_trade`),
                  CONSTRAINT `userpokemon_ibfk_1` FOREIGN KEY (`pokemon_id`) REFERENCES `pokemon` (`id`),
                  CONSTRAINT `userpokemon_ibfk_2` FOREIGN KEY (`username`) REFERENCES `users` (`username`),
                  CONSTRAINT `userpokemon_ibfk_3` FOREIGN KEY (`asking_trade`) REFERENCES `pokemon` (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=latin1
                """)
            cur.close()
            cur = con.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS `moderators` (
                    `id` int(11) NOT NULL AUTO_INCREMENT,
                    `username` VARCHAR(50) NOT NULL,
                    `channel` VARCHAR(50),
                    PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8
                """)
            cur.close()
            cur = con.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS `auth` (
                    `id` int(11) NOT NULL AUTO_INCREMENT,
                    `channel` VARCHAR(50) NOT NULL UNIQUE,
                    `twitch_oauth` VARCHAR(50),
                    `twitchalerts_oauth` VARCHAR(50 ),
                    `streamtip_oauth` VARCHAR(50),
                    PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8
                """)
            cur.close()
            cur = con.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS `market` (
                    `id` int(11) NOT NULL AUTO_INCREMENT,
                    `pokemon_id` INT(11) NOT NULL,
                    `price` INT(11) NOT NULL,
                    `time` datetime DEFAULT NULL,
                    PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8
                """)
            cur.close()
            cur = con.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS `blacklist` (
                    `id` int(11) NOT NULL AUTO_INCREMENT,
                    `username` VARCHAR(50) NOT NULL,
                    PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8
                """)
            cur.close()

initialize()
