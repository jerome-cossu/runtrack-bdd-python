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

mysql> insert into etage (nom, numero, superficie)
    -> values
    -> ('RDC', 0, 500),
    -> ('R+1', 1, 500);
Query OK, 2 rows affected (0.02 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> insert into salle (nom, id_etage, capacite)
    -> values
    -> ('Lounge', 1, 100),
    -> ('Studio Son', 1, 5),
    -> ('Broadcasting', 2, 50),
    -> ('Bocal Peda', 2, 4),
    -> ('Coworking', 2, 80),
    -> ('Studio Video', 2,5);
Query OK, 6 rows affected (0.02 sec)
Records: 6  Duplicates: 0  Warnings: 0

mysql> select * from etage;
+----+------+--------+------------+
| id | nom  | numero | superficie |
+----+------+--------+------------+
|  1 | RDC  |      0 |        500 |
|  2 | R+1  |      1 |        500 |
+----+------+--------+------------+
2 rows in set (0.00 sec)

mysql> select * from salle;
+----+--------------+----------+----------+
| id | nom          | id_etage | capacite |
+----+--------------+----------+----------+
|  1 | Lounge       |        1 |      100 |
|  2 | Studio Son   |        1 |        5 |
|  3 | Broadcasting |        2 |       50 |
|  4 | Bocal Peda   |        2 |        4 |
|  5 | Coworking    |        2 |       80 |
|  6 | Studio Video |        2 |        5 |
+----+--------------+----------+----------+