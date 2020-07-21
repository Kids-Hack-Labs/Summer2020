import pygame, sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))

    is_running = True

    while is_running:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                is_running = False

        screen.fill((0, 50, 127))
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
