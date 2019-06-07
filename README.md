"# examen_django" 
Installer pillow pour l'ajout d'image (au cas ou):
pip install pillow

Le projet consiste à pouvoir ajouter des mangas, ainsi que les auteurs de ces derniers.
Cependant un manga ne peut pas être ajouter si on n'a pas déjà ajouter l'auteur.
on peut ajouter et supprimer un manga, on peut également faire la même chose pour les auteurs.

Entitées:

L'entité auteur est composé d'un nom, prénom, d'un âge et de l'histoire de l'auteur (ce dernier n'est pas obligatoire).
L'entité manga est composé d'un titre, d'un résumé, d'un auteur associé et d'une image.

Les fonctionnalité:

Auteurs:
on peut ajouter et supprimer un auteur comme expliqué précédemment, on peut également voir en détails la liste des auteurs,
et on peut voir les détails de chaque auteur, ici le détail sera l'historique que l'on ne verra que en regardant l'auteur en question.
Mangas:
C'est exactement les mêmes fonctionnalités que pour les auteurs, sauf que l'on peut voir une partie du résumé de l'oeuvre directement dans la liste des mangas.
Mais pour voir le résumé entier, il faut aller sur la page du manga en question.