'''
    Kids Hack Labs
    Summer 2020 - Week 02 code
    Task: Create a pygame window from scratch,
          add images and blend them
'''
#1. Module imports

#2. Define a cleanup function which should quit pygame and
#   exit to the OS

#3. Define the application main entry point

#2. Pygame initialization and window size/title settings
#   OBS.: remember to store the window in a variable

#3. Create the variables needed for today's program
#   3.1. Load two images and store them in variables
#        OBS.: One of the images should be large enough
#              to be used as a background
#   3.2. Create an extra square Surface with the SRCALPHA
#        flag set. Remember to store it in a variable
#   3.3. Draw a white circle on the extra surface
#   3.4. Store all the Surfaces' rectangles in variables

#4. Create a variable to hold the application's current
#   state. Hint: it should be a boolean for now

#5. While the application is running, poll the event list
#   for quit-type events.
#   IN CASE OF A QUIT EVENT:
#       flag the application state to stop running!

### WARNING: one of the steps below is a misstep! ###
#   5.1. Blit the largest image onto the screen
#   5.2. Blit the Surface with the white cirle onto the second
#        image using a blend mode of your choosing
#   5.3. Blit the second image onto the middle of the screen
#   5.4. Do not forget to swap the display buffers!

#6. Call the cleanup function

#7. Check whether the current file is being executed as the
#   main module
#   7.1 If it is, invoke the application's main entry point

#CHALLENGES:
#1. Test different blend modes of the same image
#   Hint: offset the coordinate values on the blit calls
#2. Move the (smaller) image around with keys
