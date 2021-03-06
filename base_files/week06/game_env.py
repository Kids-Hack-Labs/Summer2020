'''
    KHL - Week 6
    pygame
    game_env.py file
'''
import pygame, sys
from screen import Screen

class Game():
    def __init__(self, size, title):
        pygame.init()
        self.canvas = pygame.display.set_mode(size)
        pygame.display.set_caption(title)

        self.current_screen = Screen()
        
        self.is_running = True

    def run(self):
        while self.is_running:
            self.process_events()
            self.update()
            self.render()
        self.cleanup()

    def process_events(self):
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        self.current_screen.update()

    def render(self):
        self.current_screen.render()
        pygame.display.flip()

    def cleanup(self):
        pygame.quit()
        sys.exit()

if __name__ ==  "__main__":
    print("Wrong module. Run the \"app.py\" file to start game")
