'''
    Summer 2020, Week 1
    Python and pygame review
    Task: create a pygame window from scratch,
          using the instructions below
'''
#1. Modules to import: pygame and sys
import pygame, sys
#Convenience import
from pygame import Surface, Color

#2. Create an application main entry point
def main():
    
#3. Initialize pygame
    pygame.init()

#4. Create a square window with side of 600
#   4.1. Store the returned surface from the step above
#        in a variable
    window_size = (600, 600)
    window_caption = "Week 1 with Challenges"
    screen = pygame.display.set_mode(window_size)
    
#5. Set the window's title to "Week 1"
    pygame.display.set_caption(window_caption)

    ###Reorg and Challenge: variables and images###
    
    #background setup
    bg_colour = Color(0, 50, 100)
    bg_image = pygame.image.load("patates.jpg")

    #Transparent circle setup
    circle_radius = 50
    surf_size = (2*circle_radius, 2*circle_radius)
    surf_center = (circle_radius, circle_radius)
    outline_thickness = 5
    circle_fill = Color(100, 23, 197, 100)
    circle_outline = Color(155, 232, 58, 100)

    #Surface creation for transparent circle
    surf = pygame.Surface(surf_size, pygame.SRCALPHA)
    surf_rect = surf.get_rect()

    #Surface draw for transparent circle
    pygame.draw.circle(surf, circle_fill, surf_center, circle_radius)
    pygame.draw.circle(surf, circle_outline, surf_center,
                       circle_radius, outline_thickness)

    ###End of Reorg and Challenge###
    
#6. Create an infinite while-loop
#   (While the aforementioned loop is running:)
#   6.1. Iterate through pygame's event queue
#       6.1.1. If one of these events is of type QUIT:
#           6.1.1.1. Quit pygame
#           6.1.1.2. Instruct the app to exit
    while True:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
#   6.2. Store the mouse's coordinates in a variable
        surf_rect.center = pygame.mouse.get_pos()

#   6.3. Fill the screen with a colour of your choosing
        screen.fill(bg_colour)
        top_left = (0, 0)
        screen.blit(bg_image, top_left)
        
#   6.4. Draw a circle on the screen that meets the following criteria:
#       6.4.1. It can be of any colour that is not that of the background
#       6.4.2. It must be centered on the mouse
#       6.4.3. It must have a radius of 50
#       6.4.4. It must have a differently-coloured outline,
#              with a thickness of 5

        ###OBS: The setup steps were done after item 5###
        screen.blit(surf, surf_rect)

#   6.5. Call pygame's function that swaps the display buffers
        pygame.display.flip()

#7. Check whether the current file
#   is the application's entry point file
#   (if it is):
#   7.1. Call the application's entry point function
if __name__ == "__main__":
    main()

#REORGANIZE:
#R1. Look through your code, and store all numerical,
#    tuple and text data in variables.
#    Replace the hard-coded function calls with these variables

#CHALLENGE:
#C1. Alter your code so that, instead of a background colour,
#    you load a background image
#    (hint: use variables)
#C2. Alter your code so that the circle that moves with the mouse
#    is semi-transparent
#    (warning: it is not so simple as it sounds)
