CREATE DATABASE IF NOT EXISTS `animal` DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci;
USE `animal`;

CREATE TABLE IF NOT EXISTS `animal`.`cienpies` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(45) NOT NULL,
    `edad` INT NOT NULL,
    `patas` INT NOT NULL,
    `venenoso` TINYINT NOT NULL,
    PRIMARY KEY (`id`));

CREATE TABLE IF NOT EXISTS `animal`.`lombriz` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(45) NOT NULL,
    `tamaño` VARCHAR(45) NOT NULL,
    `color` VARCHAR(45) NOT NULL,
    `especie` VARCHAR(45) NOT NULL,
    PRIMARY KEY (`id`));

CREATE TABLE IF NOT EXISTS `animal`.`usuario` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(45) NOT NULL,
    `edad` INT NOT NULL,
    `correo` VARCHAR(45) NOT NULL,
    `contraseña` VARCHAR(45) NOT NULL,
    PRIMARY KEY (`id`));