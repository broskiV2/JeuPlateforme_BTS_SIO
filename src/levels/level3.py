import pygame

# Couleurs
BACKGROUND_COLOR = (70, 130, 180)  # Bleu acier
GREEN = (34, 139, 34)

# Configuration du niveau
LEVEL_NAME = "Niveau 3 - Plateformes Mobiles"

# Point de départ du joueur
player_start = [50, 450]

# Point d'arrivée (ajusté pour être sur la dernière plateforme)
finish_point = [800, 200]  # Y = 250 (plateforme) - 50 (hauteur du drapeau), X = 750 + 50 (centre de la plateforme)

# Plateformes [x, y, largeur, hauteur]
platforms = [
    [0, 500, 150, 40],     # Plateforme de départ
    [200, 450, 100, 20],   # Petites plateformes
    [350, 400, 100, 20],
    [500, 350, 100, 20],
    [650, 300, 100, 20],
    [400, 250, 100, 20],   # Plateforme bonus
    [750, 250, 150, 40],   # Plateforme d'arrivée
]

# Pièces [x, y]
coins = [
    [200, 400],  # Sur chaque plateforme
    [350, 350],
    [500, 300],
    [650, 250],
    [400, 200],  # Pièce bonus
    #[750, 200],  # Près de l'arrivée
]

# Ennemis [x, y, range_x]
enemies = [
    [200, 430, 80],   # Un ennemi par plateforme
    [350, 380, 80],
    [500, 330, 80],
    #[650, 280, 80],
]

# Image de fond
background_image = None