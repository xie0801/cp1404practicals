"""
CP1404/CP5632 - Practical
Temperature Conversion Program
"""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def main():
    """Temperature conversion program with menu options."""
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    while True:
        choice = input(">>> ").upper()
        if choice == "Q":
            break
        elif choice == "C":
            celsius = float(input("Celsius: "))
            print(f"Result: {celsius_to_fahrenheit(celsius):.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print(f"Result: {fahrenheit_to_celsius(fahrenheit):.2f} C")
        else:
            print("Invalid option")
        print(MENU)
    print("Thank you.")

if __name__ == "__main__":
    main()
