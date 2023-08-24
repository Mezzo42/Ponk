import pygame
import random

# Initialisierung
pygame.init()

# Bildschirmgröße
screen_width = 800
screen_height = 600

# Farben
black = (0, 0, 0)
white = (255, 255, 255)

# Spielbildschirm einrichten
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ponk-Spiel")

# Schläger
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 100))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.y += 5

# Ball
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed_x = 5
        self.speed_y = 5

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Kollision mit Wänden
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed_y *= -1
        if self.rect.left <= 0:
            self.rect.center = (screen_width // 2, screen_height // 2)
            self.speed_x = 5
            self.speed_y = 5
        if self.rect.right >= screen_width:
            self.rect.center = (screen_width // 2, screen_height // 2)
            self.speed_x = -5
            self.speed_y = 5

        # Kollision mit Schläger
        if pygame.sprite.collide_rect(self, paddle_left) or pygame.sprite.collide_rect(self, paddle_right):
            self.speed_x *= -1

# Spielobjekte erstellen
paddle_left = Paddle(50, screen_height // 2)
paddle_right = Paddle(screen_width - 50, screen_height // 2)
ball = Ball()

# Spritelisten
all_sprites = pygame.sprite.Group()
all_sprites.add(paddle_left, paddle_right, ball)

# Spielhauptschleife
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Bildschirm leeren
    screen.fill(black)

    # Sprites zeichnen
    all_sprites.draw(screen)

    # Bildschirm aktualisieren
    pygame.display.flip()

    # Begrenzung der Aktualisierungsrate
    clock.tick(60)

pygame.quit()
