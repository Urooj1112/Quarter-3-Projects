ADULT_AGE:int = 18

def is_adult(age:int) -> bool:
    if age >= ADULT_AGE:
        return True
    else:
        return False

def main():
    age: int = int(input("How old is this person?: "))
    print(is_adult(age))
    
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()