'''
    KHL - week 5
    pygame
    screen_sonic.py file
'''
import pygame
from pygame import Color, Surface, Rect

class Screen():
    def __init__(self):
        self.bg_colour = Color(63, 0, 200);
        self.surf = pygame.display.get_surface()
        surf_rect = self.surf.get_rect()
        #this is where code will go
        rect_size = 206
        temp_rect = Rect(295, 118, rect_size, rect_size)
        temp_img = pygame.image.load("../assets/images/sonic-ball.jpg").subsurface(temp_rect)
        self.ball = Surface((rect_size, rect_size), pygame.SRCALPHA)
        pygame.draw.circle(self.ball, Color(255, 255, 255),
                           self.ball.get_rect().center, int(rect_size/2))
        self.ball.blit(temp_img,(0,0), None, pygame.BLEND_RGBA_MULT)
        self.coords = [int(surf_rect.width/2), int(surf_rect.height/2)]
        self.speeds = [2, 2]
        
    def update(self):
        self.coords[0] += self.speeds[0]
        self.coords[1] += self.speeds[1]
        if 0 > self.coords[0]  or self.coords[0] > self.surf.get_rect().width:
            self.speeds[0] *= -1
        if 0 > self.coords[1] or self.coords[1]  > self.surf.get_rect().height:
            self.speeds[1] *= -1
        self.ball.get_rect().center = (self.coords[0], self.coords[1])

    def render(self):
        self.surf.fill(self.bg_colour)
        rect_coords = self.ball.get_rect()
        rect_coords.center = tuple(self.coords)
        self.surf.blit(self.ball, rect_coords)

if __name__ ==  "__main__":
    print("Wrong module. Run the \"app.py\" file to start game")
