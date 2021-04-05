import pygame
import pygame_button

pygame.init()

display = pygame.display.set_mode((400, 200))
pygame.display.set_caption("pygame-button")

clicks = 0


def func():
    global clicks
    clicks += 1


# Create the button
btn = pygame_button.button(display, (0, 255, 0), "Pygame Button", (125, 70, 150, 40), lambda: func(),
                           border_radius=5, font_family="Arial", font_size=18)

while True:
    display.fill((255, 255, 255))

    # Show the button
    btn.show()

    # Show the amount of clicks
    font = pygame.font.SysFont("Arial", 20, italic=True)
    text = font.render(f"Clicks  {clicks}", True, (0, 0, 0))
    display.blit(text, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
