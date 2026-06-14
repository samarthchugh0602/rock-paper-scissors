import random
import time
def play_rock_paper_scissors():
    
    player_choices = ["rock", "paper", "scissors", "r", "p", "s"]
    
    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choices)
    
    player_choice = ""
    while player_choice not in player_choices:
        print("Rock")
        time.sleep(0.4)
        print("Paper")
        time.sleep(0.4)
        print("Scissor")
        time.sleep(0.4)
        print("Shoot")
        player_choice = input("Choose rock, paper, or scissors: ").lower().strip()
        if player_choice not in player_choices:
            print("Invalid choice. Please type 'rock', 'paper', or 'scissors'.")

    print(f"\nYou chose: {player_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")

    
    if player_choice == computer_choice:
        print("It's a tie!")
    if player_choice == r and computer_choice == rock:
        print("It's a tie!")
    if player_choice == p and computer_choice == paper:
        print("It's a tie!")
    if player_choice == s and computer_choice == scissors:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"): #or \
         
         """(player_choice == "r" and computer_choice == "scissors") or \
         (player_choice == "s" and computer_choice == "paper") or \
         (player_choice == "p" and computer_choice == "rock"): """
    else:
        print("Computer wins!")
    print("-" * 30)

def main():
    
    print("--- Welcome to Rock, Paper, Scissors! ---")
    
    while True:
        play_rock_paper_scissors()
        
        play_again = input("Play again? (yes/no): ").lower().strip()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
