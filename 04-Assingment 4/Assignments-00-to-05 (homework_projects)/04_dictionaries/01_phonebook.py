def read_phone_numbers():
    """
    Ask the user for names/numbers to story in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}

    while True:
        name = input("Enter name: ")
        if name == "":
            break
        number = input("Enter number: ")
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")

def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """

    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name in phonebook:
            print(f"{name} -> {phonebook[name]}")
        else:
            print(f"{name} not found in phonebook.")
            break

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()