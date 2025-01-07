import pygame

# Couleurs
BACKGROUND_COLOR = (25, 25, 112)  # Bleu nuit
GREEN = (34, 139, 34)

# Configuration du niveau
LEVEL_NAME = "Niveau 8 - Timing"

# Point de départ du joueur
player_start = [50, 500]

# Point d'arrivée (ajusté pour être sur la dernière plateforme)
finish_point = [750, 500]  # Y = 550 (plateforme) - 50 (hauteur du drapeau)

# Plateformes [x, y, largeur, hauteur]
platforms = [
    [0, 550, 150, 40],     # Départ
    [700, 550, 150, 40],   # Arrivée
    # Plateformes avec ennemis rapides
    [200, 550, 100, 20],
    [400, 550, 100, 20],
    [600, 550, 100, 20],
    # Plateformes en hauteur
    [150, 450, 60, 20],
    [350, 450, 60, 20],
    [550, 450, 60, 20],
    # Plateformes bonus
    [250, 350, 40, 20],
    [450, 350, 40, 20],
    [650, 350, 40, 20],
]

# Pièces [x, y]
coins = [
    [200, 500],  # Pièces principales
    [400, 500],
    [600, 500],
    # Pièces en hauteur
    [150, 400],
    [350, 400],
    [550, 400],
    # Pièces bonus
    [250, 300],
    [450, 300],
    [650, 300],
]

# Ennemis [x, y, range_x]
enemies = [
    [200, 530, 80],  # Ennemis rapides au sol
    [400, 530, 80],
    [600, 530, 80],
    # Ennemis en hauteur
    [150, 430, 40],
    [350, 430, 40],
    [550, 430, 40],
]

# Image de fond
background_image = None 