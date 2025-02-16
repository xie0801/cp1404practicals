"""
CP1404/CP5632 - Practical
Password Stars Program
"""

def get_password(min_length):
    """Get a valid password from the user."""
    password = input("Enter a password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter a password: ")
    return password

def print_asterisks(password):
    """Print asterisks equal to the password length."""
    print("*" * len(password))

def main():
    """Main function to execute the password program."""
    MIN_LENGTH = 6
    password = get_password(MIN_LENGTH)
    print_asterisks(password)

if __name__ == "__main__":
    main()
