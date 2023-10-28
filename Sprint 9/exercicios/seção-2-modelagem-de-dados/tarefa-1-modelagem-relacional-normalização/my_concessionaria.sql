-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: myconcessionaria
-- ------------------------------------------------------
-- Server version	8.0.34-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dimCarro`
--

DROP TABLE IF EXISTS `dimCarro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dimCarro` (
  `idCarro` int NOT NULL AUTO_INCREMENT,
  `idCombustivel` int DEFAULT NULL,
  `marcaCarro` varchar(80) DEFAULT NULL,
  `modeloCarro` varchar(80) DEFAULT NULL,
  `chassiCarro` varchar(50) DEFAULT NULL,
  `anoCarro` int DEFAULT NULL,
  PRIMARY KEY (`idCarro`),
  KEY `fk_idCombustivel_idx` (`idCombustivel`),
  CONSTRAINT `fk_idCombustivel` FOREIGN KEY (`idCombustivel`) REFERENCES `dimCombustivel` (`idCombustivel`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dimCarro`
--

LOCK TABLES `dimCarro` WRITE;
/*!40000 ALTER TABLE `dimCarro` DISABLE KEYS */;
INSERT INTO `dimCarro` VALUES (1,1,'Fiat','Fiat Uno','AKJHKN98JY76539',2000),(2,1,'Fiat','Fiat Palio','IKJHKN98JY76539',2010),(3,1,'VW','Fusca 78','DKSHKNS8JS76S39',1978),(4,1,'Fiat','Fiat 147','LKIUNS8JS76S39',1996),(5,1,'Fiat','Fiat 147','SSIUNS8JS76S39',1996),(6,1,'Nissan','Versa','SKIUNS8JS76S39',2019),(7,2,'Nissan','Versa','AKIUNS1JS76S39',2019),(8,2,'Nissan','Versa','LLLUNS1JS76S39',2020),(9,3,'Toyota','Corolla XEI','AAAKNS8JS76S39',2023),(10,4,'Nissan','Frontier','MSLUNS1JS76S39',2022);
/*!40000 ALTER TABLE `dimCarro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dimCidade`
--

DROP TABLE IF EXISTS `dimCidade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dimCidade` (
  `idCidade` int NOT NULL AUTO_INCREMENT,
  `nomeCidade` varchar(45) DEFAULT NULL,
  `idEstado` int DEFAULT NULL,
  PRIMARY KEY (`idCidade`),
  KEY `fk_idEstado_idx` (`idEstado`),
  CONSTRAINT `fk_idEstado` FOREIGN KEY (`idEstado`) REFERENCES `dimEstado` (`idEstado`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dimCidade`
--

LOCK TABLES `dimCidade` WRITE;
/*!40000 ALTER TABLE `dimCidade` DISABLE KEYS */;
INSERT INTO `dimCidade` VALUES (1,'São Paulo',1),(2,'Rio de Janeiro',3),(3,'Belo Horizonte',2),(4,'Rio Branco',4),(5,'Macapá',5),(6,'Porto Alegre',6),(7,'Eusébio',7),(8,'Manaus',8),(9,'Campo Grande',9);
/*!40000 ALTER TABLE `dimCidade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dimCliente`
--

DROP TABLE IF EXISTS `dimCliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dimCliente` (
  `idCliente` int NOT NULL AUTO_INCREMENT,
  `nomeCliente` varchar(45) DEFAULT NULL,
  `idCidade` int DEFAULT NULL,
  PRIMARY KEY (`idCliente`),
  KEY `fk_idCidade_idx` (`idCidade`),
  CONSTRAINT `fk_idCidadeCliente` FOREIGN KEY (`idCidade`) REFERENCES `dimCidade` (`idCidade`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dimCliente`
--

LOCK TABLES `dimCliente` WRITE;
/*!40000 ALTER TABLE `dimCliente` DISABLE KEYS */;
INSERT INTO `dimCliente` VALUES (1,'Cliente dois',1),(2,'Cliente tres',2),(3,'Cliente quatro',2),(4,'Cliente seis',3),(5,'Cliente dez',4),(6,'Cliente vinte',5),(7,'Cliente vinte e dois',6),(8,'Cliente vinte e tres',7),(9,'Cliente cinco',8),(10,'Cliente vinte e seis',9);
/*!40000 ALTER TABLE `dimCliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dimCombustivel`
--

DROP TABLE IF EXISTS `dimCombustivel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dimCombustivel` (
  `idCombustivel` int NOT NULL AUTO_INCREMENT,
  `tipoCombustivel` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idCombustivel`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dimCombustivel`
--

LOCK TABLES `dimCombustivel` WRITE;
/*!40000 ALTER TABLE `dimCombustivel` DISABLE KEYS */;
INSERT INTO `dimCombustivel` VALUES (1,'Gasolina'),(2,'Etanol'),(3,'Flex'),(4,'Diesel');
/*!40000 ALTER TABLE `dimCombustivel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dimEstado`
--

DROP TABLE IF EXISTS `dimEstado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dimEstado` (
  `idEstado` int NOT NULL AUTO_INCREMENT,
  `nomeEstado` varchar(45) DEFAULT NULL,
  `idPais` int DEFAULT NULL,
  PRIMARY KEY (`idEstado`),
  KEY `fk_idPais_idx` (`idPais`),
  CONSTRAINT `fk_idPais` FOREIGN KEY (`idPais`) REFERENCES `dimPais` (`idPais`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dimEstado`
--

LOCK TABLES `dimEstado` WRITE;
/*!40000 ALTER TABLE `dimEstado` DISABLE KEYS */;
INSERT INTO `dimEstado` VALUES (1,'São Paulo',1),(2,'Minas Gerais',1),(3,'Rio de Janeiro',1),(4,'Acre',1),(5,'Amapá',1),(6,'Rio Grande do Sul',1),(7,'Ceará',1),(8,'Amazonas',1),(9,'Mato Grosso do Sul',1);
/*!40000 ALTER TABLE `dimEstado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dimPais`
--

DROP TABLE IF EXISTS `dimPais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dimPais` (
  `idPais` int NOT NULL AUTO_INCREMENT,
  `nomePais` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idPais`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dimPais`
--

LOCK TABLES `dimPais` WRITE;
/*!40000 ALTER TABLE `dimPais` DISABLE KEYS */;
INSERT INTO `dimPais` VALUES (1,'Brasil');
/*!40000 ALTER TABLE `dimPais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dimVendedor`
--

DROP TABLE IF EXISTS `dimVendedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dimVendedor` (
  `idVendedor` int NOT NULL AUTO_INCREMENT,
  `nomeVendedor` varchar(45) DEFAULT NULL,
  `sexoVendedor` smallint DEFAULT NULL,
  `idCidade` int DEFAULT NULL,
  PRIMARY KEY (`idVendedor`),
  KEY `fk_idCidade_idx` (`idCidade`),
  CONSTRAINT `fk_idCidadeVendedor` FOREIGN KEY (`idCidade`) REFERENCES `dimCidade` (`idCidade`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dimVendedor`
--

LOCK TABLES `dimVendedor` WRITE;
/*!40000 ALTER TABLE `dimVendedor` DISABLE KEYS */;
INSERT INTO `dimVendedor` VALUES (1,'Vendedor cinco',0,1),(2,'Vendedora seis',1,1),(3,'Vendedora sete',1,2),(4,'Vendedora oito',1,3),(5,'Vendedor dezesseis',0,8),(6,'Vendedor trinta',0,6),(7,'Vendedor trinta e um',0,7),(8,'Vendedora trinta e dois',1,9);
/*!40000 ALTER TABLE `dimVendedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbLocacao`
--

DROP TABLE IF EXISTS `tbLocacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbLocacao` (
  `idLocacao` int NOT NULL AUTO_INCREMENT,
  `idCarro` int DEFAULT NULL,
  `idCliente` int DEFAULT NULL,
  `idVendedor` int DEFAULT NULL,
  `kmCarro` int DEFAULT NULL,
  `dataLocacao` datetime DEFAULT NULL,
  `horaLocacao` time DEFAULT NULL,
  `dataEntrega` date DEFAULT NULL,
  `horaEntrega` time DEFAULT NULL,
  `qtdDiaria` int DEFAULT NULL,
  `vlrDiaria` decimal(18,2) DEFAULT NULL,
  PRIMARY KEY (`idLocacao`),
  KEY `fk_idCarro_idx` (`idCarro`),
  KEY `fk_idCliente_idx` (`idCliente`),
  KEY `fk_idVendedor_idx` (`idVendedor`),
  CONSTRAINT `fk_idCarro` FOREIGN KEY (`idCarro`) REFERENCES `dimCarro` (`idCarro`),
  CONSTRAINT `fk_idCliente` FOREIGN KEY (`idCliente`) REFERENCES `dimCliente` (`idCliente`),
  CONSTRAINT `fk_idVendedor` FOREIGN KEY (`idVendedor`) REFERENCES `dimVendedor` (`idVendedor`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbLocacao`
--

LOCK TABLES `tbLocacao` WRITE;
/*!40000 ALTER TABLE `tbLocacao` DISABLE KEYS */;
INSERT INTO `tbLocacao` VALUES (1,1,1,1,25412,'2015-01-10 00:00:00','10:00:00','2015-01-12','10:00:00',2,100.00),(2,1,1,1,29450,'2015-02-10 00:00:00','12:00:00','2015-02-12','12:00:00',2,100.00),(3,2,2,2,20000,'2015-02-13 00:00:00','12:00:00','2015-02-15','12:00:00',2,150.00),(4,2,3,2,21000,'2015-02-15 00:00:00','13:00:00','2015-02-20','13:00:00',5,150.00),(5,2,3,3,21700,'2015-03-02 00:00:00','14:00:00','2015-03-07','14:00:00',5,150.00),(6,3,4,4,121700,'2016-03-02 00:00:00','14:00:00','2016-03-12','14:00:00',10,250.00),(7,3,4,4,131800,'2016-08-02 00:00:00','14:00:00','2016-08-12','14:00:00',10,250.00),(8,3,3,2,151800,'2017-01-02 00:00:00','18:00:00','2017-01-12','18:00:00',10,250.00),(9,3,3,2,152800,'2018-01-02 00:00:00','18:00:00','2018-01-12','18:00:00',10,280.00),(10,4,5,5,211800,'2018-03-02 00:00:00','18:00:00','2018-03-12','18:00:00',10,50.00),(11,5,6,5,212800,'2018-04-01 00:00:00','11:00:00','2018-04-11','11:00:00',10,50.00),(12,6,6,5,21800,'2020-04-01 00:00:00','11:00:00','2020-04-11','11:00:00',10,150.00),(13,7,7,6,10000,'2022-05-01 00:00:00','08:00:00','2022-05-21','18:00:00',20,150.00),(14,7,7,6,20000,'2022-06-01 00:00:00','08:00:00','2022-06-21','18:00:00',20,150.00),(15,7,7,6,30000,'2022-07-01 00:00:00','08:00:00','2022-07-21','18:00:00',20,150.00),(16,7,7,6,40000,'2022-08-01 00:00:00','08:00:00','2022-08-21','18:00:00',20,150.00),(17,8,7,7,55000,'2022-09-01 00:00:00','08:00:00','2022-09-21','18:00:00',20,150.00),(18,8,7,7,56000,'2022-10-01 00:00:00','08:00:00','2022-10-21','18:00:00',20,150.00),(19,8,7,7,58000,'2022-11-01 00:00:00','08:00:00','2022-11-21','18:00:00',20,150.00),(20,9,9,5,1800,'2023-01-02 00:00:00','18:00:00','2023-01-12','18:00:00',10,880.00),(21,9,9,5,8500,'2023-01-15 00:00:00','18:00:00','2023-01-25','18:00:00',10,880.00),(22,10,10,8,28000,'2023-01-25 00:00:00','08:00:00','2023-01-30','18:00:00',5,600.00),(23,10,10,8,38000,'2023-01-31 00:00:00','08:00:00','2023-02-05','18:00:00',5,600.00),(24,10,10,8,48000,'2023-02-06 00:00:00','08:00:00','2023-02-11','18:00:00',5,600.00),(25,10,10,8,68000,'2023-02-12 00:00:00','08:00:00','2023-02-17','18:00:00',5,600.00),(26,10,10,8,78000,'2023-02-18 00:00:00','08:00:00','2023-02-19','18:00:00',1,600.00);
/*!40000 ALTER TABLE `tbLocacao` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-25 10:59:21
