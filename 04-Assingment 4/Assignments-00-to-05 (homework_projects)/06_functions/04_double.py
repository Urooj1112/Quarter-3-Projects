def double_num(num):
    return num * 2


def main():
    num = int(input("Enter a number: "))
    doubled_num = double_num(num)
    print(doubled_num)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

print(__name__)