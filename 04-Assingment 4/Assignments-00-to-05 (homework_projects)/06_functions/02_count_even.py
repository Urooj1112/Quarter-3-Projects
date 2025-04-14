def make_list():
    lst = []
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":
        lst.append(int(user_input))
        user_input = input("Enter an integer or press enter to stop: ")
    return lst

def count_even(lst):
    count = 0

    for i in range(len(lst)):
        num = lst[i]
        if num % 2 == 0:
            count += 1
    print(count)


def main():
    lst = make_list()
    count_even(lst)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()