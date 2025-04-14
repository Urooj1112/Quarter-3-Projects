INCHES_IN_FOOT = 12

def main():
    feet = float(input("Enter number of feet: "))
    inches = INCHES_IN_FOOT * feet
    print(f"{inches} inches in {feet} feets")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()