'''
    Summer 2020, Week 1
    Python and pygame review
    Task: create a pygame window from scratch,
          using the instructions below
'''
#1. Modules to import: pygame and sys
import pygame, sys

#2. Create an application main entry point
def main():
    
#3. Initialize pygame
    pygame.init()

#4. Create a square window with side of 600
#   4.1. Store the returned surface from the step above
#        in a variable
    screen = pygame.display.set_mode((600, 600))
#5. Set the window's title to "Week 1"
    pygame.display.set_caption("Week 1")
    
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
        mouse_pos = pygame.mouse.get_pos()

#   6.3. Fill the screen with a colour of your choosing
        screen.fill((0, 50, 100))
        
#   6.4. Draw a circle on the screen that meets the following criteria:
#       6.4.1. It can be of any colour that is not that of the background
#       6.4.2. It must be centered on the mouse
#       6.4.3. It must have a radius of 50
#       6.4.4. It must have a differently-coloured outline,
#              with a thickness of 5
        pygame.draw.circle(screen, (100, 23, 197), mouse_pos, 50)
        pygame.draw.circle(screen, (155, 232, 58), mouse_pos, 50, 5)

#   6.5. Call pygame's function that swaps the display buffers
        pygame.display.flip()

#7. Check whether the current file is the application's entry point file
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
