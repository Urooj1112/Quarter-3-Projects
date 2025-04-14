def main():
    numbers:list = [1,2,3,4,5]

    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2

    print(numbers)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()