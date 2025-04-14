MAX_LENGTH = 3

def shorten(lst:list):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print("Removed: ",removed_item)
    return lst

def get_list():
    list = []
    elem = input("Please Enter an element of the list or press enter to stop.")
    while elem != "":
        list.append(elem)
        elem = input("Please Enter an element of the list or press enter to stop.")
    return list

def main():
    list = get_list()
    shortened_list = shorten(list)
    print(shortened_list)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()