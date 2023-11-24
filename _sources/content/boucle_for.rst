Boucle bornée "for"
===================

La structure de boucle est une structure **itérative** et chaque répétition est une **itération**.

La boucle ``for`` est une boucle **bornée**. Elle répète **un nombre fini de fois** les instructions contenues dans la boucle.

La boucle ``for`` prélève dans l’ordre les valeurs présentes dans un ensemble **itérable** de valeurs.

Cet ensemble itérable de valeurs peut être:

-  un tableau ;
-  une chaine de caractère ;
-  une séquence de nombres entiers définie par ``range``.

Syntaxe de la boucle ``for``
----------------------------

.. code:: python

   for clé in ensemble_itérable_de_valeurs:
       instruction 1
       instruction 2
       etc
   # on désindente en fin de la boucle

La **clé** utilisée dans la boucle ``for`` est une **variable** qui prend une nouvelle valeur à chaque **itération**.

.. admonition:: Exemple

    Supposons le tableau de valeurs "mot", 13, "deux", 6, 125 et "quatre" que l'on souhaite afficher.

    >>> for cle in ["mot",13,"deux",6,125,"quatre"]:
            print(cle)

    On obtient l'affichage :

    .. code-block:: python
    
        mot
        13
        deux
        6
        125
        quatre

Itération avec RANGE
--------------------

Une variable de type ``tableau`` est **itérable**, ce qui signifie que l’on peut parcourir ses éléments un à un.

Par exemple, si on veut afficher les 6 premiers nombres entiers non nuls, on peut écrire la boucle suivante:

.. code:: python

   for i in [1,2,3,4,5,6]:
       print(i)

Seulement, cette méthode sera très longue si on veut afficher les 100 premiers nombres entiers !

En Python, le type ``range`` construit une séquence immuable de nombres entiers régulièrement espacés. Ce type ``range`` s’utilise comme une
fonction et a différents paramètres:

-  ``range(n)`` renvoie la séquence de nombres entiers positifs de :math:`0` jusqu’à :math:`n-1`.
-  ``range(p,n)`` renvoie la séquence de nombres entiers positifs de :math:`p` jusqu’à :math:`n-1`.
-  ``range(p,n,k)`` renvoie la séquence de nombres entiers positifs de :math:`p`, :math:`p+k`, :math:`p+2k`, … jusqu’à :math:`n-1` au plus.

.. admonition:: Exemple

    - ``range(8)`` est la séquence de nombres entiers de 0 à 7 soit huit valeurs : 0, 1, 2, 3, 4, 5, 6, 7.
    - ``range(3,8)`` est la séquence de nombres entiers de 3 à 7 soit cinq valeurs : 3, 4, 5, 6, 7.
    - ``range(3,8,2)`` est la séquence de nombres entiers 3, 5, 7. Elle démarre à 3, progresse de 2 en 2 jusqu'à 8.

.. tip::

    L'exécution de ``range(3,8,2)`` dans l'interpréteur Python n'affiche pas les valeurs. Pour les afficher, il faut une boucle avec un **print**.

Pour afficher les 100 premiers nombres entiers, on détermine la séquence de nombres entiers avec range: ``range(1,101)``.

Ensuite, avec une boucle ``for`` on peut afficher nos nombres:

.. code:: python

   for i in range(1,101):
       print(i)

Ce qui affichera tous les nombres entiers de 1 à 100.
