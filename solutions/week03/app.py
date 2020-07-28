'''
    Kids Hack Labs
    Summer 2020 - Week 03 code
    TaskA: Create an app entry point file
'''
#1. Game module import (NOT pygame)
from game_env import Game

#2. Main function definition
#   2.1. Create a Game-type variable
#        (Remember to pass setup parameters)
#   2.2. Call the run() function in the variable
def main():
    print("entered main()")
    g = Game((1024, 768), "Week 03")
    g.run()
    print("exited main()")
    
#3. Check whether this is the application entry point
#   (if it is):
#   3.1 Call the main() function
if __name__ == "__main__":
    print("Module name is", __name__)
    main()
'''
    OBS.: In the future, we will mix in more
          Python features, so...
          ...take care of these files well
'''
