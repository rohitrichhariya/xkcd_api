CREATE TABLE `comic` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`comic_number` VARCHAR(500) NOT NULL,
	`comic_name` VARCHAR(500) NOT NULL,
	`comic_alt` TEXT NULL,
	`comic_link` TEXT NULL,
	`comic_image_link` TEXT NULL,
	`comic_image` LONGBLOB NULL,
	PRIMARY KEY (`id`)
)
COMMENT='This table will store the details of all comics which are requested using xkcd API';

