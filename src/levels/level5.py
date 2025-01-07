import pygame

# Couleurs
BACKGROUND_COLOR = (147, 112, 219)  # Violet moyen
GREEN = (34, 139, 34)

# Configuration du niveau
LEVEL_NAME = "Niveau 5 - Parcours d'Obstacles"

# Point de départ du joueur
player_start = [50, 500]

# Point d'arrivée (ajusté pour être sur la dernière plateforme)
finish_point = [750, 500]  # Y = 550 (plateforme) - 50 (hauteur du drapeau)

# Plateformes [x, y, largeur, hauteur]
platforms = [
    [0, 550, 200, 40],      # Départ
    [300, 550, 100, 40],    # Plateformes au sol
    [500, 550, 100, 40],
    [700, 550, 200, 40],    # Arrivée
    # Obstacles verticaux
    [200, 450, 40, 100],
    [400, 450, 40, 100],
    [600, 450, 40, 100],
    # Plateformes en hauteur (ajustées plus bas et plus proches)
    [100, 450, 80, 20],     # Première plateforme plus basse
    [300, 400, 80, 20],     # Deuxième plateforme intermédiaire
    [500, 400, 80, 20],     # Troisième plateforme même niveau
    [650, 450, 80, 20],     # Dernière plateforme pour redescendre
]

# Pièces [x, y]
coins = [
    [150, 500],    # Pièces au sol
    [350, 500],
    [550, 500],
    [750, 500],
    # Pièces en hauteur (ajustées avec les nouvelles plateformes)
    [100, 400],
    [300, 350],
    [500, 350],
    [650, 400],
]

# Ennemis [x, y, range_x]
enemies = [
    [300, 530, 80],    # Ennemis au sol
    [500, 530, 80],
    [700, 530, 80],
    # Ennemis en hauteur (ajustés avec les nouvelles plateformes)
    [100, 430, 60],
    [300, 380, 60],
    [500, 380, 60],
]

# Image de fond
background_image = None 