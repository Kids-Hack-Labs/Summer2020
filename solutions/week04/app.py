'''
    Kids Hack Labs
    Summer 2020 - Week 03 code
    TaskA: Create an app entry point file
'''
from game_env import Game

def main():
    g = Game((1280, 800), "Week 03")
    g.run()
    
if __name__ == "__main__":
    main()
'''
    OBS.: In the future, we will mix in more
          Python features, so...
          ...take care of these files well
'''
