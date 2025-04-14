import random 

def main():
    secret_number = random.randint(1,99)

    print("I am thinking of a number between 1 and 99...")
    guess = int(input("Enter a guess: "))
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")

        print()
        guess = int(input("Enter a new guess: "))

    print(f"Congrats! The number was: {secret_number}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()