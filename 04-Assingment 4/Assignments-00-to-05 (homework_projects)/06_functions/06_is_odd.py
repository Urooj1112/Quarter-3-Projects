def is_odd(num:int):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    remainder = num % 2
    return remainder == 1

def main():
    for i in range(10):
        if is_odd(i):
            print(i, "is odd")
        else:
            print(i, "is even")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()