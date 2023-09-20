-- prepares a MySQL server for the project AirBnB clone

-- Create DATABSE called hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Use Database
USE hbnb_dev_db;

-- grant all privileges on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
