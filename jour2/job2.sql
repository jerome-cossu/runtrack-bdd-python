mysql> CREATE TABLE etage (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255),
    ->     numero INT,
    ->     superficie INT
    -> );
Query OK, 0 rows affected (0.05 sec)

mysql> create table salle (
    ->     id int auto_increment primary key,
    ->     nom varchar(255),
    ->     id_etage int,
    ->     capacite int
    -> );
Query OK, 0 rows affected (0.05 sec)

mysql> show tables;
+------------------------+
| Tables_in_laplateforme |
+------------------------+
| etage                  |
| etudiant               |
| salle                  |
+------------------------+
3 rows in set (0.01 sec)

mysql> describe etage;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int          | NO   | PRI | NULL    | auto_increment |
| nom        | varchar(255) | YES  |     | NULL    |                |
| numero     | int          | YES  |     | NULL    |                |
| superficie | int          | YES  |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

