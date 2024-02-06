import string
import random
import unicodedata

print("------------------------------------------------- MGA802 --------------------------------------------------")
print("---------------------------------------------- JEU DU PENDU -----------------------------------------------")

# ----------- Renvoie une chaîne de caractère qui contient l’alphabet
alphabet = string.ascii_lowercase

# ----------- Initialisation des valeurs d'entrées
erreur = 0  # nombre d'erreurs effectuées par le joueur
nbre_de_chance = 6  # nombre de d'essai maximal pour déviner le mot


def remove_accents(input_str):
    """ Fonction qui permet de retirer les accents et normaliser les lettres
    source : https://stackoverflow.com/questions/517923/what-is-the-best-way
    -to-remove-accents-normalize-in-a-python-unicode-string """
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


def choisir_mot(mots):
    """ Fonction pour choisir un mot au hasard dans une liste de mots """
    return remove_accents(random.choice(mots))


def importer_banque_de_mots(nom_fichier):
    """ Fonction pour importer la banque de mots du jeu à partir d'un fichier txt """
    liste_de_mots = []
    # Ouvrir le contenu du fichier
    with open(nom_fichier, 'r', encoding='utf-8') as file:
        # Lire le contenu du fichier ligne par ligne
        contenu = file.readlines( )
        # Copier le contenu du fichier txt source dans une liste
        for ligne in contenu:
            ligne = ligne.strip("\n")
            liste_de_mots.append(ligne)
    return liste_de_mots


# ----------- Appel de la fonction pour définir la banque de mots à jouer
banque_de_mots = importer_banque_de_mots("mots_pendu.txt")

# ----------- Appel de la fonction pour choisir un mot aléatoire à jouer
mot_aleatoire = choisir_mot(banque_de_mots)

# ----------- Convertir le mot aléatoire en liste de lettres
mot_secret_en_liste = []
for lettre in mot_aleatoire:
    mot_secret_en_liste.append(lettre)

# ----------- Définir le format des lettres dévinées par le joueur
lettres_devinees = []
for i in range(len(mot_secret_en_liste)):
    lettres_devinees.append("_")


def afficher_mot(la_liste):
    """ Fonction pour afficher chaque lettre du mot sur une ligne """
    for j in range(len(la_liste)):
        print(la_liste[j], '', end="")


print(f"le mot à déviner est composé de - {len(mot_aleatoire)} - lettres ")


def reveler_lettres_du_mot(lettre_mot, lettres_devinees):
    """ Fonction pour reveler après chaque proposition la lettre dans le mot caché """
    global erreur  # comptabiliser l'erreur globale
    count = 0
    # boucle pour verifier si la lettre proposée est dans le mot
    for i in range(len(mot_secret_en_liste)):
        if mot_secret_en_liste[i] == lettre_mot:
            count += 1
            lettres_devinees[i] = lettre_mot
    # si mauvaise lettre proposée, alors comptabiliser l'erreur
    if count == 0:
        erreur += 1
    # afficher le nombre d'erreurs commises
    print("Nombre d'erreurs: ", erreur)
    return lettres_devinees, erreur


def determiner_victoire_echec(lettres_devinees):
    """ Fonction pour determiner les victoires et les echecs """
    if (erreur < nbre_de_chance) and (mot_secret_en_liste == lettres_devinees):
        return True
    else:
        return False


def jouer_une_lettre():
    """ Cette fonction demande au joueur de jouer une lettre,
    la revèle et augmente le nombre d'erreurs en cas de mauvaise lettre """
    # demander au joueur de jouer une lettre
    lettre = input("proposer une lettre : \n")
    # appel de la fonction pour revèler la lettre jouée si contenue dans le mot
    reveler_lettres_du_mot(lettre, lettres_devinees)
    # afficher les lettres dévinées
    afficher_mot(lettres_devinees)
    return erreur


def donner_lettre_abscente_dans_le_mot(mot_secret_en_liste):
    """ Fonction pour donner un indice au joueur s'il lui reste une chance """
    liste_lettres_abscentes = []
    print("Attention! c'est votre dernière chance")
    print("Voici un indice pour vous aider :")
    # boucler pour extraire toutes les lettres du mot caché de l'alphabet
    for lettre in alphabet:
        if mot_secret_en_liste.find(lettre) == -1:
            liste_lettres_abscentes.append(lettre)
    # retourner une lettre choisie aléatoirement pour la donner en indice
    return random.choice(liste_lettres_abscentes)


# ----------- Programme final pour jouer une partie entière
# continuer la partie tant que le nombre d'erreurs est inférieur à 6 et qu'on n'est pas au bout de la victoire/échec
while (erreur < nbre_de_chance) and (not (determiner_victoire_echec(lettres_devinees))):
    # appeler la fonction pour joueur une lettre
    jouer_une_lettre( )
    # donner un indice s'il reste une chance
    if erreur == nbre_de_chance - 1:
        lettre_indice = donner_lettre_abscente_dans_le_mot(mot_aleatoire)
        print(f"la lettre - {lettre_indice} - n'est pas dans le mot")
    # dire si le joueur a perdu
    if erreur == nbre_de_chance:
        print("\n Perdu ! Vous avez fait ", erreur, "erreurs \n")
    # dire si le joueur a gagné
    if determiner_victoire_echec(lettres_devinees):
        print("\n Félicitation ! Vous avez trouvé le mot. \n")

print("_____________________________________________________________________________________________________")
print(" *----**----**----**----**----**----**----** Fin du jeu ! **----**----**----**----**----**----**----*")
