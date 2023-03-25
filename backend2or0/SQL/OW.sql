CREATE TABLE `OW`.`ships` (`id` INT NOT NULL AUTO_INCREMENT , `name` TEXT NOT NULL , `registration_id` TEXT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

CREATE TABLE `OW`.`routes` (`id` INT NOT NULL AUTO_INCREMENT , `registration_id` INT NOT NULL , `route_id` INT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

CREATE TABLE `OW`.`route` (`id` INT NOT NULL , `position.x` TEXT NOT NULL , `position.y` TEXT NOT NULL , `course` INT NOT NULL , `speed` INT NOT NULL , `start_port` TEXT NOT NULL , `end_port` TEXT NOT NULL , `timestamp` DATE NOT NULL ) ENGINE = InnoDB;
