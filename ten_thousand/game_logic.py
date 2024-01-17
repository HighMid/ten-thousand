import random
from collections import Counter

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
