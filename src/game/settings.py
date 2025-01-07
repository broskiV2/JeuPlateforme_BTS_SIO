import pygame
import os

# Configuration de la fenêtre
WINDOW_SIZE = (800, 600)
TITLE = "Jeu de Plateforme"

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
LIGHT_BLUE = (100, 200, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Configuration du son
SOUND_ENABLED = True
SOUND_VOLUME = 0.3
MUSIC_VOLUME = 0.3

# Configuration des fichiers
SOUND_FILES = {
    "jump": "assets/sounds/jump.wav",
    "coin": "assets/sounds/coin.wav",
    "death": "assets/sounds/death.wav",
    "level_complete": "assets/sounds/level_complete.wav",
    "background_music": "assets/sounds/background_music.wav"
}

# Configuration des sprites
SPRITE_FILES = {
    "player": "assets/images/player.png",
    "enemy": "assets/images/enemy.png",
    "platform": "assets/images/platform.png",
    "coin": "assets/images/coin.png"
}

BACKGROUND_IMAGES = {
    "level1": "assets/images/backgrounds/prairie.png",
    "level2": "assets/images/backgrounds/cave.png",
    "level3": "assets/images/backgrounds/castle.png"
}

# Configuration des niveaux
DIFFICULTY_SETTINGS = {
    "facile": {
        "enemy_speed": 1,
        "enemy_damage": 0.5,
        "player_lives": 5
    },
    "normal": {
        "enemy_speed": 2,
        "enemy_damage": 1,
        "player_lives": 3
    },
    "difficile": {
        "enemy_speed": 3,
        "enemy_damage": 2,
        "player_lives": 2
    }
}

def init_game():
    """Initialise Pygame et crée la fenêtre du jeu"""
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(TITLE)
    return screen

def load_sounds():
    """Charge les sons du jeu"""
    sounds = {}
    try:
        print("Tentative de chargement des sons...")
        # Chargement de la musique de fond
        if os.path.exists(SOUND_FILES["background_music"]):
            print(f"Chargement de la musique de fond: {SOUND_FILES['background_music']}")
            pygame.mixer.music.load(SOUND_FILES["background_music"])
            pygame.mixer.music.set_volume(MUSIC_VOLUME)
            pygame.mixer.music.play(-1)
            print("Musique de fond chargée avec succès")
        else:
            print(f"Fichier musique non trouvé: {SOUND_FILES['background_music']}")
        
        # Chargement des effets sonores
        for name, path in SOUND_FILES.items():
            if name != "background_music":
                if os.path.exists(path):
                    print(f"Chargement du son {name}: {path}")
                    sound = pygame.mixer.Sound(path)
                    sound.set_volume(SOUND_VOLUME)
                    sounds[name] = sound
                    print(f"Son {name} chargé avec succès")
                else:
                    print(f"Fichier son non trouvé: {path}")
    except Exception as e:
        print(f"Erreur lors du chargement des sons: {str(e)}")
        print(f"Type d'erreur: {type(e)}")
        import traceback
        traceback.print_exc()
    return sounds

def load_sprites():
    """Charge les sprites du jeu"""
    sprites = {}
    try:
        for name, path in SPRITE_FILES.items():
            if os.path.exists(path):
                sprite = pygame.image.load(path).convert_alpha()
                if name == "player":
                    sprite = pygame.transform.scale(sprite, (32, 32))
                elif name == "enemy":
                    sprite = pygame.transform.scale(sprite, (32, 32))
                elif name == "platform":
                    sprite = pygame.transform.scale(sprite, (64, 16))
                elif name == "coin":
                    sprite = pygame.transform.scale(sprite, (16, 16))
                sprites[name] = sprite
            else:
                print(f"Sprite non trouvé : {path}")
    except Exception as e:
        print(f"Erreur lors du chargement des sprites: {e}")
    return sprites

def load_background_images():
    """Charge les images de fond"""
    images = {}
    try:
        for name, path in BACKGROUND_IMAGES.items():
            if os.path.exists(path):
                image = pygame.image.load(path)
                image = pygame.transform.scale(image, WINDOW_SIZE)
                images[name] = image
    except Exception as e:
        print(f"Erreur lors du chargement des images: {e}")
    return images
