import pygame
import random

# Initialize pygame
pygame.init()

# Define custom events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# Define colors
GREEN = pygame.Color('green')
RED = pygame.Color('red')
LIGHTBLUE = pygame.Color('lightblue')
PINK = pygame.Color('pink')

# Define the Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        # Bounce off the horizontal boundaries
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True

        # Bounce off the vertical boundaries
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        # Post events when a boundary is hit
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    def change_color(self):
        self.image.fill(random.choice([GREEN, RED]))

# Function to change the background color
def change_background_color():
    global bg_color
    bg_color = random.choice([LIGHTBLUE, PINK])

# Initialize the game
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Boundary Sprite")

bg_color = LIGHTBLUE
screen.fill(bg_color)

# Sprite group
all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(GREEN, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
all_sprites_list.add(sp1)

# Main game loop
exit_game = False
clock = pygame.time.Clock()

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

    # Update and redraw the screen
    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(240)

# Quit pygame
pygame.quit()
