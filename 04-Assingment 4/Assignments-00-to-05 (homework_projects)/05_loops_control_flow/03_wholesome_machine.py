AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: I am capable of doing anything I put my mind to. ")
    
    user_input = input()
    while user_input != AFFIRMATION:
        print("Hmmm That was not the affirmation.")
        print("Please type the following affirmation: ",AFFIRMATION)
        user_input = input()

    print("That's right! ")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()