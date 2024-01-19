import random
from collections import Counter
import pygame
from ten_thousand.print_functions import delay_print, delay_print_fast, delay_print_sound

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
    
    @staticmethod
    def setup_music():
    
        choice = input("Would you like music to be played? Yes/No: ").strip()
        
        if choice.lower() in ['yes', 'y']:
            pygame.mixer.init()
            pygame.mixer.music.load("ten_thousand\Shnabubula - VGMCAST Vol. 8 - 01 Final Fantasy VIII - Shuffle or Boogie.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.5)
            return
        
        if choice.lower() in ['n', 'no']:
            
            print("No worries, maybe next time.")
        else:
            print("No worries, maybe next time.")

class Game:
    
    def __init__(self, test_mode=False):
        self.test_mode = test_mode
    
    def valid_kept_dice(self, kept_dice, dice_roll):
        
        
        """
        Check if the kept dice are a valid subset of the rolled dice.

        This function ensures that the dice chosen to be kept by the player are
        actually part of the dice that were rolled.

        Args:
            kept_dice (tuple): A tuple of integers representing the dice kept by the player.
            dice_roll (list): A list of integers representing the dice rolled.

        Returns:
            bool: True if the kept dice are valid, False otherwise.
        """
        
        # Check if kept_dice are a valid subset of dice_roll
        roll_counter = Counter(dice_roll)
        kept_counter = Counter(kept_dice)
        for die, count in kept_counter.items():
            if roll_counter[die] < count:
                return False
        return True
    def play_game(self, roller=None, max_rounds=20):    
        """
        Play the 'Ten Thousand' dice game.

        The function handles the gameplay logic, including rolling dice, keeping score,
        and interacting with the player to make game decisions.

        Args:
            roller (function, optional): A function to simulate dice rolls. If None,
                                        the default GameLogic.roll_dice is used.

        The game continues until the player decides to quit or the end condition is met.
        """
        
        if roller is None:
            roller = GameLogic.roll_dice

        total_score = 0
        round_number = 1
        playing = True

        print("Welcome to Ten Thousand")
        choice = input("(y)es to play or (n)o to decline\n> ")
        if choice.lower() != 'y':
            print("OK. Maybe another time")
            return

        while playing:
            print(f"Starting round {round_number}")
            num_dice = 6
            round_score = 0
            round_rolls = []

            while num_dice > 0:
                dice_roll = roller(num_dice)
                round_rolls.extend(dice_roll)
                print("***", " ".join(map(str, dice_roll)), "***")

                keep = input("Enter dice to keep, or (q)uit:\n> ")
                if keep.lower() == 'q':
                    playing = False
                    break

                kept_dice = tuple(map(int, keep))  # Convert 'keep' to a tuple of integers
                if self.valid_kept_dice(kept_dice, round_rolls):
                    points = GameLogic.calculate_score(kept_dice)
                    round_score += points
                    num_dice -= len(kept_dice)
                    round_rolls = [die for die in round_rolls if die not in kept_dice]
                    print(f"You have {points} points with the current dice.")
                else:
                    print("Invalid dice selection. Please choose again.")
                    continue  # Skip the rest of the loop and prompt for dice again

                print(f"You have {round_score} unbanked points and {num_dice} dice remaining")
                if num_dice == 0:
                    print("You've used all your dice. Time to bank your points.")
                    break

                decision = input("(r)oll again, (b)ank your points or (q)uit:\n> ")
                if decision.lower() == 'b':
                    total_score += round_score
                    print(f"You banked {round_score} points in round {round_number}")
                    print(f"Total score is {total_score} points")
                    break
                elif decision.lower() == 'q':
                    playing = False
                    break

            if playing:
                round_number += 1

        print(f"Thanks for playing. You earned {total_score} points")

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
    
    def menu(self, roller, max_rounds):
    
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
                self.play_game(roller, max_rounds)
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

