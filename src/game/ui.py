import pygame
import math
from .settings import WINDOW_SIZE, WHITE

class GameUI:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.heart_size = 20
        self.coin_size = 20
        self.padding = 15
        self.ui_height = 60
        
        # Couleurs
        self.ui_bg_color = (0, 0, 0, 180)
        self.ui_border_color = (100, 100, 100)
        self.heart_color = (220, 0, 0)
        self.score_color = (255, 215, 0)  # Or
        self.level_color = (0, 191, 255)  # Bleu ciel
        
        # Création de la surface de l'UI
        self.ui_surface = pygame.Surface((WINDOW_SIZE[0], self.ui_height), pygame.SRCALPHA)

    def draw(self, screen, player, level_name, current_time):
        # Réinitialiser la surface de l'UI
        self.ui_surface.fill((0, 0, 0, 0))
        
        # Fond semi-transparent avec effet de dégradé
        for y in range(self.ui_height):
            alpha = int(180 * (1 - y/self.ui_height))  # Dégradé de transparence
            pygame.draw.line(self.ui_surface, (0, 0, 0, alpha), 
                           (0, y), (WINDOW_SIZE[0], y))
        
        # Bordure inférieure avec effet de brillance
        glow = abs(math.sin(current_time / 1000)) * 50 + 50
        border_color = (*self.ui_border_color, glow)
        pygame.draw.line(self.ui_surface, border_color, 
                        (0, self.ui_height-1), 
                        (WINDOW_SIZE[0], self.ui_height-1), 2)

        # Affichage des vies avec des cœurs animés
        heart_beat = abs(math.sin(current_time / 500)) * 2
        for i in range(player.lives):
            heart_x = self.padding + i * (self.heart_size + 10)
            heart_y = self.padding
            
            # Animation de flottement
            heart_y += math.sin(current_time / 400 + i * 1.5) * 2
            
            # Taille du cœur avec animation
            current_size = self.heart_size + heart_beat
            
            # Effet de brillance
            heart_glow = abs(math.sin(current_time / 300 + i * 0.5)) * 35
            heart_color = (min(255, self.heart_color[0] + heart_glow),
                         min(255, self.heart_color[1] + heart_glow),
                         min(255, self.heart_color[2] + heart_glow))
            
            # Base du cœur
            circle_radius = current_size // 4
            pygame.draw.circle(self.ui_surface, heart_color, 
                             (int(heart_x + current_size//4), int(heart_y + current_size//4)),
                             int(circle_radius))
            pygame.draw.circle(self.ui_surface, heart_color, 
                             (int(heart_x + current_size*3//4), int(heart_y + current_size//4)),
                             int(circle_radius))
            
            # Pointe du cœur
            points = [
                (int(heart_x + current_size//2), int(heart_y + current_size)),
                (int(heart_x), int(heart_y + current_size//3)),
                (int(heart_x + current_size), int(heart_y + current_size//3)),
            ]
            pygame.draw.polygon(self.ui_surface, heart_color, points)

        # Affichage du score avec effet de brillance
        score_glow = abs(math.sin(current_time / 300)) * 55
        score_color_glow = (min(255, self.score_color[0] + score_glow),
                          min(255, self.score_color[1] + score_glow),
                          min(255, self.score_color[2] + score_glow))
        
        score_text = self.font.render(f"Score: {player.score}", True, score_color_glow)
        score_shadow = self.font.render(f"Score: {player.score}", True, (0, 0, 0, 128))
        score_rect = score_text.get_rect(midright=(WINDOW_SIZE[0] - 20, self.ui_height//2))
        
        # Ombre du score
        screen.blit(score_shadow, score_rect.move(2, 2))
        screen.blit(score_text, score_rect)

        # Affichage du nom du niveau avec effet de dégradé
        level_glow = abs(math.sin(current_time / 400)) * 55
        level_color_glow = (min(255, self.level_color[0] + level_glow),
                          min(255, self.level_color[1] + level_glow),
                          min(255, self.level_color[2] + level_glow))
        
        level_text = self.font.render(level_name, True, level_color_glow)
        level_shadow = self.font.render(level_name, True, (0, 0, 0, 128))
        level_rect = level_text.get_rect(center=(WINDOW_SIZE[0]//2, self.ui_height//2))
        
        # Ombre du nom du niveau
        screen.blit(level_shadow, level_rect.move(2, 2))
        screen.blit(level_text, level_rect)

        # Séparateurs verticaux décoratifs avec animation
        for i in range(2):
            x = (i + 1) * WINDOW_SIZE[0]//3
            wave = math.sin(current_time / 1000 + i * math.pi) * 3
            separator_color = (100, 100, 100, 150)
            
            # Points pour la ligne ondulée
            points = [(x + wave * math.sin(y/10), y) 
                     for y in range(10, self.ui_height-10, 2)]
            
            if len(points) > 1:
                pygame.draw.lines(self.ui_surface, separator_color, False, points, 1)

        # Afficher l'UI sur l'écran
        screen.blit(self.ui_surface, (0, 0))