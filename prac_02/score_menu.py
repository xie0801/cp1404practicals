"""
CP1404/CP5632 - Practical
Score Menu Program
"""

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

def get_valid_score():
    """Get a valid score between 0 and 100 from the user."""
    score = float(input("Enter score (0-100): "))
    while not (0 <= score <= 100):
        print("Invalid input. Please enter a score between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score

def print_stars(score):
    """Print stars equal to the score length."""
    print("*" * int(score))

def main():
    """Main function to execute the score menu program."""
    MENU = """(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"""
    print(MENU)
    score = get_valid_score()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_status(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Finished.")

if __name__ == "__main__":
    main()
