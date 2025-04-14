def in_range(n,low,high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

def main():
    print(in_range(5,6,10))
    print(in_range(11,10,20))

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()