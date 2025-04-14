def repeat_message(message, times):
    for i in range(times):
        print(message)

def main():
    user_msg = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    repeat_message(user_msg, repeats)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()