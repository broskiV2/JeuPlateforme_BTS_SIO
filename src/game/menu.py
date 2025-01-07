import pygame
import math
import random
from src.game.settings import WINDOW_SIZE, WHITE, BLACK, BLUE, LIGHT_BLUE

def get_font(size):
    return pygame.font.Font(None, size)

class MenuButton:
    def __init__(self, text, pos, size=(300, 60)):
        self.rect = pygame.Rect(0, 0, size[0], size[1])
        self.rect.center = pos
        self.text = text
        self.is_hovered = False
        self.base_color = (30, 30, 30)  # Gris foncé
        self.hover_color = (60, 60, 60)  # Gris plus clair
        self.text_color = WHITE
        self.font = get_font(40)
        self.hover_scale = 1.0
        self.animation_speed = 0.05
        self.glow_value = 0
        self.glow_speed = 0.1

    def draw(self, surface):
        # Animation de survol
        if self.is_hovered and self.hover_scale < 1.05:
            self.hover_scale += self.animation_speed
            self.glow_value = min(1, self.glow_value + self.glow_speed)
        elif not self.is_hovered and self.hover_scale > 1.0:
            self.hover_scale -= self.animation_speed
            self.glow_value = max(0, self.glow_value - self.glow_speed)

        # Calculer la taille et la position avec l'échelle
        scaled_rect = pygame.Rect(0, 0, 
                                self.rect.width * self.hover_scale,
                                self.rect.height * self.hover_scale)
        scaled_rect.center = self.rect.center

        # Effet de lueur
        if self.glow_value > 0:
            glow_surf = pygame.Surface((scaled_rect.width + 20, scaled_rect.height + 20), pygame.SRCALPHA)
            glow_color = (100, 200, 255, int(128 * self.glow_value))
            pygame.draw.rect(glow_surf, glow_color, glow_surf.get_rect(), border_radius=20)
            surface.blit(glow_surf, glow_surf.get_rect(center=scaled_rect.center))

        # Dessiner le bouton
        pygame.draw.rect(surface, 
                        self.hover_color if self.is_hovered else self.base_color,
                        scaled_rect,
                        border_radius=15)
        
        # Bordure subtile
        border_color = (80, 80, 80) if not self.is_hovered else (120, 120, 120)
        pygame.draw.rect(surface, border_color, scaled_rect, 
                        width=2, border_radius=15)

        # Dessiner le texte avec ombre
        shadow_color = (0, 0, 0, 100)
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=scaled_rect.center)
        
        # Ombre du texte
        shadow_surf = self.font.render(self.text, True, shadow_color)
        shadow_rect = shadow_surf.get_rect(center=(text_rect.centerx + 2, text_rect.centery + 2))
        surface.blit(shadow_surf, shadow_rect)
        surface.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered:
                return True
        return False

class Menu:
    def __init__(self):
        self.background_color = BLACK
        self.title_font = get_font(80)
        self.buttons = [
            MenuButton("JOUER", (WINDOW_SIZE[0]//2, 250)),
            MenuButton("OPTIONS", (WINDOW_SIZE[0]//2, 350)),
            MenuButton("QUITTER", (WINDOW_SIZE[0]//2, 450))
        ]
        self.particles = [(pygame.math.Vector2(random.randint(0, WINDOW_SIZE[0]),
                                           random.randint(0, WINDOW_SIZE[1])),
                          random.random() * 2 + 1,
                          random.random() * 360) for _ in range(30)]
        self.difficulty = "normal"

    def draw_particles(self, surface):
        current_time = pygame.time.get_ticks() * 0.001
        for particle, size, angle in self.particles:
            # Mouvement circulaire
            angle_rad = math.radians(angle + current_time * 30)
            offset_x = math.cos(angle_rad) * 2
            offset_y = math.sin(angle_rad) * 2
            
            # Couleur qui varie avec le temps
            hue = (angle + current_time * 20) % 360
            color = pygame.Color(0)
            color.hsva = (hue, 60, 100, 50)
            
            # Dessin de la particule
            pygame.draw.circle(surface, color, 
                             (int(particle.x + offset_x), int(particle.y + offset_y)), 
                             size)
            
            # Déplacement
            particle.y = (particle.y + size * 0.2) % WINDOW_SIZE[1]

    def draw(self, surface):
        surface.fill(self.background_color)
        self.draw_particles(surface)
        
        # Titre avec effet de lueur
        current_time = pygame.time.get_ticks() * 0.001
        glow = abs(math.sin(current_time)) * 50
        
        title_text = "JEU DE PLATEFORME"
        shadow_surf = self.title_font.render(title_text, True, (0, 0, 50))
        glow_surf = self.title_font.render(title_text, True, (50 + glow, 100 + glow, 255))
        text_surf = self.title_font.render(title_text, True, WHITE)
        
        shadow_rect = shadow_surf.get_rect(center=(WINDOW_SIZE[0]//2 + 4, 120 + 4))
        glow_rect = glow_surf.get_rect(center=(WINDOW_SIZE[0]//2, 120))
        text_rect = text_surf.get_rect(center=(WINDOW_SIZE[0]//2, 120))
        
        surface.blit(shadow_surf, shadow_rect)
        surface.blit(glow_surf, glow_rect)
        surface.blit(text_surf, text_rect)
        
        for button in self.buttons:
            button.draw(surface)

    def handle_event(self, event):
        for i, button in enumerate(self.buttons):
            if button.handle_event(event):
                if i == 0:  # Jouer
                    return "play"
                elif i == 1:  # Options
                    return "settings"
                else:  # Quitter
                    return "quit"
        return None

class SettingsMenu:
    def __init__(self):
        self.background_color = BLACK
        self.title_font = get_font(60)
        self.text_font = get_font(36)
        
        button_y = 250
        self.buttons = [
            MenuButton("SON : ON", (WINDOW_SIZE[0]//2, button_y)),
            MenuButton("PLEIN ÉCRAN : OFF", (WINDOW_SIZE[0]//2, button_y + 80)),
            MenuButton("THÈME : CLASSIQUE", (WINDOW_SIZE[0]//2, button_y + 160)),
            MenuButton("RETOUR", (WINDOW_SIZE[0]//2, button_y + 240))
        ]
        
        self.sound_enabled = True
        self.fullscreen = False
        self.themes = ["CLASSIQUE", "SOMBRE", "COLORÉ", "RÉTRO", "FANTAISIE"]
        self.current_theme = 0

    def draw(self, surface):
        surface.fill(self.background_color)
        
        # Titre
        title_text = "PARAMÈTRES"
        title_surf = self.title_font.render(title_text, True, WHITE)
        title_rect = title_surf.get_rect(center=(WINDOW_SIZE[0]//2, 120))
        surface.blit(title_surf, title_rect)
        
        # Mise à jour du texte des boutons
        self.buttons[0].text = "SON : ON" if self.sound_enabled else "SON : OFF"
        self.buttons[1].text = "PLEIN ÉCRAN : ON" if self.fullscreen else "PLEIN ÉCRAN : OFF"
        self.buttons[2].text = f"THÈME : {self.themes[self.current_theme]}"
        
        # Dessiner les boutons
        for button in self.buttons:
            button.draw(surface)

    def handle_event(self, event):
        for i, button in enumerate(self.buttons):
            if button.handle_event(event):
                if i == 0:  # Son
                    self.sound_enabled = not self.sound_enabled
                    return ("toggle_sound", self.sound_enabled)
                elif i == 1:  # Plein écran
                    self.fullscreen = not self.fullscreen
                    return ("toggle_fullscreen", self.fullscreen)
                elif i == 2:  # Thème
                    self.current_theme = (self.current_theme + 1) % len(self.themes)
                    return ("change_theme", self.themes[self.current_theme])
                else:  # Retour
                    return "back"
        return None
