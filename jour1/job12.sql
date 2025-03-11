mysql> INSERT INTO etudiant (nom, prenom, age, email)
    -> VALUES ('Dupuis', 'Martin', 18, 'martin.dupuis@laplateforme.io');

Query OK, 1 row affected (0.02 sec)

mysql> SELECT * FROM etudiant
    -> WHERE nom = 'Dupuis';
+----+--------+----------+-----+---------------------------------+
| id | nom    | prenom   | age | email                           |
+----+--------+----------+-----+---------------------------------+
|  5 | Dupuis | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
| 13 | Dupuis | Martin   |  18 | martin.dupuis@laplateforme.io   |
+----+--------+----------+-----+---------------------------------+