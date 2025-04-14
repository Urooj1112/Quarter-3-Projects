def num_in_stock(fruit):
    """
    This function returns the number of fruit Sophia has in stock.
    """
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    elif fruit == 'pear':
        return 1000
    else:
        return 0

def main():
    fruit = input("Enter a fruit: ")
    stock = num_in_stock(fruit)
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()