def get_user_numbers():
    """
    Create an empty list.
    Ask the user to input numbers and store them in a list. 
    Once they enter a blank line, break out of the loop and return the list.
    """
    user_numbers = []
    
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        user_numbers.append(int(user_input))

    return user_numbers

def count_nums(num_list):
    """
    Create an empty dictionary.
    Loop over the list of numbers. 
    If the number is not in the dictionary, add it as a key with a value of 1.
    If the number is in the dictionary, increment its value by 1.
    """
    num_counts = {}
    for num in num_list:
        if num not in num_counts:
            num_counts[num] = 1
        else:
            num_counts[num] += 1
    
    return num_counts

def print_counts(num_dict):
    """
    Loop over the dictionary and print out each key and its value.
    """
    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")


def main():
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()