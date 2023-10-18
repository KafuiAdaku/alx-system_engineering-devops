-- An sql script to create a uuserser
-- username: replica_user; hostname: %
-- password: replica

CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'replica';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holbrton_user'@'localhost';
FLUSH PRIVILEGES;
