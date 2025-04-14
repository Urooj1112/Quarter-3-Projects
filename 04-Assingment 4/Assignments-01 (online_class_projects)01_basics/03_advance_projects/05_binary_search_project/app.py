import time
import random

def native_search(l,target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    
    if high < low:
        return -1
    
    midpoint = (low + high) // 2
    if l[midpoint] == target:
        return midpoint
    elif l[midpoint] > target:
        return binary_search(l, target, low, midpoint - 1)
    else:
        return binary_search(l, target, midpoint + 1, high)

if __name__ == "__main__":
    length = 5000
    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length , 3*length))
    sorted_list = sorted(list(sorted_list))

    start_time = time.time()
    for target in sorted_list:
        result = native_search(sorted_list, target)
    end_time = time.time()
    print(f"Native search time: {(end_time - start_time) / length:.9f} seconds")

    start_time = time.time()
    for target in sorted_list:
        result = binary_search(sorted_list, target)
    end_time = time.time()
    print(f"Binary search time: {(end_time - start_time) / length:.9f} seconds")