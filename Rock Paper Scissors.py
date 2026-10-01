import random

R = "Rock"
P = "Paper"
S = "Scissors"
score=0

def c_c():
    return random.choice((R, P, S))

print("Welcome to Rock Paper Scissors!")
print("Enter your choice (Rock=r, Paper=p, Scissors=s):")
def get_user_choice():
    user_input = input().lower()
    if user_input == 'r':
        return R
    elif user_input == 'p':
        return P
    elif user_input == 's':
        return S
    else:
        print("Invalid input. Please enter 'r', 'p', or 's'.")
        return get_user_choice()

user_choice = get_user_choice()
computer_choice = c_c()

print(f"You chose {user_choice}")
print(f"The computer chose {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == R and computer_choice == S) or \
     (user_choice == P and computer_choice == R) or \
     (user_choice == S and computer_choice == P):
    print("You win!")
    score += 1
else:
    print("You lose!")

print(f"Your score is: {score}")

def again():
    global score
    print("Do you want to play again? (yes/no)")
    again_1 = input().lower()
    if again_1 == 'yes':
        print("Starting a new game...")
        user_choice = get_user_choice()
        computer_choice = c_c()

        print(f"You chose {user_choice}")
        print(f"The computer chose {computer_choice}")

        if user_choice == computer_choice:

            print("It's a tie!")
        elif (user_choice == R and computer_choice == S) or \
             (user_choice == P and computer_choice == R) or \
             (user_choice == S and computer_choice == P):
            print("You win!")
            score += 1
            print(f"Your score is: {score}")
        else:
            print("You lose!")
        again()
    elif again_1 == 'no':
        print("Thanks for playing!")
    else:
        print("Please answer yes or no.")
        again()

again()
