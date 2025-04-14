def print_divisors(num):
    print(f"Here are the divisors of {num}")
    for i in range(1,num + 1):
        if num % i == 0:
            print(i)

def main():
    user_int = int(input("Enter a number:"))
    print_divisors(user_int)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()