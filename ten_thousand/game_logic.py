import random
from collections import Counter
import pygame
from print_functions import delay_print, delay_print_fast, delay_print_sound

class GameLogic:
    @staticmethod
    def calculate_score(dice):
        """
        Calculate the score for a given roll of dice.

        :param dice: Tuple of integers representing dice rolls.
        :return: Integer score based on the game's rules.
        """
        # Count the frequency of each die value in the dice roll.
        counts = Counter(dice)

        # Initialize the score variable to 0.
        score = 0

        # Check if the roll is a straight (one of each die from 1 to 6).
        if len(counts) == 6:
            return 1500  # Return 1500 points for a straight.

        # Check if the roll consists of three pairs.
        if len(counts) == 3 and all(count == 2 for count in counts.values()):
            return 1500  # Return 1500 points for three pairs.

        # Check if the roll consists of two triplets.
        if len(counts) == 2 and all(count == 3 for count in counts.values()):
            return 1200  # Return 1200 points for two triplets.

        # Iterate over each distinct die value and its count in the roll.
        for num, count in counts.items():
            # Scoring rules for ones.
            if num == 1:
                # If there are three or more ones, score 1000 for the first three, plus 1000 for each additional one.
                if count >= 3:
                    score += 1000 + (1000 * (count - 3))
                else:
                    score += count * 100  # If less than three ones, score 100 points for each.
            
            # Scoring rules for fives.
            elif num == 5:
                # If there are three or more fives, score 500 for the first three, plus 500 for each additional five.
                if count >= 3:
                    score += 500 + (500 * (count - 3))
                else:
                    score += count * 50  # If less than three fives, score 50 points for each.
            
            # Scoring rules for other numbers.
            else:
                # If there are three or more of the same number, score 100 times the number for the first three,
                # plus the same score for each additional die of the same number.
                if count >= 3:
                    score += num * 100 + (num * 100 * (count - 3))

        return score  # Return the total calculated score.

    @staticmethod
    def roll_dice(num_dice):
        """
        Roll the dice and return a tuple with the results.

        :param num_dice: An integer between 1 and 6 representing the number of dice to roll.
        :return: A tuple of integers representing the dice roll result.
        """
        # Generate and return a tuple of random integers between 1 and 6, with the number of elements equal to num_dice.
        return tuple(random.randint(1, 6) for _ in range(num_dice))

class GameConfig:
    
    def setup_music(self):
    
        choice = input("Would you like music to be played? Yes/No: ").strip()
        
        if choice.lower() in ['yes', 'y']:
            pygame.mixer.init()
            pygame.mixer.music.load("ten_thousand\Shnabubula - VGMCAST Vol. 8 - 01 Final Fantasy VIII - Shuffle or Boogie.mp3")
            pygame.mixer.music.play(-1)
        
        if choice.lower() in ['n', 'no']:
            
            print("No worries, maybe next time.")
        else:
            print("No worries, maybe next time.")

class Game:
    
    def __init__(self):
        pass
    
    def play_game(self):        
        print("We are playing.")

    def rules(self):        
        delay_print("Ngl I don't understand it completely so just listen to your heart...")

    def intro(self):
        print()
        delay_print("Howdy friend, I see you're awake . . .")
        delay_print("Got caught crossing the border too huh . . .")
        delay_print("Well we probably don't have that much time until we go to jail.")
        print()
        delay_print("Let's say we play a game? What do you say? Yes/No")
        choice = input()
        
        print()
        if choice.lower() in ['yes', 'y']:
            delay_print("Hell yeah, I think it's called Farkle or something.")
        
        elif choice.lower() in ['no', 'n']:
            delay_print("Understandable, I too like to think about how cozy my prison bed will be.")
            delay_print("You take care now, I'll play by myself.")
            exit()

        else:
            delay_print("Sorry I didn't quite get that, but you look like a gamer anyways so we'll just play Farkle.")
    
    def who_am_I(self, asked):
        print("I am me")
    
    def menu(self):
    
        asked = 0
        
        delay_print("Well we got some time to kill, got anything questions before we start?")
        
        while True:
            
            print()
            print("\t1.  Play Game")
            print("\t2.  Rules")
            print("\t3.  Who are you?")
            print("\t4.  Quit")
            
            choice = input("Option: ")
            
            if choice == "1" or choice.lower() in ['one']:
                self.play_game()
            elif choice == "2" or choice.lower() in ['two']:
                self.rules()
            elif choice == "3" or choice.lower() in ['three']:
                self.who_am_I(asked)
            elif choice == "4" or choice.lower() in ['four']:
                delay_print(". . . well thanks for getting my hopes up, I hope you trip on a lego.")
                exit()
            else:
                delay_print("Sorry I didn't catch that can you repeat that? (Invalid Response)")

        
# def main():
    
#     pygame.mixer.init()
#     config()
#     intro()
#     menu()
    
# if __name__ == "__main__":

