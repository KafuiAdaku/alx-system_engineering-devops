-- An sql to create a uuserser
-- username: holberton_user; hostname: localhost
-- password: projectcorrection280hbtn

CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
