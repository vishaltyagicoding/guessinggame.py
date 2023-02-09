import random

computer_guess = random.randint(1, 100)
print("Welcome to the guessing game!")
print("You need to guess the number between 1 to 100!")

label = input("Choose a difficulty? Type 'easy' or 'hard' ").lower()
loop_time = 10
if label == "hard":
    loop_time = 5


def guess():
    for i in range(loop_time, 0, -1):
        print(f"You have {i} attempt remaining to guess the number!")
        user_guess = int(input("Make a guess? "))
        if user_guess == computer_guess:
            print(f"You got it. ans was {computer_guess} !")
            return
        elif user_guess > computer_guess:
            print("Too high \n guess again")
        else:
            print("Too low \n guess again")

    print("You have ran out of the guesses, You lose.")


guess()


