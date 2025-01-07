import pygame

# Couleurs
BACKGROUND_COLOR = (139, 0, 139)  # Magenta foncé
GREEN = (34, 139, 34)

# Configuration du niveau
LEVEL_NAME = "Niveau 7 - Défi de Précision"

# Point de départ du joueur
player_start = [50, 500]

# Point d'arrivée (ajusté pour être sur la dernière plateforme)
finish_point = [700, 250]  # Y = 300 (plateforme) - 50 (hauteur du drapeau)

# Plateformes [x, y, largeur, hauteur]
platforms = [
    # Zone de départ
    [0, 550, 150, 40],  # Plateforme de départ
    
    # Première section - Plateformes moyennes avec progression graduelle
    [200, 500, 80, 20],
    [350, 470, 80, 20],
    [500, 440, 80, 20],
    
    # Section intermédiaire - Plateformes plus petites
    [250, 400, 60, 20],
    [400, 370, 60, 20],
    [550, 340, 60, 20],
    
    # Section finale avec progression vers la plateforme d'arrivée
    [450, 320, 50, 20],
    [600, 300, 200, 40],  # Grande plateforme d'arrivée
    
    # Plateformes de sécurité
    [150, 450, 60, 20],
    [300, 420, 60, 20],
    [450, 390, 60, 20],
]

# Pièces [x, y]
coins = [
    # Chemin principal
    [220, 470],  # Au-dessus des plateformes moyennes
    [370, 440],
    [520, 410],
    
    # Bonus sur les petites plateformes
    [270, 370],
    [420, 340],
    [570, 310],
    
    # Pièce de récompense finale
    [700, 270],  # Au-dessus de la plateforme finale
]

# Ennemis [x, y, range_x]
enemies = [
    # Ennemis sur les plateformes moyennes
    [250, 480, 80],  # Premier ennemi
    [400, 450, 80],  # Deuxième ennemi
    
    # Ennemis sur les petites plateformes
    [350, 350, 60],  # Ennemi central
    
    # Gardien final
    [650, 280, 100],  # Garde l'arrivée
]

# Image de fond
background_image = None