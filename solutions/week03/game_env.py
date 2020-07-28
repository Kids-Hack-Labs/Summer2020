'''
    Kids Hack Labs
    Summer 2020 - Week 03 code
    TaskB: Create an app entry point file
'''
#1. Module imports
import pygame, sys

#2. Game class creation:
#   2.1. Initializer definition:
#       2.1.1. pygame initialization
#       2.1.2. Game variables initialization
#              based on initializer function
#              (remember to create a variable to
#              control the game loop)
class Game:
    def __init__(self, screen_size, screen_caption):
        print("\tGame created")
        pygame.init()

        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption(screen_caption)

        self.is_running = True
        print("\tGame initialized")

#   2.2. run function creation
#       2.2.1. the run() function should only
#              contain four other functions
#              (for now), three in the main loop
#              and the last one outside. The
#              functions are:
#                  process_events()
#                  update()
#                  render()
#              cleanup()
    def run(self):
        print("\tentered run()")
        while self.is_running:
            print("\t\trun loop")
            self.process_events()
            self.update()
            self.render()
        print("\t\tself.is_running loop ended...\n",
              "\t\tproceeding to cleanup()")
        self.cleanup()
        
#   2.3. process_events function creation
#       2.3.1. This function should contain all
#              the event management functionality,
#              including polling the event queue
#              for quit-type events, and flagging
#              the game class accordingly
    def process_events(self):
        print("\t\t\tentered event processing function...\n",
              "\t\t\t\tpolling event queue")
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                print("\t\t\t\t\tquit command issued")
                self.is_running = False
                print("\t\t\t\t\tset self.is_running to False")
    
#   2.4. update function creation
#       2.4.1. This function should take care of 
#              managing the state updates, based on
#              the events handled in process_events()
    def update(self):
        print("\t\t\tupdating")
        
#   2.5. render function creation
#       2.5.1. This function should take care of 
#              passing things to the display, as well
#              swapping the display buffers.
#              optional: before swapping displays,
#              fill the screen with your favourite colour
    def render(self):
        print("\t\t\trendering")
        self.screen.fill((0, 32, 63))
        pygame.display.flip()
        print("\t\t\tswapped buffers")
        
#   2.6. cleanup function creation
#       2.6.1. This function should take care of 
#              de-initializing pygame and exiting
#              to the operating system
    def cleanup(self):
        print("\tcleaning up... bye")
        pygame.quit()
        sys.exit()
