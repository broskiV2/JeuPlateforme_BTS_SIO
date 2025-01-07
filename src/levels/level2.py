import pygame

# Couleurs
BACKGROUND_COLOR = (100, 149, 237)  # Bleu cornflower
GREEN = (34, 139, 34)

# Configuration du niveau
LEVEL_NAME = "Niveau 2 - Premiers Défis"

# Point de départ du joueur
player_start = [50, 400]

# Point d'arrivée (ajusté pour être sur la dernière plateforme)
finish_point = [700, 300]  # Y = 350 (plateforme) - 50 (hauteur du drapeau)

# Plateformes [x, y, largeur, hauteur]
platforms = [
    [0, 500, 200, 40],     # Plateforme de départ
    [250, 450, 150, 40],   # Première plateforme surélevée
    [450, 400, 150, 40],   # Deuxième plateforme surélevée
    [650, 350, 150, 40],   # Plateforme d'arrivée
    [300, 300, 100, 20],   # Plateforme bonus en hauteur
]

# Pièces [x, y]
coins = [
    [150, 450],  # Sur la première plateforme
    [300, 400],  # Entre les plateformes
    [500, 350],  # Sur la deuxième plateforme
    [350, 250],  # Pièce bonus en hauteur
    [700, 300],  # Près de l'arrivée
]

# Ennemis [x, y, range_x]
enemies = [
    [300, 420, 100],  # Premier ennemi
    [500, 370, 100],  # Deuxième ennemi
]

# Image de fond
background_image = None