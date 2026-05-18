import pygame

# Initialize pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 500, 150
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Welcome")

# Colors
BG_COLOR = (30, 30, 40)
TEXT_COLOR = (255, 255, 255)

# Font
font = pygame.font.SysFont("arial", 42)

# Text
text = font.render("Welcome to Pygame", True, TEXT_COLOR)
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Main loop
running = True
clock = pygame.time.Clock()