import pygame

# Couleurs
BACKGROUND_COLOR = (0, 0, 0)  # Noir
GREEN = (34, 139, 34)

# Configuration du niveau
LEVEL_NAME = "Niveau 10 - Boss Final"

# Point de départ du joueur
player_start = [50, 500]

# Point d'arrivée (ajusté pour être sur la dernière plateforme)
finish_point = [700, 500]  # Y = 550 (plateforme) - 50 (hauteur du drapeau)

# Plateformes [x, y, largeur, hauteur]
platforms = [
    # Zone de départ sécurisée
    [0, 550, 200, 40],     # Zone de départ plus large
    
    # Arène principale avec plus de plateformes
    [250, 550, 100, 20],   # Plateformes de base
    [400, 550, 100, 20],
    [550, 550, 100, 20],
    
    # Plateformes de progression verticale
    [200, 450, 80, 20],    # Côté gauche
    [350, 450, 80, 20],    # Centre
    [500, 450, 80, 20],    # Côté droit
    
    # Plateformes intermédiaires
    [250, 350, 80, 20],
    [400, 350, 80, 20],
    [550, 350, 80, 20],
    
    # Plateformes hautes
    [300, 250, 80, 20],
    [450, 250, 80, 20],
    
    # Zone d'arrivée sécurisée
    [650, 550, 150, 40],   # Grande plateforme d'arrivée
]

# Pièces [x, y]
coins = [
    # Pièces sur le chemin principal
    [250, 500],
    [400, 500],
    [550, 500],
    
    # Pièces bonus en hauteur
    [200, 400],
    [350, 400],
    [500, 400],
    
    # Pièces de récompense
    [300, 200],
    [450, 200],
    
    # Pièce finale
    [700, 500],
]

# Ennemis [x, y, range_x]
enemies = [
    # Boss au sol avec grande zone de patrouille
    [400, 530, 200],  # Boss principal
    
    # Mini-boss sur les plateformes
    [350, 430, 100],  # Niveau intermédiaire
    [500, 330, 100],  # En hauteur
    
    # Gardien final
    [650, 530, 100],  # Garde l'arrivée
]

# Image de fond
background_image = None 