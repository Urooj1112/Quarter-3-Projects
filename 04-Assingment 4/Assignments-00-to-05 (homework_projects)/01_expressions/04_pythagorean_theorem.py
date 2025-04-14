import math  # Import the math library so we can use the sqrt function

def main():
    # Get the two side lengths from the user and cast them to be numbers
    ab :float = float(input("Enter the length of AB: "))
    ac :float = float(input("Enter the length of AC: "))

    bc :float = math.sqrt(ab**2 + ac**2)
    print(f"The length of BC (the hypotenuse) is: {bc}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()