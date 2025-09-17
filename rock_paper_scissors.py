import random

def determine_winner(player_choice, computer_choice):
    """Determine the winner of a round"""
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if player_choice == computer_choice:
        return "tie"
    elif winning_combinations[player_choice] == computer_choice:
        return "player"
    else:
        return "computer"

def main():
    choice_map = {'r': 'rock', 'p': 'paper', 's': 'scissors', 'rock': 'rock', 'paper': 'paper', 'scissors': 'scissors'}
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0
    
    print("Welcome to Rock Paper Scissors!")
    print("=" * 30)
    
    while True:
        user_input = input("\nEnter (r)ock, (p)aper, (s)cissors or 'quit' to exit: ").lower()
        if user_input == 'quit':
            break
        
        player_choice = choice_map.get(user_input)
        if not player_choice:
            print("Invalid input. Please enter r, p, s, or quit.")
            continue
        
        # Computer makes random choice
        computer_choice = random.choice(choices)
        
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine winner
        result = determine_winner(player_choice, computer_choice)
        
        if result == "player":
            player_score += 1
            print("You win this round!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")
        
        # Display current score
        print(f"\nCurrent Score - You: {player_score}, Computer: {computer_score}")
    
    print(f"\nFinal Score - You: {player_score}, Computer: {computer_score}")
    if player_score > computer_score:
        print("Congratulations! You won overall!")
    elif computer_score > player_score:
        print("Computer won overall! Better luck next time!")
    else:
        print("It's a tie overall! Great game!")

if __name__ == "__main__":
    main()
