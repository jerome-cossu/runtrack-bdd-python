mysql> SELECT * FROM etudiant
    -> WHERE age =(SELECT MAX(age) FROM etudiant);
+----+-------+--------+-----+-----------------------------+
| id | nom   | prenom | age | email                       |
+----+-------+--------+-----+-----------------------------+
|  2 | Steak | Chuck  |  45 | chuck.steak@laplateforme.io |
+----+-------+--------+-----+-----------------------------+