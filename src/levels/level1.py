import pygame

# Couleurs
BACKGROUND_COLOR = (135, 206, 235)  # Ciel bleu
GREEN = (34, 139, 34)  # Vert forêt

# Configuration du niveau
LEVEL_NAME = "Niveau 1 - Tutoriel"

# Point de départ du joueur
player_start = [100, 400]

# Point d'arrivée (ajusté pour être sur la dernière plateforme)
finish_point = [700, 450]  # Y = 500 (plateforme) - 50 (hauteur du drapeau)

# Plateformes [x, y, largeur, hauteur]
platforms = [
    [0, 500, 300, 40],    # Plateforme de départ
    [350, 500, 200, 40],  # Plateforme du milieu
    [600, 500, 200, 40],  # Plateforme d'arrivée
]

# Pièces [x, y]
coins = [
    [200, 450],  # Première pièce pour montrer le concept
    [400, 450],  # Pièce au milieu
    [600, 450],  # Pièce près de l'arrivée
]

# Ennemis [x, y, range_x]
enemies = [
    [400, 470, 100],  # Un seul ennemi simple pour apprendre
]

# Image de fond
background_image = None  # Sera chargée par le jeu