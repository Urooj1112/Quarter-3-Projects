import random

DONE_LIKELIHOOD = 0.2

def chaoting_counting():
    for i in range(1,11):
        if is_done():
            return
        print(i)
        
def is_done():
    if random.random() < DONE_LIKELIHOOD:
        return True
    else:
        return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaoting_counting()
    print("I'm done")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()