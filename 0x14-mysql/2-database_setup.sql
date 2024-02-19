-- create replica user if not exits
CREATE USER IF NOT EXISTS 'replica_user'@'%';
-- grant permission to replicate my source
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
-- give SELECT privileges to holberton_user on mysql.user
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

