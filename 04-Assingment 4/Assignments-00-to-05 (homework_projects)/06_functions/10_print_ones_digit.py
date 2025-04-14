def print_ones_digit(num):
    print(f"The ones digit of {num} is {num % 10}")

def main():
    user_num = int(input("Enter a number:"))
    print_ones_digit(user_num)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()