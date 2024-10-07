DROP DATABASE IF EXISTS DB_PYTHON;
CREATE DATABASE DB_PYTHON;
USE DB_PYTHON;

CREATE TABLE `usuario` (
  `ID_Usuario` int NOT NULL,
  `Nome` varchar(100) NOT NULL,
  `Celular` varchar(20) NOT NULL,
  `Login` varchar(50) DEFAULT NULL,
  `Senha` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`ID_Usuario`),
  UNIQUE KEY `Login_UNIQUE` (`Login`)
) ;

INSERT INTO `usuario` VALUES 
(1,'José da Silva','(41) 99999-1234','jose.silva','70b4269b412a8af42b1f7b0d26eceff2'),
(2,'Maria dos Anjos','(41) 98888-1234','maria.anjos','70b4269b412a8af42b1f7b0d26eceff2'),
(3,'Gabriela Duarte Alves','(41) 977777-1234','g.alves','70b4269b412a8af42b1f7b0d26eceff2'),
(4,'Olivia Oliveira Santos','(41) 91234-1234','oli.oliveira','70b4269b412a8af42b1f7b0d26eceff2'),
(5,'Camila Andrade P. Alves','(41) 81234-1234','camila.andrade','70b4269b412a8af42b1f7b0d26eceff2'),
(6,'Daniela Dutra','(41)98765-1234','d.dutra','70b4269b412a8af42b1f7b0d26eceff2'),
(7,'Manoel Estevão','(41) 97777-1111','m.estavao','70b4269b412a8af42b1f7b0d26eceff2'),
(8,'Ricardo Alencar','(41)8765-1234','ricardo.alencar','70b4269b412a8af42b1f7b0d26eceff2'),
(9,'Estela Lorena','(41)98765-1234','e.lorena','70b4269b412a8af42b1f7b0d26eceff2'),
(10,'Vitor Frank','(41)95432-1234','vitor.f','70b4269b412a8af42b1f7b0d26eceff2'),
(11,'Zelia Amaro','(41)96555-6789','zelia.a','70b4269b412a8af42b1f7b0d26eceff2');



SELECT * FROM usuario;