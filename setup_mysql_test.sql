-- prepares a MySQL server for the project

-- A database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- A new user hbnb_test (in localhost) and the password set to hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- use database hbnb_test_db
USE hbnb_test_db;

-- grants all privileges on the database hbnb_test_db (and only this database)
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- grant SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
