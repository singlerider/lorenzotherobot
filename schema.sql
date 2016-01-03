-- MySQL dump 10.13  Distrib 5.6.28, for Linux (x86_64)
--
-- Host: localhost    Database: twitchcurvyllama
-- ------------------------------------------------------
-- Server version	5.6.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `custom_commands`
--

DROP TABLE IF EXISTS `custom_commands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `custom_commands` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `channel` varchar(20) NOT NULL,
  `command` varchar(20) NOT NULL,
  `creator` varchar(20) NOT NULL,
  `user_level` varchar(10) NOT NULL,
  `time` datetime DEFAULT NULL,
  `response` varchar(200) NOT NULL,
  `times_used` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `evolutiontriggers`
--

DROP TABLE IF EXISTS `evolutiontriggers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `evolutiontriggers` (
  `id` int(4) unsigned NOT NULL AUTO_INCREMENT,
  `condition` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `items` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8 NOT NULL DEFAULT '',
  `value` int(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `channel` varchar(30) NOT NULL,
  `message` varchar(2000) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pokemon`
--

DROP TABLE IF EXISTS `pokemon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pokemon` (
  `id` int(4) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8 NOT NULL DEFAULT '',
  `type_primary` int(2) NOT NULL,
  `type_secondary` int(2) DEFAULT NULL,
  `rarity` tinyint(1) NOT NULL,
  `time` datetime DEFAULT NULL,
  `evolution_set` int(2) unsigned NOT NULL,
  `evolution_index` tinyint(1) unsigned NOT NULL,
  `evolution_level` tinyint(2) unsigned DEFAULT NULL,
  `evolution_trigger` int(4) unsigned NOT NULL,
  `hp_base` int(4) unsigned NOT NULL,
  `speed_base` int(4) unsigned NOT NULL,
  `attack_base` int(4) unsigned NOT NULL,
  `defense_base` int(4) unsigned NOT NULL,
  `special_attack_base` int(4) unsigned NOT NULL,
  `special_defense_base` int(4) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `type_primary` (`type_primary`),
  KEY `type_secondary` (`type_secondary`),
  KEY `evolution_trigger` (`evolution_trigger`),
  CONSTRAINT `pokemon_ibfk_1` FOREIGN KEY (`type_primary`) REFERENCES `types` (`id`),
  CONSTRAINT `pokemon_ibfk_2` FOREIGN KEY (`type_secondary`) REFERENCES `types` (`id`),
  CONSTRAINT `pokemon_ibfk_3` FOREIGN KEY (`evolution_trigger`) REFERENCES `evolutiontriggers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `quotes`
--

DROP TABLE IF EXISTS `quotes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `quotes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `channel` varchar(30) NOT NULL,
  `created_by` varchar(30) NOT NULL,
  `quote` varchar(2000) NOT NULL,
  `quote_number` int(11) NOT NULL,
  `game` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `types`
--

DROP TABLE IF EXISTS `types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `types` (
  `identifier` varchar(20) CHARACTER SET utf8 NOT NULL DEFAULT '',
  `id` int(2) NOT NULL,
  `1` float(3,1) unsigned NOT NULL,
  `2` float(2,1) unsigned NOT NULL,
  `3` float(2,1) unsigned NOT NULL,
  `4` float(2,1) unsigned NOT NULL,
  `5` float(2,1) unsigned NOT NULL,
  `6` float(2,1) unsigned NOT NULL,
  `7` float(2,1) unsigned NOT NULL,
  `8` float(2,1) unsigned NOT NULL,
  `9` float(2,1) unsigned NOT NULL,
  `10` float(2,1) unsigned NOT NULL,
  `11` float(2,1) unsigned NOT NULL,
  `12` float(2,1) unsigned NOT NULL,
  `13` float(2,1) unsigned NOT NULL,
  `14` float(2,1) unsigned NOT NULL,
  `15` float(2,1) unsigned NOT NULL,
  `16` float(2,1) unsigned NOT NULL,
  `17` float(2,1) unsigned NOT NULL,
  `18` float(2,1) unsigned NOT NULL,
  `10001` float(2,1) unsigned NOT NULL,
  `10002` float(2,1) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `identifier` (`identifier`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `useritems`
--

DROP TABLE IF EXISTS `useritems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `useritems` (
  `username` varchar(50) CHARACTER SET utf8 NOT NULL DEFAULT '',
  `item_id` int(11) unsigned NOT NULL,
  `quantity` tinyint(4) NOT NULL,
  PRIMARY KEY (`username`,`item_id`),
  KEY `item_id` (`item_id`),
  KEY `username` (`username`),
  CONSTRAINT `useritems_ibfk_1` FOREIGN KEY (`item_id`) REFERENCES `items` (`id`),
  CONSTRAINT `useritems_ibfk_2` FOREIGN KEY (`username`) REFERENCES `users` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `userpokemon`
--

DROP TABLE IF EXISTS `userpokemon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userpokemon` (
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `username` varchar(50) NOT NULL DEFAULT '',
  `donation_points` int(11) DEFAULT '0',
  `lastbattle` datetime DEFAULT CURRENT_TIMESTAMP,
  `wins` int(11) DEFAULT '0',
  `losses` int(11) DEFAULT '0',
  `time_in_chat` int(11) DEFAULT '0',
  `time_points` int(11) DEFAULT '0',
  PRIMARY KEY (`username`),
  KEY `treats` (`donation_points`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-01-03  8:05:08
