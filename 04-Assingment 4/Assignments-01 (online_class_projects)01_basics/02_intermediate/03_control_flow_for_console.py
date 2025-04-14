import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    score = 0

    for i in range(NUM_ROUNDS):
        computer_num = random.randint(1,100)
        user_num = random.randint(1,100)
        print('--------------------------------')
        print(f"Round {i + 1}")
        print(f"Your number is {user_num}")

        user_answer = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

        while user_answer not in ["higher", "lower"]:
            user_answer = input("Please enter either higher or lower: ").strip().lower()

        higher_and_correct = user_answer == "higher" and user_num > computer_num
        lower_and_correct = user_answer == "lower" and user_num < computer_num

        if higher_and_correct or lower_and_correct:
            print(f"You were right! The computer's number was {computer_num}")
            score += 1
        else:
            print("Aww, that's incorrect. The computer's number was " + str(computer_num))

        print(f"Your score is now {score}")
    
    print("Your final score is", score)
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score > NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")
    
    print("Thanks for playing!")
        

if __name__ == "__main__":
    main()