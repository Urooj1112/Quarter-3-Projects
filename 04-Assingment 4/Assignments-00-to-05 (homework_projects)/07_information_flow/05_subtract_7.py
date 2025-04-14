def subtract_seven(num):
    return num - 7

def main():
    num: int = 10
    num = subtract_seven(num)
    print(num)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()