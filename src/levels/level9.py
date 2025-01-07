import pygame

# Couleurs
BACKGROUND_COLOR = (128, 0, 0)  # Rouge foncé
GREEN = (34, 139, 34)

# Configuration du niveau
LEVEL_NAME = "Niveau 9 - Défi Extrême"

# Point de départ du joueur
player_start = [50, 500]

# Point d'arrivée (ajusté pour être sur la dernière plateforme)
finish_point = [750, 100]  # Y = 150 (plateforme) - 50 (hauteur du drapeau)

# Plateformes [x, y, largeur, hauteur]
platforms = [
    [0, 550, 100, 40],     # Départ
    # Plateformes minuscules
    [150, 500, 30, 20],
    [250, 450, 30, 20],
    [350, 400, 30, 20],
    [450, 350, 30, 20],
    [550, 300, 30, 20],
    [650, 250, 30, 20],
    # Plateformes avec ennemis
    [200, 550, 80, 20],
    [400, 500, 80, 20],
    [600, 450, 80, 20],
    # Plateformes bonus très difficiles
    [300, 200, 20, 20],
    [500, 150, 20, 20],
    # Plateforme d'arrivée
    [700, 150, 100, 40],
]

# Pièces [x, y]
coins = [
    [150, 450],  # Pièces sur le parcours principal
    [250, 400],
    [350, 350],
    [450, 300],
    [550, 250],
    [650, 200],
    # Pièces bonus très difficiles
    [300, 150],
    [500, 100],
    [400, 50],
]

# Ennemis [x, y, range_x]
enemies = [
    [200, 530, 60],  # Ennemis rapides
    [400, 480, 60],
    [600, 430, 60],
    [300, 180, 40],  # Ennemis sur plateformes bonus
    [500, 130, 40],
    [700, 130, 80],  # Ennemi final très difficile
]

# Image de fond
background_image = None 