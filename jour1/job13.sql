mysql> SELECT * FROM etudiant
    -> WHERE age BETWEEN 18 AND 25;
+----+-----------+----------+-----+---------------------------------+
| id | nom       | prenom   | age | email                           |
+----+-----------+----------+-----+---------------------------------+
|  1 | Spaghetti | Betty    |  20 | betty.Spaghetti@laplateforme.io |
|  5 | Dupuis    | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
| 13 | Dupuis    | Martin   |  18 | martin.dupuis@laplateforme.io   |