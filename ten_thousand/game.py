from game_logic import GameLogic
from collections import Counter

def play(roller=None):
    
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
            if valid_kept_dice(kept_dice, round_rolls):
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

def valid_kept_dice(kept_dice, dice_roll):
    
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

# To test the game with the real dice roller
play()
