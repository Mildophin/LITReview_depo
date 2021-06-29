# LITReview

Ceci est le dossier du projet LITReview, vous trouverez l'ensemble des étapes nécessaires à suivre pour pouvoir lancer et tester le site en local sur votre ordinateur

![alt text](https://user.oc-static.com/upload/2020/09/18/16004297044411_P7.png "Logo LITReview")

## Etapes

1. S'assurer d'avoir le compiler de python installé

Ouvrir la console de commande de l'OS et taper:


`py --version`

2. Installer Virtual Env

Toujours dans la console, écrire:

`py -m venv LITReview`

Cette commande va créer un environnement virtuel pour le projet.

3. Le lancer

Puis:

`LITReview\Scripts\activate.bat`

Cette commande va lancer l'environnement virtuel que l'on vient de créer.

4. Installer django

Puis:

`py -m pip install Django`

Cette commande va installer le package de django, qui nous est obligatoire pour faire tourner le site internet.

5. Mettre les fichiers du projet dans le dossier qui vient d'être créé


6. Lancer django

Toujours dans l'invite de commande:

`py manage.py runserver`

Puis faire `Ctrl + C` pour stopper le serveur

7. Faire les migrations

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
