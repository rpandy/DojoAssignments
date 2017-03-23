-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema cities_states
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cities_states
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cities_states` DEFAULT CHARACTER SET utf8 ;
USE `cities_states` ;

-- -----------------------------------------------------
-- Table `cities_states`.`states`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cities_states`.`states` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NULL,
  `admission_to_union` DATE NULL,
  `population` MEDIUMTEXT NULL,
  `area` MEDIUMTEXT NULL,
  `largest_city` VARCHAR(50) NULL,
  `govenor` VARCHAR(30) NULL,
  `abbreviation` VARCHAR(2) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cities_states`.`cities`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cities_states`.`cities` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NULL,
  `zipcode` VARCHAR(9) NULL,
  `population` MEDIUMTEXT NULL,
  `incorporated` DATE NULL,
  `Capital` TINYINT(1) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `state_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_cities_states_idx` (`state_id` ASC),
  CONSTRAINT `fk_cities_states`
    FOREIGN KEY (`state_id`)
    REFERENCES `cities_states`.`states` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
