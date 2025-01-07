import pygame
import sys
import os
import math
import random

# Ajout du chemin du projet au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .settings import init_game, load_sounds, load_background_images, load_sprites, WINDOW_SIZE, WHITE, BLACK, BLUE, LIGHT_BLUE
from .menu import Menu, SettingsMenu, get_font
from .player import Player, PLAYER_SPEED
from .ui import GameUI
from src.levels import levels

class GameOverScreen:
    def __init__(self, score):
        self.score = score
        self.font_big = pygame.font.Font(None, 74)
        self.font = pygame.font.Font(None, 36)
        self.buttons = [
            {"text": "REJOUER", "rect": pygame.Rect(300, 300, 200, 50), "color": (255, 100, 100)},
            {"text": "MENU", "rect": pygame.Rect(300, 370, 200, 50), "color": (100, 100, 255)}
        ]

    def draw(self, screen):
        screen.fill((0, 0, 0))
        
        # Titre Game Over
        game_over_text = self.font_big.render("GAME OVER", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(WINDOW_SIZE[0]//2, 150))
        screen.blit(game_over_text, game_over_rect)
        
        # Score
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(WINDOW_SIZE[0]//2, 220))
        screen.blit(score_text, score_rect)
        
        # Boutons
        for button in self.buttons:
            pygame.draw.rect(screen, button["color"], button["rect"], border_radius=15)
            pygame.draw.rect(screen, WHITE, button["rect"], 2, border_radius=15)
            text = self.font.render(button["text"], True, WHITE)
            text_rect = text.get_rect(center=button["rect"].center)
            screen.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.buttons[0]["rect"].collidepoint(mouse_pos):
                return "replay"
            elif self.buttons[1]["rect"].collidepoint(mouse_pos):
                return "menu"
        return None

class GameCompleteScreen:
    def __init__(self, score):
        self.score = score
        self.font_big = pygame.font.Font(None, 74)
        self.font = pygame.font.Font(None, 36)
        self.buttons = [
            {"text": "MENU", "rect": pygame.Rect(300, 370, 200, 50), "color": (100, 100, 255)}
        ]

    def draw(self, screen):
        screen.fill((0, 0, 0))
        
        # Titre
        complete_text = self.font_big.render("FÉLICITATIONS !", True, (0, 255, 0))
        complete_rect = complete_text.get_rect(center=(WINDOW_SIZE[0]//2, 150))
        screen.blit(complete_text, complete_rect)
        
        # Message
        message_text = self.font.render("Vous avez terminé tous les niveaux !", True, WHITE)
        message_rect = message_text.get_rect(center=(WINDOW_SIZE[0]//2, 220))
        screen.blit(message_text, message_rect)
        
        # Score
        score_text = self.font.render(f"Score final : {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(WINDOW_SIZE[0]//2, 280))
        screen.blit(score_text, score_rect)
        
        # Bouton
        button = self.buttons[0]
        pygame.draw.rect(screen, button["color"], button["rect"], border_radius=15)
        pygame.draw.rect(screen, WHITE, button["rect"], 2, border_radius=15)
        text = self.font.render(button["text"], True, WHITE)
        text_rect = text.get_rect(center=button["rect"].center)
        screen.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.buttons[0]["rect"].collidepoint(mouse_pos):
                return "menu"
        return None

def handle_game_over(screen, game_over_screen):
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            result = game_over_screen.handle_event(event)
            if result:
                return result
        
        game_over_screen.draw(screen)
        pygame.display.flip()
        clock.tick(60)

def handle_game_complete(screen, game_complete_screen):
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            result = game_complete_screen.handle_event(event)
            if result:
                return result
        
        game_complete_screen.draw(screen)
        pygame.display.flip()
        clock.tick(60)

def play_level(screen, level_index, difficulty, sounds, background_images, initial_score=0, theme=None):
    if theme is None:
        theme = {
            "background": BLACK,
            "platform": [(34, 139, 34), (25, 111, 25)],
            "coin": [(255, 215, 0), (218, 165, 32)],
            "enemy": [(220, 20, 60), (139, 0, 0)],
            "player": (50, 150, 255),
            "ui": WHITE
        }

    # Initialisation du niveau
    current_level = levels[level_index]
    player = Player(current_level.player_start[0], current_level.player_start[1])
    player.color = theme["player"]  # Définir la couleur du joueur
    player.score = initial_score
    platforms = [pygame.Rect(p[0], p[1], p[2], p[3]) for p in current_level.platforms]
    
    # Initialisation des ennemis
    enemies = []
    for enemy_data in current_level.enemies:
        x, y, range_x = enemy_data
        enemies.append({
            'rect': pygame.Rect(x, y, 30, 30),
            'direction': 1,
            'start_x': x,
            'range': range_x
        })
    
    collected_coins = set()
    camera_x = 0
    clock = pygame.time.Clock()
    running = True
    game_ui = GameUI()
    
    while running:
        current_time = pygame.time.get_ticks()
        
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit", player.score
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player.jump():
                        if "jump" in sounds:
                            sounds["jump"].play()
                elif event.key == pygame.K_ESCAPE:
                    return "menu", player.score
        
        # Gestion des touches maintenues
        keys = pygame.key.get_pressed()
        player.vel_x = 0
        if keys[pygame.K_LEFT]:
            player.vel_x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player.vel_x = PLAYER_SPEED
        
        # Mise à jour du joueur
        player.move(platforms)
        player.update_invincibility(current_time)
        
        # Mise à jour de la caméra
        camera_x = max(0, player.rect.x - WINDOW_SIZE[0] // 3)
        
        # Vérification si le joueur est tombé
        if player.rect.top > WINDOW_SIZE[1]:
            player.rect.x = current_level.player_start[0]
            player.rect.y = current_level.player_start[1]
            player.vel_y = 0
            if player.hit_by_enemy(current_time):
                if "death" in sounds:
                    sounds["death"].play()
                if player.lives <= 0:
                    return "game_over", player.score
        
        # Mise à jour des ennemis
        for enemy in enemies:
            enemy['rect'].x += enemy['direction'] * 1
            if enemy['rect'].x > enemy['start_x'] + enemy['range']:
                enemy['direction'] = -1
            elif enemy['rect'].x < enemy['start_x']:
                enemy['direction'] = 1
            
            if enemy['rect'].colliderect(player.rect) and not player.invincible:
                if player.hit_by_enemy(current_time):
                    if "death" in sounds:
                        sounds["death"].play()
                    if player.lives <= 0:
                        return "game_over", player.score
        
        # Vérification des collisions avec les pièces
        player_rect = pygame.Rect(player.rect.x + 5, player.rect.y + 5,
                                player.rect.width - 10, player.rect.height - 10)
        for i, coin in enumerate(current_level.coins):
            if (i, level_index) not in collected_coins:
                coin_rect = pygame.Rect(coin[0], coin[1], 20, 20)
                if player_rect.colliderect(coin_rect):
                    collected_coins.add((i, level_index))
                    if player.collect_coin():
                        if "coin" in sounds:
                            sounds["coin"].play()
        
        # Vérification de la fin du niveau
        finish_rect = pygame.Rect(current_level.finish_point[0],
                                current_level.finish_point[1], 30, 50)
        if player_rect.colliderect(finish_rect):
            if "level_complete" in sounds:
                sounds["level_complete"].play()
            return "next_level", player.score
        
        # Nettoyage complet de l'écran
        screen.fill(theme["background"])
        
        # Affichage du fond avec dégradé
        for y in range(0, WINDOW_SIZE[1], 2):
            color = (
                max(0, current_level.BACKGROUND_COLOR[0] - y//10),
                max(0, current_level.BACKGROUND_COLOR[1] - y//10),
                max(0, current_level.BACKGROUND_COLOR[2] - y//10)
            )
            pygame.draw.line(screen, color, (0, y), (WINDOW_SIZE[0], y))
        
        # Dessin des plateformes avec effet 3D
        for platform in platforms:
            platform_screen = pygame.Rect(platform.x - camera_x, platform.y,
                                      platform.width, platform.height)
            if 0 <= platform_screen.right and platform_screen.left <= WINDOW_SIZE[0]:
                # Corps de la plateforme
                pygame.draw.rect(screen, theme["platform"][0], platform_screen)
                # Bordure supérieure
                pygame.draw.rect(screen, theme["platform"][1], platform_screen, 2)
                # Effet 3D
                pygame.draw.line(screen, theme["platform"][1],
                               (platform_screen.left, platform_screen.bottom),
                               (platform_screen.right, platform_screen.bottom))
        
        # Dessin des pièces avec animation
        for i, coin in enumerate(current_level.coins):
            if (i, level_index) not in collected_coins:
                coin_screen_x = coin[0] - camera_x
                if 0 <= coin_screen_x <= WINDOW_SIZE[0]:
                    coin_y_offset = abs(math.sin(current_time / 500)) * 5
                    coin_pos = (int(coin_screen_x + 10), int(coin[1] + 10 - coin_y_offset))
                    # Effet de brillance
                    size = 10 + abs(math.sin(current_time / 200)) * 2
                    pygame.draw.circle(screen, theme["coin"][1], coin_pos, int(size))
                    pygame.draw.circle(screen, theme["coin"][0], coin_pos, int(size - 2))
        
        # Dessin des ennemis avec animation
        for enemy in enemies:
            enemy_screen = pygame.Rect(enemy['rect'].x - camera_x, enemy['rect'].y,
                                   enemy['rect'].width, enemy['rect'].height)
            if 0 <= enemy_screen.right and enemy_screen.left <= WINDOW_SIZE[0]:
                # Corps de l'ennemi
                pygame.draw.rect(screen, theme["enemy"][0], enemy_screen)
                # Yeux
                eye_color = theme["ui"]
                eye_size = 6
                pygame.draw.circle(screen, eye_color,
                                 (enemy_screen.left + 10, enemy_screen.top + 10), eye_size)
                pygame.draw.circle(screen, eye_color,
                                 (enemy_screen.right - 10, enemy_screen.top + 10), eye_size)
                # Pupilles
                pupil_color = theme["enemy"][1]
                pupil_offset = -1 if enemy['direction'] < 0 else 1
                pygame.draw.circle(screen, pupil_color,
                                 (enemy_screen.left + 10 + pupil_offset * 2,
                                  enemy_screen.top + 10), eye_size - 3)
                pygame.draw.circle(screen, pupil_color,
                                 (enemy_screen.right - 10 + pupil_offset * 2,
                                  enemy_screen.top + 10), eye_size - 3)
        
        # Dessin du checkpoint (drapeau d'arrivée)
        finish_screen_x = current_level.finish_point[0] - camera_x
        if 0 <= finish_screen_x <= WINDOW_SIZE[0]:
            flag_height = 50  # Hauteur du drapeau
            
            # Trouver la plateforme d'arrivée et sa position exacte
            platform_found = False
            for platform in platforms:
                if abs(platform.x + platform.width//2 - current_level.finish_point[0]) < platform.width:
                    base_y = platform.top
                    platform_found = True
                    break
            
            if not platform_found:
                base_y = current_level.finish_point[1]
            
            # Mât du drapeau (plus fin)
            pole_rect = pygame.Rect(finish_screen_x + 15, base_y - flag_height,
                                  3, flag_height)
            pygame.draw.rect(screen, (200, 200, 200), pole_rect)
            
            # Drapeau avec animation
            flag_wave = math.sin(current_time / 200) * 5
            flag_points = [
                (finish_screen_x + 18, base_y - flag_height + 5),  # Point d'attache haut
                (finish_screen_x + 38 + flag_wave, base_y - flag_height + 10),  # Coin supérieur
                (finish_screen_x + 38 - flag_wave, base_y - flag_height + 25),  # Coin inférieur
                (finish_screen_x + 18, base_y - flag_height + 30),  # Point d'attache bas
            ]
            
            # Effet de brillance sur le drapeau
            flag_glow = abs(math.sin(current_time / 300)) * 55
            flag_color = (min(255, 50 + flag_glow), min(255, 205 + flag_glow), min(255, 50 + flag_glow))
            pygame.draw.polygon(screen, flag_color, flag_points)
            
            # Base du mât (plus large et plus haute)
            base_rect = pygame.Rect(finish_screen_x + 12, base_y,
                                  8, 8)
            pygame.draw.rect(screen, (150, 150, 150), base_rect)
            
            # Effet de particules autour du drapeau
            for i in range(5):
                particle_time = (current_time / 1000 + i / 5) % 1
                particle_x = finish_screen_x + 28 + math.cos(particle_time * 6.28) * 15
                particle_y = base_y - flag_height + 15 + math.sin(particle_time * 6.28) * 15
                particle_size = 2 + math.sin(current_time / 200 + i) * 1
                particle_color = (255, 255, 200, int(255 * (1 - particle_time)))
                particle_surface = pygame.Surface((4, 4), pygame.SRCALPHA)
                pygame.draw.circle(particle_surface, particle_color,
                                (2, 2), particle_size)
                screen.blit(particle_surface,
                          (int(particle_x - 2), int(particle_y - 2)))
        
        # Dessin du joueur
        player.draw(screen, camera_x)
        
        # Dessin de l'interface
        game_ui.draw(screen, player, current_level.LEVEL_NAME, current_time)
        
        # Mise à jour de l'affichage
        pygame.display.flip()
        clock.tick(60)
    
    return "quit", player.score

def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Jeu de Plateforme")
    clock = pygame.time.Clock()

    # Initialisation des menus
    menu = Menu()
    settings_menu = SettingsMenu()
    current_screen = "menu"
    current_level = 0
    total_score = 0
    sounds = load_sounds()
    background_images = load_background_images()

    # Thèmes de couleurs
    themes = {
        "CLASSIQUE": {
            "background": BLACK,
            "platform": [(34, 139, 34), (25, 111, 25)],  # Vert foncé
            "coin": [(255, 215, 0), (218, 165, 32)],     # Or
            "enemy": [(220, 20, 60), (139, 0, 0)],       # Rouge
            "player": (50, 150, 255),                     # Bleu
            "ui": WHITE
        },
        "SOMBRE": {
            "background": (10, 10, 15),
            "platform": [(40, 40, 45), (30, 30, 35)],    # Gris foncé
            "coin": [(200, 180, 60), (160, 140, 40)],    # Or foncé
            "enemy": [(150, 30, 30), (100, 20, 20)],     # Rouge foncé
            "player": (60, 100, 150),                     # Bleu foncé
            "ui": (200, 200, 200)
        },
        "COLORÉ": {
            "background": (20, 0, 40),
            "platform": [(147, 112, 219), (138, 43, 226)],  # Violet
            "coin": [(255, 140, 0), (255, 127, 80)],       # Orange
            "enemy": [(255, 20, 147), (199, 21, 133)],     # Rose
            "player": (0, 255, 255),                        # Cyan
            "ui": (255, 182, 193)
        },
        "RÉTRO": {
            "background": (0, 20, 0),
            "platform": [(0, 255, 0), (0, 200, 0)],      # Vert pixel
            "coin": [(255, 255, 0), (200, 200, 0)],      # Jaune pixel
            "enemy": [(255, 0, 0), (200, 0, 0)],         # Rouge pixel
            "player": (0, 255, 255),                      # Cyan pixel
            "ui": (0, 255, 0)
        },
        "FANTAISIE": {
            "background": (70, 0, 90),                    # Violet profond
            "platform": [(148, 0, 211), (138, 43, 226)], # Violet magique
            "coin": [(255, 223, 0), (255, 215, 0)],      # Or brillant
            "enemy": [(0, 206, 209), (0, 139, 139)],     # Turquoise
            "player": (255, 105, 180),                    # Rose vif
            "ui": (255, 218, 185)                        # Pêche
        }
    }
    current_theme = themes["CLASSIQUE"]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if current_screen == "menu":
                result = menu.handle_event(event)
                if result == "play":
                    current_screen = "game"
                elif result == "settings":
                    current_screen = "settings"
                elif result == "quit":
                    running = False
            elif current_screen == "settings":
                result = settings_menu.handle_event(event)
                if result == "back":
                    current_screen = "menu"
                elif isinstance(result, tuple):
                    action, value = result
                    if action == "toggle_sound":
                        for sound in sounds.values():
                            sound.set_volume(0.3 if value else 0)
                    elif action == "toggle_fullscreen":
                        if value:
                            screen = pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN)
                        else:
                            screen = pygame.display.set_mode(WINDOW_SIZE)
                    elif action == "change_theme":
                        current_theme = themes[value]

        # Mise à jour de l'affichage
        if current_screen == "menu":
            menu.draw(screen)
        elif current_screen == "settings":
            settings_menu.draw(screen)
        elif current_screen == "game":
            game_state, level_score = play_level(screen, current_level, menu.difficulty, sounds, background_images, total_score, current_theme)
            total_score = level_score
            
            if game_state == "game_over":
                game_over_screen = GameOverScreen(total_score)
                result = handle_game_over(screen, game_over_screen)
                if result == "menu":
                    current_screen = "menu"
                    current_level = 0
                    total_score = 0
                elif result == "replay":
                    continue
            elif game_state == "next_level":
                current_level += 1
                if current_level >= len(levels):
                    game_complete_screen = GameCompleteScreen(total_score)
                    handle_game_complete(screen, game_complete_screen)
                    current_level = 0
                    total_score = 0
                    current_screen = "menu"
            elif game_state == "menu":
                current_screen = "menu"
                current_level = 0
                total_score = 0

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
