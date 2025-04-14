def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    total_cost = 0

    for fruitname in fruits:
        price = fruits[fruitname]
        amount_bought = int(input(f"How many ({fruitname}) do you want to buy?: "))
        total_cost += price * amount_bought
    
    print(f"Your total is ${total_cost}")



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()