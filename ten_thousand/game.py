from ten_thousand.game_logic import GameConfig, Game
from collections import Counter
import pygame

def play():
    
    max_rounds = 20
    roller = None
    
    
    pygame.mixer.init()
    
    print()
    
    game = Game()
    # game_config = GameConfig()
    
    game.play_game()
    # game_config.setup_music()
    game.intro()
    game.menu(roller, max_rounds)
    

play() 