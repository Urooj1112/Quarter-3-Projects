def main():
    user_num = int(input("Enter a Number to double: "))
    while user_num < 100:
        user_num *= 2
        print(user_num, end=" ")

    
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()