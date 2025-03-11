mysql> SELECT * FROM etudiant;
+----+-----------+----------+-----+---------------------------------+
| id | nom       | prenom   | age | email                           |
+----+-----------+----------+-----+---------------------------------+
|  1 | Spaghetti | Betty    |  20 | betty.Spaghetti@laplateforme.io |
|  2 | Steak     | Chuck    |  45 | chuck.steak@laplateforme.io     |
|  4 | Barnes    | Binkie   |  16 | binkie.barnes@laplateforme.io   |
|  5 | Dupuis    | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
| 13 | Dupuis    | Martin   |  18 | martin.dupuis@laplateforme.io   |
| 14 | Doe       | John     |  18 | john.doe@laplateforme.io        |
+----+-----------+----------+-----+---------------------------------+
6 rows in set (0.00 sec)

mysql> DELETE FROM etudiant
    -> WHERE id = 14;
Query OK, 1 row affected (0.02 sec)

mysql> SELECT * FROM etudiant;
+----+-----------+----------+-----+---------------------------------+
| id | nom       | prenom   | age | email                           |
+----+-----------+----------+-----+---------------------------------+
|  1 | Spaghetti | Betty    |  20 | betty.Spaghetti@laplateforme.io |
|  2 | Steak     | Chuck    |  45 | chuck.steak@laplateforme.io     |
|  4 | Barnes    | Binkie   |  16 | binkie.barnes@laplateforme.io   |
|  5 | Dupuis    | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
| 13 | Dupuis    | Martin   |  18 | martin.dupuis@laplateforme.io   |
+----+-----------+----------+-----+---------------------------------+