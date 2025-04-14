def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """
    print(lst[0])

def get_list():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please Enter an element of the list or press enter to stop.")
    while elem != "":
        lst.append(elem)
        elem = input("Please Enter an element of the list or press enter to stop.")
    return lst

def main():
    lst = get_list()
    get_first_element(lst)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()