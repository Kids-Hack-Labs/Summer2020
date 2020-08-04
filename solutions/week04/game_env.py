'''
    Kids Hack Labs
    Summer 2020 - Week 04
    Task: Blend 2 images and allow the user tos
          take a screenshot using the mouse button
'''
#Using last class's files as a base,
#modify the Game class to load and blend 2 images
#The second image should move with the mouse
#using the left mouse button should enable the user
#to take a screenshot of the current game scene

import pygame, sys

class Game:
    def __init__(self, screen_size, screen_caption):
        pygame.init()

        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption(screen_caption)

        #Answers
        self.back_image = pygame.image.load("../assets/images/patates.jpg")

        temp_rect = pygame.Rect(25, 20, 150, 150)
        self.front_image = pygame.image.load("../assets/images/education.jpg")\
                      .subsurface(temp_rect)
        self.front_rect = self.front_image.get_rect()
    
        self.circle_surface = pygame.Surface((self.front_rect.width, self.front_rect.height),
                                         pygame.SRCALPHA)
        self.circle_rect = self.circle_surface.get_rect()
    
        pygame.draw.circle(self.circle_surface, pygame.Color(255, 255, 255),
                           self.circle_rect.center, int(self.circle_rect.width/2))
        self.circle_surface.blit(self.front_image, (0, 0), None, pygame.BLEND_RGBA_MULT)

        self.positions = [pygame.Rect(350,25, 0, 0)]
        for i in range(5):
            self.positions.append(((53+i*253), 225))
            self.positions.append(((53+i*253), 425))
            self.positions.append(((53+i*253), 625))

        self.positions.append((775, 25))

        self.offset = [0,0]

        #screenshot functionality
        self.should_screenshot = False

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

        self.offset = [0,0]
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            self.offset[1] -=1
        if pressed_keys[pygame.K_s]:
            self.offset[1] +=1
        if pressed_keys[pygame.K_a]:
            self.offset[0] -=1
        if pressed_keys[pygame.K_d]:
            self.offset[0] += 1

        if pygame.mouse.get_pressed()[0]:
            self.should_screenshot = True
        
    def update(self):
        self.positions[0].x += self.offset[0]
        self.positions[0].y += self.offset[1]
        
    def render(self):
        self.screen.fill((0, 32, 63))

        self.screen.blit(self.back_image, (0,0))

        self.screen.blit(self.circle_surface, self.positions[0])

        #All comparisons are vertical, with RGB blends on top, RGBA at the bottom
        #Challenge 7.1
        #RGB/A comparison for ADD
        self.screen.blit(self.circle_surface, self.positions[1], None, pygame.BLEND_ADD)
        self.screen.blit(self.circle_surface, self.positions[2], None, pygame.BLEND_RGB_ADD)
        self.screen.blit(self.circle_surface, self.positions[3], None, pygame.BLEND_RGBA_ADD)

        #RGB/A comparison for SUB
        self.screen.blit(self.circle_surface, self.positions[4], None, pygame.BLEND_SUB)
        self.screen.blit(self.circle_surface, self.positions[5], None, pygame.BLEND_RGB_SUB)
        self.screen.blit(self.circle_surface, self.positions[6], None, pygame.BLEND_RGBA_SUB)
        
        #RGB/A comparison for MAX
        self.screen.blit(self.circle_surface, self.positions[7], None, pygame.BLEND_MAX)
        self.screen.blit(self.circle_surface, self.positions[8], None, pygame.BLEND_RGB_MAX)
        self.screen.blit(self.circle_surface, self.positions[9], None, pygame.BLEND_RGBA_MAX)
        
        #RGB/A comparison for MIN
        self.screen.blit(self.circle_surface, self.positions[10], None, pygame.BLEND_MIN)
        self.screen.blit(self.circle_surface, self.positions[11], None, pygame.BLEND_RGB_MIN)
        self.screen.blit(self.circle_surface, self.positions[12], None, pygame.BLEND_RGBA_MIN)
        
        #RGB/A comparison for MULT
        self.screen.blit(self.circle_surface, self.positions[13], None, pygame.BLEND_MULT)
        self.screen.blit(self.circle_surface, self.positions[14], None, pygame.BLEND_RGB_MULT)
        self.screen.blit(self.circle_surface, self.positions[15], None, pygame.BLEND_RGBA_MULT)

        #BLEND_PREMULTIPLIED
        self.screen.blit(self.circle_surface, self.positions[16], None, pygame.BLEND_PREMULTIPLIED)

        if self.should_screenshot:
            self.should_screenshot = False
            pygame.image.save(self.screen, "../assets/screenshots/screencap.png")
            
        pygame.display.flip()

    def cleanup(self):
        pygame.quit()
        sys.exit()
