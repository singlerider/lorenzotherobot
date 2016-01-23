-- MySQL dump 10.13  Distrib 5.6.28, for Linux (x86_64)
--
-- Host: localhost    Database: twitch
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
) ENGINE=InnoDB AUTO_INCREMENT=252 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pokemon`
--

LOCK TABLES `pokemon` WRITE;
/*!40000 ALTER TABLE `pokemon` DISABLE KEYS */;
INSERT INTO `pokemon` VALUES (0,'Missingno',1,3,0,NULL,0,0,NULL,0,100,70,120,90,70,120),(1,'Bulbasaur',12,4,2,NULL,1,1,16,0,45,45,49,49,65,65),(2,'Ivysaur',12,4,1,NULL,1,2,32,0,60,60,62,63,80,80),(3,'Venusaur',12,4,0,NULL,1,3,NULL,0,80,80,82,83,100,100),(4,'Charmander',10,NULL,2,NULL,2,1,16,0,39,65,52,43,60,50),(5,'Charmeleon',10,NULL,1,NULL,2,2,32,0,58,80,64,58,80,65),(6,'Charizard',10,3,0,NULL,2,3,NULL,0,78,100,84,78,109,85),(7,'Squirtle',11,NULL,2,NULL,3,1,16,0,44,43,48,65,50,64),(8,'Wartortle',11,NULL,1,NULL,3,2,32,0,59,58,63,80,65,80),(9,'Blastoise',11,NULL,0,NULL,3,3,NULL,0,79,78,83,100,85,105),(10,'Caterpie',7,NULL,3,NULL,4,1,7,0,45,45,30,35,20,20),(11,'Metapod',7,NULL,3,NULL,4,2,11,0,50,30,20,55,25,25),(12,'Butterfree',7,3,1,NULL,4,3,NULL,0,60,70,45,50,90,80),(13,'Weedle',7,4,3,NULL,5,1,7,0,40,50,35,30,20,20),(14,'Kakuna',7,4,3,NULL,5,2,10,0,45,35,25,50,25,25),(15,'Beedrill',7,4,2,NULL,5,3,NULL,0,65,75,90,40,45,80),(16,'Pidgey',1,3,3,NULL,6,1,18,0,40,56,45,40,35,35),(17,'Pidgeotto',1,3,2,NULL,6,2,36,0,63,71,60,55,50,50),(18,'Pidgeot',1,3,1,NULL,6,3,NULL,0,83,101,80,75,70,70),(19,'Rattata',1,NULL,3,NULL,7,1,20,0,30,72,56,35,25,35),(20,'Raticate',1,NULL,2,NULL,7,2,NULL,0,55,97,81,60,50,70),(21,'Spearow',1,3,3,NULL,8,1,20,0,40,70,60,30,31,31),(22,'Fearow',1,3,1,NULL,8,2,NULL,0,65,100,90,65,61,61),(23,'Ekans',4,NULL,3,NULL,9,1,22,0,35,55,60,44,40,54),(24,'Arbok',4,NULL,3,NULL,9,2,NULL,0,60,80,85,69,65,79),(25,'Pikachu',13,NULL,2,NULL,10,1,NULL,0,35,90,55,40,50,50),(26,'Raichu',13,NULL,0,NULL,10,2,NULL,3,60,110,90,55,90,80),(27,'Sandshrew',5,NULL,3,NULL,11,1,22,0,50,40,75,85,20,30),(28,'Sandslash',5,NULL,2,NULL,11,2,NULL,0,75,65,100,110,45,55),(29,'Nidoran Female',4,NULL,3,NULL,12,1,16,0,55,41,47,52,40,40),(30,'Nidorina',4,NULL,2,NULL,12,2,NULL,0,70,56,62,67,55,55),(31,'Nidoqueen',4,5,0,NULL,12,3,NULL,5,90,76,92,87,75,85),(32,'Nidoran Male',4,NULL,3,NULL,13,1,16,0,46,50,57,40,40,40),(33,'Nidorino',4,NULL,2,NULL,13,2,NULL,0,61,65,72,57,55,55),(34,'Nidoking',4,5,0,NULL,13,3,NULL,5,81,85,102,77,85,75),(35,'Clefairy',18,NULL,1,NULL,14,1,NULL,0,70,35,45,48,60,65),(36,'Clefable',18,NULL,0,NULL,14,2,NULL,5,95,60,70,73,95,90),(37,'Vulpix',10,NULL,3,NULL,15,1,NULL,0,38,65,41,40,50,65),(38,'Ninetales',10,NULL,1,NULL,15,2,NULL,1,73,100,76,75,81,100),(39,'Jigglypuff',1,18,1,NULL,16,1,NULL,0,115,20,45,20,45,25),(40,'Wigglytuff',1,18,0,NULL,16,2,NULL,5,140,45,70,45,85,50),(41,'Zubat',4,3,3,NULL,17,1,22,0,40,55,45,35,30,40),(42,'Golbat',4,3,2,NULL,17,2,NULL,0,75,90,80,70,65,75),(43,'Oddish',12,4,3,NULL,18,1,21,0,45,30,50,55,75,65),(44,'Gloom',12,4,2,NULL,18,2,NULL,0,60,40,65,70,85,75),(45,'Vileplume',12,4,1,NULL,18,3,NULL,0,75,50,80,85,110,90),(46,'Paras',7,12,3,NULL,19,1,24,0,35,25,70,55,45,55),(47,'Parasect',7,12,2,NULL,19,2,NULL,0,60,30,95,80,60,80),(48,'Venonat',7,4,3,NULL,20,1,31,0,60,45,55,50,40,55),(49,'Venomoth',7,4,2,NULL,20,2,NULL,0,70,90,65,60,90,75),(50,'Diglett',5,NULL,3,NULL,21,1,26,0,10,95,55,25,35,45),(51,'Dugtrio',5,NULL,2,NULL,21,2,NULL,0,35,120,80,50,50,70),(52,'Meowth',1,NULL,3,NULL,22,1,28,0,40,90,45,35,40,40),(53,'Persian',1,NULL,2,NULL,22,2,NULL,0,65,115,70,60,65,65),(54,'Psyduck',11,NULL,3,NULL,23,1,33,0,50,55,52,48,65,50),(55,'Golduck',11,NULL,3,NULL,23,2,NULL,0,80,85,82,78,95,80),(56,'Mankey',2,NULL,3,NULL,24,1,28,0,40,70,80,35,35,45),(57,'Primeape',2,NULL,2,NULL,24,2,NULL,0,65,95,105,60,60,70),(58,'Growlithe',10,NULL,2,NULL,25,1,NULL,0,55,60,70,45,70,50),(59,'Arcanine',10,NULL,1,NULL,25,2,NULL,1,90,95,110,80,100,80),(60,'Poliwag',11,NULL,3,NULL,26,1,25,0,40,90,50,40,40,40),(61,'Poliwhirl',11,NULL,2,NULL,26,2,NULL,0,65,90,65,65,50,50),(62,'Poliwrath',11,2,0,NULL,26,3,NULL,2,90,70,95,95,70,90),(63,'Abra',14,NULL,3,NULL,27,1,16,0,25,90,20,15,105,55),(64,'Kadabra',14,NULL,1,NULL,27,2,NULL,0,40,105,35,30,120,70),(65,'Alakazam',14,NULL,0,NULL,27,3,NULL,20,55,120,50,45,135,95),(66,'Machop',2,NULL,3,NULL,28,1,28,0,70,35,80,50,35,35),(67,'Machoke',2,NULL,2,NULL,28,2,NULL,0,80,45,100,70,50,60),(68,'Machamp',2,NULL,0,NULL,28,3,NULL,20,90,55,130,80,65,85),(69,'Bellsprout',12,4,3,NULL,29,1,21,0,50,40,75,35,70,30),(70,'Weepinbell',12,4,2,NULL,29,2,NULL,4,65,55,90,50,85,45),(71,'Victreebel',12,4,0,NULL,29,3,NULL,0,80,70,105,65,100,70),(72,'Tentacool',11,4,3,NULL,30,1,30,0,40,70,40,35,50,100),(73,'Tentacruel',11,4,2,NULL,30,2,NULL,0,80,100,70,65,80,120),(74,'Geodude',6,5,3,NULL,31,1,25,0,40,20,80,100,30,30),(75,'Graveler',6,5,2,NULL,31,2,NULL,0,55,35,95,115,45,45),(76,'Golem',6,5,0,NULL,31,3,NULL,20,80,45,120,130,55,65),(77,'Ponyta',10,NULL,3,NULL,32,1,40,0,50,90,85,55,65,65),(78,'Rapidash',10,NULL,2,NULL,32,2,NULL,0,65,105,100,70,80,80),(79,'Slowpoke',11,14,3,NULL,33,1,37,0,90,15,65,65,40,40),(80,'Slowbro',11,14,0,NULL,33,2,NULL,0,95,30,75,110,100,80),(81,'Magnemite',13,9,3,NULL,34,1,30,0,25,45,35,70,95,55),(82,'Magneton',13,9,2,NULL,34,2,NULL,0,50,70,60,95,120,70),(83,'Farfetch\'d',1,3,1,NULL,0,0,NULL,0,52,60,65,55,58,62),(84,'Doduo',1,3,3,NULL,35,1,31,0,35,75,85,45,35,35),(85,'Dodrio',1,3,2,NULL,35,2,NULL,0,60,100,110,70,60,60),(86,'Seel',11,NULL,3,NULL,36,1,34,0,65,45,45,55,45,70),(87,'Dewgong',11,15,2,NULL,36,2,NULL,0,90,70,70,80,70,95),(88,'Grimer',4,NULL,3,NULL,37,1,38,0,80,25,80,50,40,50),(89,'Muk',4,NULL,2,NULL,37,2,NULL,0,105,50,105,75,65,100),(90,'Shellder',11,NULL,3,NULL,38,1,NULL,0,30,40,65,100,45,25),(91,'Cloyster',11,15,2,NULL,38,2,NULL,2,50,70,95,180,85,45),(92,'Gastly',8,4,2,NULL,39,1,25,0,30,80,35,30,100,35),(93,'Haunter',8,4,1,NULL,39,2,NULL,0,45,95,50,45,115,55),(94,'Gengar',8,4,0,NULL,39,3,NULL,20,60,110,65,60,130,75),(95,'Onix',6,5,2,NULL,0,0,NULL,0,35,70,45,160,30,45),(96,'Drowzee',14,NULL,2,NULL,40,1,26,0,60,42,48,45,43,90),(97,'Hypno',14,NULL,1,NULL,40,2,NULL,0,85,67,73,70,73,115),(98,'Krabby',11,NULL,3,NULL,41,1,28,0,30,50,105,90,25,25),(99,'Kingler',11,NULL,2,NULL,41,2,NULL,0,55,75,130,115,50,50),(100,'Voltorb',13,NULL,3,NULL,42,1,30,0,40,100,30,50,55,55),(101,'Electrode',13,NULL,2,NULL,42,2,NULL,0,60,140,50,70,80,80),(102,'Exeggcute',12,14,3,NULL,43,1,NULL,0,60,40,40,80,60,45),(103,'Exeggutor',12,14,2,NULL,43,2,NULL,4,95,55,95,85,125,65),(104,'Cubone',5,NULL,3,NULL,44,1,28,0,50,35,50,95,40,50),(105,'Marowak',5,NULL,1,NULL,44,2,NULL,0,60,45,80,110,50,80),(106,'Hitmonlee',2,NULL,1,NULL,0,0,NULL,0,50,87,120,53,35,110),(107,'Hitmonchan',2,NULL,1,NULL,0,0,NULL,0,50,76,105,79,35,110),(108,'Lickitung',1,NULL,2,NULL,0,0,NULL,0,90,30,55,75,60,75),(109,'Koffing',4,NULL,3,NULL,45,1,35,0,40,35,65,95,60,45),(110,'Weezing',4,NULL,2,NULL,45,2,NULL,0,65,60,90,120,85,70),(111,'Rhyhorn',5,6,2,NULL,46,1,42,0,80,25,85,95,30,30),(112,'Rhydon',5,6,1,NULL,46,2,NULL,0,105,40,130,120,45,45),(113,'Chansey',1,NULL,1,NULL,0,0,NULL,0,250,50,5,5,35,105),(114,'Tangela',12,NULL,3,NULL,0,0,NULL,0,65,60,55,115,100,40),(115,'Kangaskhan',1,NULL,1,NULL,0,0,NULL,0,105,90,95,80,40,80),(116,'Horsea',11,NULL,3,NULL,47,1,32,0,30,60,40,70,70,25),(117,'Seadra',11,NULL,2,NULL,47,2,NULL,0,55,85,65,95,95,45),(118,'Goldeen',11,NULL,3,NULL,48,1,33,0,45,63,67,60,35,50),(119,'Seaking',11,NULL,2,NULL,48,2,NULL,0,80,68,92,65,65,80),(120,'Staryu',11,NULL,3,NULL,49,1,NULL,0,30,85,45,55,70,55),(121,'Starmie',11,14,2,NULL,49,2,NULL,2,60,115,75,85,100,85),(122,'Mr-mime',14,18,2,NULL,0,0,NULL,0,40,90,45,65,100,120),(123,'Scyther',7,3,2,NULL,0,0,NULL,0,70,105,110,80,55,80),(124,'Jynx',15,14,2,NULL,0,0,NULL,0,65,95,50,35,115,95),(125,'Electabuzz',13,NULL,2,NULL,0,0,NULL,0,65,105,83,57,95,85),(126,'Magmar',10,NULL,2,NULL,0,0,NULL,0,65,93,95,57,100,85),(127,'Pinsir',7,NULL,2,NULL,0,0,NULL,0,65,85,125,100,55,70),(128,'Tauros',1,NULL,2,NULL,0,0,NULL,0,75,110,100,95,40,70),(129,'Magikarp',11,NULL,3,NULL,50,1,20,0,20,80,10,55,15,20),(130,'Gyarados',11,3,1,NULL,50,2,NULL,0,95,81,125,79,60,100),(131,'Lapras',11,15,1,NULL,0,0,NULL,0,130,60,85,80,85,95),(132,'Ditto',1,NULL,3,NULL,0,0,NULL,0,48,48,48,48,48,48),(133,'Eevee',1,NULL,2,NULL,51,1,NULL,0,55,55,55,50,45,65),(134,'Vaporeon',11,NULL,0,NULL,51,2,NULL,2,130,65,65,60,110,95),(135,'Jolteon',13,NULL,0,NULL,51,2,NULL,3,65,130,65,60,110,95),(136,'Flareon',10,NULL,0,NULL,51,2,NULL,1,65,65,130,60,95,110),(137,'Porygon',1,NULL,0,NULL,0,0,NULL,0,65,40,60,70,85,75),(138,'Omanyte',6,11,0,NULL,52,1,40,0,35,35,40,100,90,55),(139,'Omastar',6,11,0,NULL,52,2,NULL,0,70,55,60,125,115,70),(140,'Kabuto',6,11,0,NULL,53,1,40,0,30,55,80,90,55,45),(141,'Kabutops',6,11,0,NULL,53,2,NULL,0,60,80,115,105,65,70),(142,'Aerodactyl',6,3,0,NULL,0,0,NULL,0,80,130,105,65,60,75),(143,'Snorlax',1,NULL,1,NULL,0,0,NULL,0,160,30,110,65,65,110),(144,'Articuno',15,3,0,NULL,0,0,NULL,0,90,85,85,100,95,125),(145,'Zapdos',13,3,0,NULL,0,0,NULL,0,90,100,90,85,125,90),(146,'Moltres',10,3,0,NULL,0,0,NULL,0,90,90,100,90,125,85),(147,'Dratini',16,NULL,2,NULL,54,1,30,0,41,50,64,45,50,50),(148,'Dragonair',16,NULL,1,NULL,54,2,55,0,61,70,84,65,70,70),(149,'Dragonite',16,3,0,NULL,54,3,NULL,0,91,80,134,95,100,100),(150,'Mewtwo',14,NULL,0,NULL,0,0,NULL,0,106,130,110,90,154,90),(151,'Mew',14,NULL,0,NULL,0,0,NULL,0,100,100,100,100,100,100),(244,'Entei',10,NULL,0,NULL,0,0,NULL,0,115,100,115,85,90,75),(251,'Celebei',14,12,0,'0000-00-00 00:00:00',0,0,0,0,100,100,100,100,100,100);
/*!40000 ALTER TABLE `pokemon` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evolutiontriggers`
--

LOCK TABLES `evolutiontriggers` WRITE;
/*!40000 ALTER TABLE `evolutiontriggers` DISABLE KEYS */;
INSERT INTO `evolutiontriggers` VALUES (0,'No Condition'),(1,'Fire Stone'),(2,'Water Stone'),(3,'Thunder Stone'),(4,'Leaf Stone'),(5,'Moon Stone'),(6,'Sun Stone'),(7,'Shiny Stone'),(8,'Dusk Stone'),(9,'Dawn Stone'),(10,'Ever Stone'),(20,'Trade Only');
/*!40000 ALTER TABLE `evolutiontriggers` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES (0,'Nugget',1000),(1,'Fire Stone',750),(2,'Water Stone',750),(3,'Thunder Stone',750),(4,'Leaf Stone',750),(5,'Moon Stone',750),(6,'Sun Stone',750),(7,'Shiny Stone',750),(8,'Dusk Stone',750),(9,'Dawn Stone',750),(10,'Ever Stone',750),(11,'Rare Candy',1000),(12,'Dome Fossil',1250),(13,'Helix Fossil',1250),(14,'Old Amber',1250),(15,'Full Restore',500);
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `types`
--

LOCK TABLES `types` WRITE;
/*!40000 ALTER TABLE `types` DISABLE KEYS */;
INSERT INTO `types` VALUES ('normal',1,1.0,1.0,1.0,1.0,1.0,0.5,1.0,0.0,0.5,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0),('fighting',2,2.0,1.0,0.5,0.5,1.0,2.0,0.5,0.0,2.0,1.0,1.0,1.0,1.0,0.5,2.0,1.0,2.0,0.5,1.0,1.0),('flying',3,1.0,2.0,1.0,1.0,1.0,0.5,2.0,1.0,0.5,1.0,1.0,2.0,0.5,1.0,1.0,1.0,1.0,1.0,1.0,1.0),('poison',4,1.0,1.0,1.0,0.5,0.5,0.5,1.0,0.5,0.0,1.0,1.0,2.0,1.0,1.0,1.0,1.0,1.0,2.0,1.0,1.0),('ground',5,1.0,1.0,0.0,2.0,1.0,2.0,0.5,1.0,2.0,2.0,1.0,0.5,2.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0),('rock',6,1.0,0.5,2.0,1.0,0.5,1.0,2.0,1.0,0.5,2.0,1.0,1.0,1.0,1.0,2.0,1.0,1.0,1.0,1.0,1.0),('bug',7,1.0,0.5,0.5,0.5,1.0,1.0,1.0,0.5,0.5,0.5,1.0,2.0,1.0,2.0,1.0,1.0,2.0,0.5,1.0,1.0),('ghost',8,0.0,1.0,1.0,1.0,1.0,1.0,1.0,2.0,1.0,1.0,1.0,1.0,1.0,2.0,1.0,1.0,0.5,1.0,1.0,1.0),('steel',9,1.0,1.0,1.0,1.0,1.0,2.0,1.0,1.0,0.5,0.5,0.5,1.0,0.5,1.0,2.0,1.0,1.0,2.0,1.0,1.0),('fire',10,1.0,1.0,1.0,1.0,1.0,0.5,2.0,1.0,2.0,0.5,0.5,2.0,1.0,1.0,2.0,0.5,1.0,1.0,1.0,1.0),('water',11,1.0,1.0,1.0,1.0,2.0,2.0,1.0,1.0,1.0,2.0,0.5,0.5,1.0,1.0,1.0,0.5,1.0,1.0,1.0,1.0),('grass',12,1.0,1.0,0.5,0.5,2.0,2.0,0.5,1.0,0.5,0.5,2.0,0.5,1.0,1.0,1.0,0.5,1.0,1.0,1.0,1.0),('electric',13,1.0,1.0,2.0,1.0,0.0,1.0,1.0,1.0,1.0,1.0,2.0,0.5,0.5,1.0,1.0,0.5,1.0,1.0,1.0,1.0),('psychic',14,1.0,2.0,1.0,2.0,1.0,1.0,1.0,1.0,0.5,1.0,1.0,1.0,1.0,0.5,1.0,1.0,0.0,1.0,1.0,1.0),('ice',15,1.0,1.0,2.0,1.0,2.0,1.0,1.0,1.0,0.5,0.5,0.5,2.0,1.0,1.0,0.5,2.0,1.0,1.0,1.0,1.0),('dragon',16,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.5,1.0,1.0,1.0,1.0,1.0,1.0,2.0,1.0,0.0,1.0,1.0),('dark',17,1.0,0.5,1.0,1.0,1.0,1.0,1.0,2.0,1.0,1.0,1.0,1.0,1.0,2.0,1.0,1.0,0.5,0.5,1.0,1.0),('fairy',18,1.0,2.0,1.0,0.5,1.0,1.0,1.0,1.0,0.5,0.5,1.0,1.0,1.0,1.0,1.0,2.0,2.0,1.0,1.0,1.0),('shadow',10001,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0),('unknown',10002,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0);
/*!40000 ALTER TABLE `types` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-01-03  8:05:08
