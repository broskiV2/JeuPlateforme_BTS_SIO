import pygame

# Couleurs
BACKGROUND_COLOR = (0, 139, 139)  # Bleu-vert foncé
GREEN = (34, 139, 34)

# Configuration du niveau
LEVEL_NAME = "Niveau 6 - Parcours Acrobatique"

# Point de départ du joueur
player_start = [50, 500]

# Point d'arrivée (ajusté pour être sur la dernière plateforme)
finish_point = [700, 250]  # Y = 300 (plateforme) - 50 (hauteur du drapeau)

# Plateformes [x, y, largeur, hauteur]
platforms = [
    # Zone de départ sécurisée
    [0, 550, 200, 40],
    
    # Première section - Escalier montant
    [200, 500, 100, 20],
    [300, 450, 100, 20],
    [400, 400, 100, 20],
    
    # Section centrale - Plateformes espacées
    [250, 350, 80, 20],
    [400, 350, 80, 20],
    [550, 350, 80, 20],
    
    # Section finale
    [650, 300, 150, 40],  # Grande plateforme d'arrivée
    
    # Plateformes bonus pour les pièces
    [200, 300, 60, 20],
    [500, 250, 60, 20],
    
    # Plateformes de sécurité
    [100, 400, 60, 20],
    [600, 400, 60, 20],
]

# Pièces [x, y] (ajustées pour être au-dessus des plateformes)
coins = [
    # Chemin principal
    [220, 470],  # Au-dessus de la première plateforme
    [320, 420],  # Au-dessus de la deuxième plateforme
    [420, 370],  # Au-dessus de la troisième plateforme
    
    # Bonus en hauteur
    [210, 270],  # Au-dessus de la plateforme bonus
    [510, 220],  # Au-dessus de la plateforme bonus haute
    
    # Pièce de récompense
    [700, 270],  # Au-dessus de la plateforme finale
]

# Ennemis [x, y, range_x]
enemies = [
    # Ennemis sur le chemin principal
    [250, 480, 100],  # Premier ennemi
    [400, 380, 100],  # Ennemi central
    
    # Ennemi gardien
    [650, 280, 100],  # Garde l'arrivée
]

# Image de fond
background_image = None