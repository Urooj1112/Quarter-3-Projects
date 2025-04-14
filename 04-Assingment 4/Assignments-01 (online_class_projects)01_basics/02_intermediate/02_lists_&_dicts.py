# Problem 1: List Practice

# fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
# print(len(fruit_list))
# fruit_list.append("mango")
# print(fruit_list)


# Problem 2: Index Game

def access_element(lst :list, index: int):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst :list, index:int, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst :list, start_index:int, end_index):
    try:
        new_list = lst[start_index:end_index]
        return new_list
    except IndexError:
        return "Invalid indices."
    
def index_game():
    lst = [1, 2, 3, 4, 5]  # Example list
    print("Current list:", lst)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ")

    if operation == "access":
        index = int(input("Enter index to access: "))
        print(access_element(lst, index))
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print(modify_element(lst, index, new_value))
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(lst, start, end))
    else:
        print("Invalid operation.")

index_game()