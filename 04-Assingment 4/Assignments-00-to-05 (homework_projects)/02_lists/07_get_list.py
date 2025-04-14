def main():
    list = []
    while True:
        user_input = input("Enter a value: ")
        if user_input == "":
            break
        list.append(user_input)
    print("Here is the List: ",list)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()