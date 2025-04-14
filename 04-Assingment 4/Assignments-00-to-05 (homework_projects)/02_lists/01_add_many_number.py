def add_many_numbers(numbers:list) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """

    total = 0
    for number in numbers:
        total += number
    
    return total

def main():
    numbers : list[int] = [1,2,3,4,5,6,7,8,9]
    sum_of_numbers = add_many_numbers(numbers)
    print(sum_of_numbers)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()