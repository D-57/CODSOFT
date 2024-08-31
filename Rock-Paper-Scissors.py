import random

choices = [1,2,3]


user_score = 0
computer_score = 0

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (computer_choice==1 and user_choice==3)or(computer_choice==2 and user_choice==1)or(computer_choice==3 and user_choice==2):
        return "comp"
    else:
        return "user"

while True:
    user_choice = int(input("1 for Rock\n2 for paper\n3 for scissors\nEnter your choice:"))
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)
    if computer_choice==1:
        print("Computer chose: Rock")
    elif computer_choice==2:
        print("Computer chose: Paper")
    else :
        print("Computer chose: Scissors")

    winner = get_winner(user_choice, computer_choice)
    if winner == "user":
        print("You win this round!")
        user_score += 1
    elif winner == "comp":
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("It's a tie!")

    print(f"Score: You {user_score} - {computer_score} Computer")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        break

print(f"Final Score: You {user_score} - {computer_score} Computer")
print("Thanks for playing!")