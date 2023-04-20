SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

DROP SCHEMA IF EXISTS `subletapp` ;
CREATE SCHEMA IF NOT EXISTS `subletapp` DEFAULT CHARACTER SET latin1 ;
USE `subletapp` ;

-- -----------------------------------------------------
-- Table `subletapp`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `subletapp`.`user` (
	username VARCHAR(50),
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	email VARCHAR(50),
	bio TEXT,
	age INT,
	dateJoined DATE,
	dateBeginSublet DATE,
	dateEndSublet DATE,
	pets VARCHAR(50),
	password VARCHAR(50),
	zipcode VARCHAR(50),
	requestID VARCHAR(50)
);
  PRIMARY KEY (`username`),
  CONSTRAINT `fk_requestID`
    FOREIGN KEY (`request_ID`)
    REFERENCES `subletapp`.`rentRequest` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  INDEX `first_name` (`first_name` ASC),
  INDEX `last_name` (`last_name` ASC),
  INDEX `zipcode` (`zipcode` ASC),
  INDEX `age` (`age` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `subletapp`.`rentRequest`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `subletapp`.`rentRequest` (
	id INT,
	isResolved VARCHAR(50),
	dateResolved DATE,
	info TEXT,
	dateSubmitted DATE,
	residentUsername VARCHAR(50)
);
  PRIMARY KEY (`id`)
  CONSTRAINT `fk_residentUsername`
    FOREIGN KEY (`residentUsername`)
    REFERENCES `subletapp`.`Resident` (`username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

-- -----------------------------------------------------
-- Table `subletapp`.`Resident`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `subletapp`.`resident` (
	username VARCHAR(50),
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	email VARCHAR(50),
	bio TEXT,
	password VARCHAR(50),
	dateAvailabletoBeginSublet DATE,
	dateAvailabletoEndSublet DATE,
	Age INT,
	requestID VARCHAR(50),
	propertyID VARCHAR(50)
);
  PRIMARY KEY (`username`)
  CONSTRAINT `fk_requestID`
    FOREIGN KEY (`requestID`)
    REFERENCES `subletapp`.`rentRequest` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_propertyID`
    FOREIGN KEY (`propertyID`)
    REFERENCES `subletapp`.`Property` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
  INDEX `first_name` (`first_name` ASC),
  INDEX `last_name` (`last_name` ASC),
  INDEX `age` (`age` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

-- -----------------------------------------------------
-- Table `subletapp`.`subletRequest`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `subletapp`.`property` (
	id INT,
	sqft INT,
	pets VARCHAR(50),
	rate INT,
	isOpen VARCHAR(50),
	address VARCHAR(50),
	city VARCHAR(50),
	state VARCHAR(50),
	zipCode VARCHAR(50),
	landlordUsername INT,
	description TEXT
);
  PRIMARY KEY (`id`))
  CONSTRAINT `fk_landlordUsername`
    FOREIGN KEY (`landlordUsername`)
    REFERENCES `subletapp`.`landlord` (`username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
  INDEX `sqft` (`sqft` ASC),
  INDEX `zipcode` (`zipcode` ASC),
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `subletapp`.`subletRequest`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `subletapp`.`rentRequest` (
	id INT,
	isResolved VARCHAR(50),
	dateResolved DATE,
	info TEXT,
	dateSubmitted DATE,
	residentUsername VARCHAR(50)
);
  PRIMARY KEY (`id`))
  CONSTRAINT `fk_residentUsername`
    FOREIGN KEY (`residentUsername`)
    REFERENCES `subletapp`.`Resident` (`username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `subletapp`.`landlord`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `subletapp`.`landlord` (
	id VARCHAR(50),
	first_name VARCHAR(50),
	last_name VARCHAR(50)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
