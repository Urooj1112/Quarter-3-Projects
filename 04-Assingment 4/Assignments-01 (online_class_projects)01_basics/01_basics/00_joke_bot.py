PROMPT = "What do you want?"
JOKE = "Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY = "Sorry I only tell jokes"

def main():
    print("Welcome to the Joke Bot.")
    user_input = input(PROMPT).strip().lower()
    if "joke" in user_input:
        print(JOKE)
    else:
        print(SORRY)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()