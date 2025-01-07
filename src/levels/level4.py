import pygame

# Couleurs
BACKGROUND_COLOR = (65, 105, 225)  # Bleu royal
GREEN = (34, 139, 34)

# Configuration du niveau
LEVEL_NAME = "Niveau 4 - Ascension"

# Point de départ du joueur
player_start = [50, 500]

# Point d'arrivée (ajusté pour être sur la dernière plateforme)
finish_point = [700, 100]  # Y = 150 (plateforme) - 50 (hauteur du drapeau)

# Plateformes [x, y, largeur, hauteur]
platforms = [
    [0, 550, 200, 40],      # Base
    [200, 450, 100, 20],    # Montée
    [100, 350, 100, 20],
    [300, 300, 100, 20],
    [150, 250, 100, 20],
    [400, 200, 100, 20],
    [250, 150, 100, 20],
    [600, 150, 200, 40],    # Plateforme d'arrivée
    # Plateformes bonus
    [500, 350, 60, 20],
    [600, 400, 60, 20],
]

# Pièces [x, y]
coins = [
    [150, 500],  # Pièce de départ
    [200, 400],  # Pièces sur le chemin principal
    [100, 300],
    [300, 250],
    [150, 200],
    [400, 150],
    [250, 100],
    # Pièces bonus
    [500, 300],
    [600, 350],
]

# Ennemis [x, y, range_x]
enemies = [
    [200, 430, 80],   # Ennemis sur les plateformes principales
    [300, 280, 80],
    [400, 180, 80],
    [600, 130, 150],  # Ennemi final plus difficile
]

# Image de fond
background_image = None 