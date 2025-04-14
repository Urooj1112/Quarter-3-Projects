def get_user_data():
    fname = input("What is your first name?: ")
    lname = input("What is your last name?: ")
    email = input("What is your email address?: ")

    return fname,lname,email

def main():
    user_data = get_user_data()
    print("Received the following user data: ", user_data)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()