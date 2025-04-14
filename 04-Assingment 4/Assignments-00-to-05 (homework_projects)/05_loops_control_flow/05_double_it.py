def main():
    current_value = int(input("enter a number to double: "))

    while current_value < 100:
        current_value *= 2
        print(current_value)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()