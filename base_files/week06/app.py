'''
    KHL - Week 6
    pygame
    app.py file
'''
from game_env import Game

def main():
    window_size = (1280, 800);
    game_title = "Week 06: Paddles"
    g = Game(window_size, game_title)
    g.run()

if __name__ == "__main__":
    main()
