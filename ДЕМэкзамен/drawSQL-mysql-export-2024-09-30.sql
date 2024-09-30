CREATE TABLE `Users`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `login` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `role_id` INT NOT NULL,
    `status` BOOLEAN NOT NULL
);
CREATE TABLE `Foods`(
    `id` INT NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `price` FLOAT(53) NOT NULL,
    PRIMARY KEY(`id`)
);
CREATE TABLE `Roles`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `role` INT NOT NULL
);
CREATE TABLE `Tables`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `number` INT NOT NULL
);
CREATE TABLE `Orders`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `count_cliens` INT NOT NULL,
    `table_id` INT NOT NULL,
    `drink_id` INT NOT NULL,
    `food_id` INT NOT NULL,
    `shift_id` INT NOT NULL,
    `status_id` INT NOT NULL
);
CREATE TABLE `Shifts`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `date` DATETIME NOT NULL,
    `cook` INT NOT NULL,
    `oficiant_1` INT NOT NULL,
    `oficiant_2` INT NOT NULL
);
CREATE TABLE `Statuces`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL
);
CREATE TABLE `Drinks`(
    `id` INT NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `price` FLOAT(53) NOT NULL,
    PRIMARY KEY(`id`)
);
ALTER TABLE
    `Orders` ADD CONSTRAINT `orders_status_id_foreign` FOREIGN KEY(`status_id`) REFERENCES `Statuces`(`id`);
ALTER TABLE
    `Orders` ADD CONSTRAINT `orders_shift_id_foreign` FOREIGN KEY(`shift_id`) REFERENCES `Shifts`(`id`);
ALTER TABLE
    `Shifts` ADD CONSTRAINT `shifts_cook_foreign` FOREIGN KEY(`cook`) REFERENCES `Users`(`id`);
ALTER TABLE
    `Orders` ADD CONSTRAINT `orders_drink_id_foreign` FOREIGN KEY(`drink_id`) REFERENCES `Drinks`(`id`);
ALTER TABLE
    `Shifts` ADD CONSTRAINT `shifts_oficiant_1_foreign` FOREIGN KEY(`oficiant_1`) REFERENCES `Users`(`id`);
ALTER TABLE
    `Orders` ADD CONSTRAINT `orders_table_id_foreign` FOREIGN KEY(`table_id`) REFERENCES `Tables`(`id`);
ALTER TABLE
    `Orders` ADD CONSTRAINT `orders_food_id_foreign` FOREIGN KEY(`food_id`) REFERENCES `Foods`(`id`);
ALTER TABLE
    `Shifts` ADD CONSTRAINT `shifts_oficiant_2_foreign` FOREIGN KEY(`oficiant_2`) REFERENCES `Users`(`id`);
ALTER TABLE
    `Users` ADD CONSTRAINT `users_role_id_foreign` FOREIGN KEY(`role_id`) REFERENCES `Roles`(`id`);