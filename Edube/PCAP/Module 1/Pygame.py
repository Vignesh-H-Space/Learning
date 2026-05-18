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


while running:
    screen.fill(BG_COLOR)

    # Draw text
    screen.blit(text, text_rect)

    pygame.display.update()

    # Event handling
    for event in pygame.event.get():
        if (
            event.type == pygame.QUIT
            or event.type == pygame.KEYUP
            or event.type == pygame.MOUSEBUTTONUP
        ):
            running = False

    clock.tick(60)

pygame.quit()