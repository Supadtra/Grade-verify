-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 13, 2020 at 01:31 PM
-- Server version: 10.1.40-MariaDB
-- PHP Version: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gradebc`
--

-- --------------------------------------------------------

--
-- Table structure for table `gradebc`
--

CREATE TABLE `gradebc` (
  `ID` int(10) NOT NULL,
  `Code` varchar(7) COLLATE utf32_unicode_ci NOT NULL,
  `Year` int(4) NOT NULL,
  `Seme` int(1) NOT NULL,
  `Grade` varchar(1) COLLATE utf32_unicode_ci NOT NULL,
  `Creator` varchar(20) COLLATE utf32_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_unicode_ci;

--
-- Dumping data for table `gradebc`
--

INSERT INTO `gradebc` (`ID`, `Code`, `Year`, `Seme`, `Grade`, `Creator`) VALUES
(592031004, '748-101', 5555, 2, 'B', '2222'),
(592031005, '748-102', 5555, 3, 'c', '111'),
(592031006, '748-103', 5555, 4, 'a', '333'),
(592031004, '748-101', 5555, 2, 'B', '2222'),
(592031005, '748-102', 5555, 3, 'c', '111'),
(592031006, '748-103', 5555, 4, 'a', '333'),
(592031004, '748-101', 5555, 2, 'B', '2222'),
(592031005, '748-102', 5555, 3, 'c', '111'),
(592031006, '748-103', 5555, 4, 'a', '333'),
(592031004, '748-101', 5555, 2, 'B', '2222'),
(592031005, '748-102', 5555, 3, 'c', '111'),
(592031006, '748-103', 5555, 4, 'a', '333'),
(592031004, '748-101', 5555, 2, 'B', '2222'),
(592031005, '748-102', 5555, 3, 'c', '111'),
(592031006, '748-103', 5555, 4, 'a', '333'),
(592031004, '748-101', 5555, 2, 'B', '2222'),
(592031005, '748-102', 5555, 3, 'c', '111'),
(592031006, '748-103', 5555, 4, 'a', '333'),
(592031004, '748-101', 5555, 2, 'B', '2222'),
(592031005, '748-102', 5555, 3, 'c', '111'),
(592031006, '748-103', 5555, 4, 'a', '333'),
(592031004, '748-101', 5555, 2, 'B', '2222'),
(592031005, '748-102', 5555, 3, 'c', '111'),
(592031006, '748-103', 5555, 4, 'a', '333'),
(592031004, '748-101', 5555, 2, 'B', '2222'),
(592031005, '748-102', 5555, 3, 'c', '111'),
(592031006, '748-103', 5555, 4, 'a', '333');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
