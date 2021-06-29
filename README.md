# LITReview

Ceci est le dossier du projet LITReview, vous trouverez l'ensemble des étapes nécessaires à suivre pour pouvoir lancer et tester le site en local sur votre ordinateur

![alt text](https://user.oc-static.com/upload/2020/09/18/16004297044411_P7.png "Logo LITReview")

## Etapes à suivre sur Windows et Mac

### S'assurer d'avoir le compiler de python installé

Ouvrir la console de commande de l'OS et taper:


`py --version`


Si il y a une erreur, alors aller sur python.org et télécharger la dernière version:

[Site officiel de python](https://www.python.org/downloads/)

### Installer Virtual Env

Toujours dans la console, écrire:

`py -m venv LITReview`

Cette commande va créer un environnement virtuel pour le projet.

### Le lancer

Puis:

`LITReview\Scripts\activate.bat`

Cette commande va lancer l'environnement virtuel que l'on vient de créer.

### Installer django

Puis, pour windows:

`py -m pip install Django`

Pour Mac:

`sudo pip install django`

Cette commande va installer le package de django, qui nous est obligatoire pour faire tourner le site internet.

### Mettre les fichiers du projet dans le dossier qui vient d'être créé

Dans le dossier du projet de l'environnement virtuel précedemment créé

### Lancer django

Toujours dans l'invite de commande:

`py manage.py runserver`

Puis faire `Ctrl + C` pour stopper le serveur

### Faire les migrations

Enfin, il faut connecter la base de données SQL au serveur:

Taper:

`py manage.py makemigrations`

Puis:

`py manage.py migrate`

Et relancer le serveur:

`py manage.py runserver`

## Identifiants de connection
Login: admin\
Mot de passe: 68056805
