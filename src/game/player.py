import pygame
from .settings import WHITE

PLAYER_SPEED = 5
GRAVITY = 0.5
JUMP_SPEED = -12

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.score = 0
        self.lives = 3
        self.invincible = False
        self.invincible_timer = 0
        self.invincible_duration = 2000  # 2 secondes
        self.facing_right = True
        self.color = (0, 191, 255)  # Bleu ciel
        self.outline_color = (0, 140, 255)  # Bleu plus foncé

    def draw(self, screen, camera_x=0):
        # Position à l'écran
        screen_rect = pygame.Rect(self.rect.x - camera_x, self.rect.y,
                                self.rect.width, self.rect.height)
        
        # Effet de clignotement si invincible
        if self.invincible:
            if (pygame.time.get_ticks() // 100) % 2:
                return
        
        # Corps du personnage
        pygame.draw.rect(screen, self.color, screen_rect)
        pygame.draw.rect(screen, self.outline_color, screen_rect, 2)
        
        # Yeux
        eye_color = (255, 255, 255)
        pupil_color = (0, 0, 0)
        eye_size = 8
        pupil_size = 4
        
        # Position des yeux selon la direction
        if self.facing_right:
            left_eye_x = screen_rect.left + 8
            right_eye_x = screen_rect.left + 20
            pupil_offset = 2
        else:
            left_eye_x = screen_rect.left + 12
            right_eye_x = screen_rect.left + 24
            pupil_offset = -2
        
        # Dessin des yeux
        pygame.draw.circle(screen, eye_color,
                         (left_eye_x, screen_rect.top + 12), eye_size)
        pygame.draw.circle(screen, eye_color,
                         (right_eye_x, screen_rect.top + 12), eye_size)
        
        # Dessin des pupilles
        pygame.draw.circle(screen, pupil_color,
                         (left_eye_x + pupil_offset, screen_rect.top + 12), pupil_size)
        pygame.draw.circle(screen, pupil_color,
                         (right_eye_x + pupil_offset, screen_rect.top + 12), pupil_size)
        
        # Expression (sourire)
        smile_rect = pygame.Rect(screen_rect.left + 8, screen_rect.top + 20,
                               16, 8)
        pygame.draw.arc(screen, pupil_color, smile_rect, 0, 3.14, 2)

    def move(self, platforms):
        # Mettre à jour la direction du regard
        if self.vel_x > 0:
            self.facing_right = True
        elif self.vel_x < 0:
            self.facing_right = False
        
        # Appliquer la gravité
        self.vel_y += GRAVITY
        
        # Mettre à jour la position verticale
        self.rect.y += self.vel_y
        self.on_ground = False
        
        # Vérifier les collisions verticales
        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.vel_y > 0:
                    self.rect.bottom = platform.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = platform.bottom
                    self.vel_y = 0
        
        # Mettre à jour la position horizontale
        self.rect.x += self.vel_x
        
        # Vérifier les collisions horizontales
        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.vel_x > 0:
                    self.rect.right = platform.left
                elif self.vel_x < 0:
                    self.rect.left = platform.right

    def jump(self):
        if self.on_ground:
            self.vel_y = JUMP_SPEED
            return True
        return False

    def collect_coin(self):
        self.score += 10
        return True

    def hit_by_enemy(self, current_time):
        if not self.invincible:
            self.lives -= 1
            self.score = max(0, self.score - 5)  # Déduire 5 points avec un minimum de 0
            self.invincible = True
            self.invincible_timer = current_time
            return True
        return False

    def update_invincibility(self, current_time):
        if self.invincible and current_time - self.invincible_timer >= self.invincible_duration:
            self.invincible = False
