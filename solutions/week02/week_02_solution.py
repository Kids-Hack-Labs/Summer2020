'''
    Kids Hack Labs
    Summer 2020 - Week 02 code
    Task: Create a pygame window from scratch,
          add images and blend them
'''
#1. Module imports
import sys, pygame

#2. Define a cleanup function which should quit pygame and
#   exit to the OS
def cleanup():
    pygame.quit()
    sys.exit()

#3. Define the application main entry point
def main():

#2. Pygame initialization and window size/title settings
#   OBS.: remember to store the window in a variable
    pygame.init()
    window_size = (600, 600)
    caption = "Week 2"

    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption(caption)
    
#3. Create the variables needed for today's program
#   3.1. Load two images and store them in variables
#        OBS.: One of the images should be large enough
#              to be used as a background
#   3.2. Create an extra square Surface with the SRCALPHA
#        flag set. Remember to store it in a variable
#   3.3. Draw a white circle on the extra surface
#   3.4. Store all the Surfaces' rectangles in variables
    back_image = pygame.image.load("../assets/images/patates.jpg")
    temp_rect = pygame.Rect(25, 20, 150, 150)
    front_image = pygame.image.load("../assets/images/education.jpg").subsurface(temp_rect)
    front_rect = front_image.get_rect()
    circle_surface = pygame.Surface((front_rect.width, front_rect.height), pygame.SRCALPHA)
    circle_rect = circle_surface.get_rect()
    pygame.draw.circle(circle_surface, pygame.Color(255, 255, 255), circle_rect.center, int(circle_rect.width/2))
    circle_surface.blit(front_image, (0, 0), None, pygame.BLEND_RGBA_MULT)

#4. Create a variable to hold the application's current
#   state. Hint: it should be a boolean for now

    is_running = True

#5. While the application is running, poll the event list
#   for quit-type events.
#   IN CASE OF A QUIT EVENT:
#       flag the application state to stop running!
    
    while is_running:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                is_running = False
### WARNING: one of the steps below is a misstep! ###
#   5.1. Blit the largest image onto the screen
#   5.2. Blit the Surface with the front image onto the surface
#        with the circle using a blend mode of your choosing
#   5.3. Blit the second image onto the middle of the screen
#   5.4. Do not forget to swap the display buffers!
        screen.fill((0, 0, 0))
        screen.blit(back_image, (0, 0))
                                
        positions = [(225, 100), (225, 325)]
        
        screen.blit(circle_surface, positions[0])
        screen.blit(circle_surface, positions[1], None, pygame.BLEND_RGBA_MULT)
        
        pygame.display.flip()
        
#6. Call the cleanup function

    cleanup()
    
#7. Check whether the current file is being executed as the
#   main module
#   7.1 If it is, invoke the application's main entry point

if __name__ == "__main__":
    main()
    
#CHALLENGES:
#1. Test different blend modes of the same image
#   Hint: offset the coordinate values on the blit calls
#2. Move the (smaller) image around with keys
