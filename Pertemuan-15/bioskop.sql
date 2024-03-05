-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2024 at 06:31 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nonton`
--

-- --------------------------------------------------------

--
-- Table structure for table `bioskop`
--

CREATE TABLE `bioskop` (
  `Id` int(11) NOT NULL,
  `no_transaksi` varchar(25) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `film` varchar(60) NOT NULL,
  `jadwal` varchar(25) NOT NULL,
  `no_kursi` varchar(25) NOT NULL,
  `harga_tiket` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bioskop`
--

INSERT INTO `bioskop` (`Id`, `no_transaksi`, `nama`, `film`, `jadwal`, `no_kursi`, `harga_tiket`) VALUES
(1, '001', 'Joko ', 'Solo Leveling', 'Senin', 'A1', 30000),
(2, '002', 'Rahma', 'Pasutri Gaje', 'Sabtu', 'B2', 40000),
(3, '003', 'Della', 'Lampir', 'Rabu', 'C3', 30000),
(4, '004', 'Rehan', 'Solo Leveling', 'Selasa', 'A2', 30000),
(5, '005', 'Desty', 'Pasutri Gaje', 'Sabtu', 'B2', 40000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bioskop`
--
ALTER TABLE `bioskop`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bioskop`
--
ALTER TABLE `bioskop`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
