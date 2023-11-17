import random

while True:
    user_choice = input("Enter a choice in (rock, paper, scissor): ")
    
    possible_choices = ["rock", "paper", "scissor"]
    computer_choice = random.choice(possible_choices)
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice.lower() == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice.lower() == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice.lower() == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    print()
    play_again = input("If you want to Play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

