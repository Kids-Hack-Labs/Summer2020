'''
    KHL - week 6
    pygame
    screen.py file
'''
import pygame
from pygame import Color, Surface, Rect
from ball import Ball
#from paddle import RPaddle, LPaddle

class Screen():
    def __init__(self):
        self.bg_colour = Color(63, 0, 200)
        self.surf = pygame.display.get_surface()
        surf_rect = self.surf.get_rect()
        #Last week's code needs to be transferred
        # to the Paddle class in the paddle.py file

        #PART 2: ADD PADDLES!
        
    def update(self):
        #Last week's code needs to be transferred
        # to the Paddle class in the paddle.py file

        #PART 2: ADD PADDLES!
        pass
    
    def render(self):
        self.surf.fill(self.bg_colour)
        #Last week's code needs to be transferred
        # to the Paddle class in the paddle.py file

        #PART 2: ADD PADDLES!

if __name__ ==  "__main__":
    print("Wrong module. Run the \"app.py\" file to start game")
