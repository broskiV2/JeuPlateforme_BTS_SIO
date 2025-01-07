import pygame

class Level:
    def __init__(self, level_module):
        self.LEVEL_NAME = level_module.LEVEL_NAME
        self.BACKGROUND_COLOR = level_module.BACKGROUND_COLOR
        self.platforms = level_module.platforms
        self.player_start = level_module.player_start
        self.coins = level_module.coins
        self.enemies = level_module.enemies
        self.finish_point = level_module.finish_point
        self.GREEN = level_module.GREEN
        self.background_image = level_module.background_image

# Import des modules de niveau
from . import level1, level2, level3, level4, level5, level6, level7, level8, level9, level10

# Création des instances de niveau
levels = [
    Level(level1),
    Level(level2),
    Level(level3),
    Level(level4),
    Level(level5),
    Level(level6),
    Level(level7),
    Level(level8),
    Level(level9),
    Level(level10)
] 