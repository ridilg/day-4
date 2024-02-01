-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema belajar-3
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema belajar-3
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `belajar-3` DEFAULT CHARACTER SET utf8 ;
USE `belajar-3` ;

-- -----------------------------------------------------
-- Table `belajar-3`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `belajar-3`.`customer` (
  `id_cust` VARCHAR(16) NOT NULL,
  `nama_pelanggan` VARCHAR(50) NOT NULL,
  `no_wa` INT NOT NULL,
  PRIMARY KEY (`id_cust`),
  UNIQUE INDEX `no_wa_UNIQUE` (`no_wa` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `belajar-3`.`produk`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `belajar-3`.`produk` (
  `idproduk` INT NOT NULL,
  `nama_produk` VARCHAR(45) NOT NULL,
  `ref_produk` VARCHAR(45) NOT NULL DEFAULT 'foreign',
  PRIMARY KEY (`idproduk`),
  INDEX `id_cust_idx` (`ref_produk` ASC) VISIBLE,
  CONSTRAINT `id_cust`
    FOREIGN KEY (`ref_produk`)
    REFERENCES `belajar-3`.`customer` (`id_cust`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
