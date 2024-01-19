from ten_thousand.game_logic import Game
from collections import Counter
# import pygame

def play(roller=None):
    
    max_rounds = 20
    roller = 5
    
    
    # pygame.mixer.init()
    

    game = Game()
    # game_config = GameConfig()
    
    game.play_game(roller=roller, max_rounds=max_rounds)
    # game_config.setup_music()
    # game.intro()
    # game.menu(roller, max_rounds)
    

if __name__ == "__main__":
    play()
 