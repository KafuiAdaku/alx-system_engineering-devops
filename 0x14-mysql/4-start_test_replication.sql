-- A mysql script wich configures MySQL configuration settings

CHANGE MASTER TO
MASTER_HOST='100.24.205.66',
MASTER_USER='replica_user',
MASTER_PASSWORD='replica',
MASTER_LOG_FILE='mysql-bin.000001',
MASTER_LOG_POS=154;

START SLAVE;
SHOW SLAVE STATUS\G;
