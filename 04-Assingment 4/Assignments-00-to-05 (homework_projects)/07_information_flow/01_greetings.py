def greet(name):
    return f"Greetings {name}!"

def main():
    user_name = input("What's your name? ")
    print(greet(user_name)) 

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()