def average(first_num: float, second_num: float):
    return (first_num + second_num) / 2

def main():
    avg_1 = average(40,5)
    avg_2 = average(10,15)

    final_avg = average(avg_1, avg_2)
    
    print("Average 1", avg_1)
    print("Average 2", avg_2)
    print("Final Average", final_avg)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()