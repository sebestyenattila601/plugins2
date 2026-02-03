import pygame
import sys

# Beállítások
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
AI_SIZE = 50
PLAYER_COLOR = (0, 128, 255) # Kék
AI_COLOR = (255, 0, 0)       # Piros

# Pygame inicializálása
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Az első AI játékom")
clock = pygame.time.Clock()

# Pozíciók
player_pos = [WIDTH // 2, HEIGHT // 2]
ai_pos = [100, 100]

# Sebesség
player_speed = 5
ai_speed = 2 # Az AI lassabb, hogy legyen esélyed!

# Játék hurok
while True:
    screen.fill((30, 30, 30)) # Sötétszürke háttér

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 1. Játékos mozgatása (Nyilakkal)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - PLAYER_SIZE:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - PLAYER_SIZE:
        player_pos[1] += player_speed

    # 2. AZ AI LOGIKÁJA (Az "agya")
    # Ha a játékos tőle jobbra van, menjen jobbra. Ha balra, menjen balra.
    if ai_pos[0] < player_pos[0]:
        ai_pos[0] += ai_speed
    elif ai_pos[0] > player_pos[0]:
        ai_pos[0] -= ai_speed

    if ai_pos[1] < player_pos[1]:
        ai_pos[1] += ai_speed
    elif ai_pos[1] > player_pos[1]:
        ai_pos[1] -= ai_speed

    # Megjelenítés
    pygame.draw.rect(screen, PLAYER_COLOR, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))
    pygame.draw.rect(screen, AI_COLOR, (ai_pos[0], ai_pos[1], AI_SIZE, AI_SIZE))

    pygame.display.flip()
    clock.tick(60) # 60 FPS
