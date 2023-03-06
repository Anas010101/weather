--
-- Database: `weather`
--

----------------------------------------------------------

--
-- Table structure for table `temperature_history`
--

CREATE TABLE `temperature_history` (
  `city_code` varchar(15) NOT NULL,
  `date` date NOT NULL,
  `maximum` int(11) DEFAULT NULL,
  `minimum` int(11) DEFAULT NULL,
  `precipitation` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for table `temperature_history`
--
ALTER TABLE `temperature_history`
  ADD PRIMARY KEY (`city_code`,`date`);

----------------------------------------------------------

--
-- Table structure for table `temperature_statistics`
--

CREATE TABLE `temperature_statistics` (
  `city_code` varchar(15) NOT NULL,
  `year` int(4) NOT NULL,
  `maximum_average` float NOT NULL DEFAULT 0,
  `minimum_average` float NOT NULL DEFAULT 0,
  `accumulated_precipitation` float NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for table `temperature_statistics`
--
ALTER TABLE `temperature_statistics`
  ADD PRIMARY KEY (`city_code`,`year`);
COMMIT;