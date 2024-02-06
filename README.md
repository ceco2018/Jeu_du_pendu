# **JEU DU PENDU**

## 1. Description générale du programme

Bienvenue dans le jeu du Pendu en Python ! Ce jeu classique vous met au défi de deviner un mot en un nombre limité d'essais.

## 2. Configurations compatibles

- Python 3.12 et versions compatibles.

- La version de l’OS (Windows 10, Ubuntu 20, Mac...).

## 3. Fonctionnalités

Les fonctionnalités globales du programme sont les suivantes :

- Choix aléatoire d'un mot parmi une liste prédéfinie.

- Choix aléatoire d'un mot parmi une liste fournie par le joueur. Nommez votre fichier :  "mots_pendu.txt". Les mots avec accents et caractère spéciaux sont pris en compte par le programme.

- Une limite d'essais permet de rendre le jeu plus difficile.

Par ailleur le code est composé principlement de fonctions.

- La fonction <mark>**remove_accents**</mark> permet de retirer les accents et normaliser les lettres.

- La fonction <mark>**choisir_mot**</mark> permet de choisir un mot au hasard dans une liste de mots.

- La fonction <mark>**importer_banque_de_mots**</mark> permet d'importer la banque de mots du jeu à partir d'un fichier txt.

- La fonction <mark>**afficher_mot**</mark> permet d'afficher chaque lettre du mot sur une ligne.

- La fonction <mark>**reveler_lettres_du_mot**</mark> permet de reveler après chaque proposition la lettre dans le mot caché.

- La fonction **<mark>determiner_victoire_echec</mark>** permet de determiner s'il y'a victoire ou  echec au cours d'une partie.

- La fonction <mark>**jouer_une_lettre**</mark> demande au joueur de jouer une lettre, la revèle et augmente le nombre d'erreurs en cas de mauvaise lettre.

- La fonction **<mark>donner_lettre_abscente_dans_le_mot</mark>** permet de donner un indice au joueur s'il lui reste une chance.

- Un programme final permet jouer une partie entière.

## 4. Packages et modules

Le programme s’exécute en important les modules ***string***, ***random*** et ***unicodedate***. Ces trois modules sont déjà intégrés à python 3. Vous n’aurez donc besoin d’aucun autre package supplémentaire.

## 5. Démarrage du programme

Clonez ce dépôt sur votre machine locale :

```bash
   git clone https://github.com/ceco2018/Jeu_du_pendu.git
```

Naviguez dans le répertoire du jeu et fichier principal : jeu_pendu.py
Suivez les instructions à l'écran pour deviner la lettre et tentez de découvrir le mot caché.

## 6. Configuration

Vous pouvez configurer certaines options du jeu en modifiant par exemple le nombre maximal d'essais autorisés pour deviner un mot.

## 7. Auteur

Cédric Foffé Ngoufo
