def main():
    first_num = int(input("Please enter an integer to be divided: "))
    second_num = int(input("Please enter an integer to be divided: "))

    division_result = first_num // second_num
    remainder = first_num % second_num
    
    print(f"The result of this division is {division_result} with a remainder of {remainder}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()