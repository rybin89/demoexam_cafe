-- phpMyAdmin SQL Dump
-- version 3.4.10.1deb1
-- http://www.phpmyadmin.net
--
-- Хост: localhost
-- Время создания: Окт 01 2024 г., 10:54
-- Версия сервера: 5.5.22
-- Версия PHP: 5.3.10-1ubuntu3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База данных: `demo_exam_cafe`
--

-- --------------------------------------------------------

--
-- Структура таблицы `Drinks`
--

CREATE TABLE IF NOT EXISTS `Drinks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `price` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Дамп данных таблицы `Drinks`
--

INSERT INTO `Drinks` (`id`, `name`, `price`) VALUES
(1, 'Tea', 100),
(2, 'Juice', 150);

-- --------------------------------------------------------

--
-- Структура таблицы `Foods`
--

CREATE TABLE IF NOT EXISTS `Foods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `price` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Дамп данных таблицы `Foods`
--

INSERT INTO `Foods` (`id`, `name`, `price`) VALUES
(1, 'Pie', 200),
(2, 'Burger', 500);

-- --------------------------------------------------------

--
-- Структура таблицы `Orders`
--

CREATE TABLE IF NOT EXISTS `Orders` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `count_cliens` int(11) NOT NULL,
  `table_id` int(11) NOT NULL,
  `drink_id` int(11) NOT NULL,
  `food_id` int(11) NOT NULL,
  `shift_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Дамп данных таблицы `Orders`
--

INSERT INTO `Orders` (`id`, `count_cliens`, `table_id`, `drink_id`, `food_id`, `shift_id`, `status_id`) VALUES
(1, 2, 1, 2, 2, 1, 1),
(2, 3, 2, 1, 1, 1, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `Roles`
--

CREATE TABLE IF NOT EXISTS `Roles` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `role` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Дамп данных таблицы `Roles`
--

INSERT INTO `Roles` (`id`, `role`) VALUES
(1, 'Administator'),
(2, 'Cook'),
(5, 'Oficiant');

-- --------------------------------------------------------

--
-- Структура таблицы `Shifts`
--

CREATE TABLE IF NOT EXISTS `Shifts` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `cook` int(11) NOT NULL,
  `oficiant_1` int(11) NOT NULL,
  `oficiant_2` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Дамп данных таблицы `Shifts`
--

INSERT INTO `Shifts` (`id`, `date`, `cook`, `oficiant_1`, `oficiant_2`) VALUES
(1, '2024-10-01 13:00:00', 2, 4, 5),
(2, '2024-10-01 17:00:00', 3, 5, 4);

-- --------------------------------------------------------

--
-- Структура таблицы `Statuces`
--

CREATE TABLE IF NOT EXISTS `Statuces` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Дамп данных таблицы `Statuces`
--

INSERT INTO `Statuces` (`id`, `name`) VALUES
(1, 'Adopted'),
(2, 'Paid'),
(3, 'Preparing'),
(4, 'Ready');

-- --------------------------------------------------------

--
-- Структура таблицы `Tables`
--

CREATE TABLE IF NOT EXISTS `Tables` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `number` varchar(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Дамп данных таблицы `Tables`
--

INSERT INTO `Tables` (`id`, `number`) VALUES
(1, 'first Table'),
(2, 'secondary T');

-- --------------------------------------------------------

--
-- Структура таблицы `Users`
--

CREATE TABLE IF NOT EXISTS `Users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `login` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `role_id` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Дамп данных таблицы `Users`
--

INSERT INTO `Users` (`id`, `login`, `password`, `name`, `role_id`, `status`) VALUES
(1, 'admin', '111111', 'Admin Adminych', 1, 1),
(2, 'Cook1', '111111', 'Cool1 Cook', 2, 1),
(3, 'Cook2', '1111111', 'Cook2 Cook2', 2, 1),
(4, 'Oficiant1', '111111', 'Oficiant1 Oficiant', 5, 1),
(5, 'Oficiant2', '111111', 'Oficiant2 Oficiant', 5, 1);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
