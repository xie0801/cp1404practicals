"""
CP1404/CP5632 - Practical
Score Classification Program
"""

import random


def determine_score_status(score):
    """Determine the status of the given score."""
    if not (0 <= score <= 100):
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    """Main function to execute the score classification program."""
    score = float(input("Enter score: "))
    print(determine_score_status(score))

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score} - {determine_score_status(random_score)}")


if __name__ == "__main__":
    main()
