-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS tyrell_corp;

-- Switch to the tyrell_corp database
USE tyrell_corp;

-- Create table nexus6
CREATE TABLE IF NOT EXISTS nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Insert a sample entry into the nexus6 table
INSERT INTO nexus6 (name) VALUES ('Leon');

-- Grant SELECT permissions to holberton_user
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
