"""
Rock Paper Scissors GUI Game using Tkinter
A simple graphical interface for playing Rock Paper Scissors against the computer
with score tracking and visual feedback.
"""
import tkinter as tk
from tkinter import ttk, messagebox
import random


class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Game state
        self.player_score = 0
        self.computer_score = 0
        self.choices = ['rock', 'paper', 'scissors']
        
        # Game logic mappings
        self.winning_combinations = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
        
        # Emojis for visual appeal
        self.choice_emojis = {
            'rock': '🪨',
            'paper': '📄',
            'scissors': '✂️'
        }
        
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the user interface"""
        # Title
        title_label = tk.Label(
            self.root, 
            text="Rock Paper Scissors", 
            font=("Arial", 20, "bold"),
            pady=20
        )
        title_label.pack()
        
        # Score display
        self.score_frame = tk.Frame(self.root)
        self.score_frame.pack(pady=10)
        
        self.score_label = tk.Label(
            self.score_frame,
            text=f"Player: {self.player_score}  |  Computer: {self.computer_score}",
            font=("Arial", 14),
            bg="#f0f0f0",
            padx=20,
            pady=10
        )
        self.score_label.pack()
        
        # Game status display
        self.status_label = tk.Label(
            self.root,
            text="Choose your move!",
            font=("Arial", 12),
            pady=10
        )
        self.status_label.pack()
        
        # Choice display frame
        self.choice_frame = tk.Frame(self.root)
        self.choice_frame.pack(pady=20)
        
        self.player_choice_label = tk.Label(
            self.choice_frame,
            text="You: ",
            font=("Arial", 14)
        )
        self.player_choice_label.grid(row=0, column=0, padx=20)
        
        self.vs_label = tk.Label(
            self.choice_frame,
            text="VS",
            font=("Arial", 12, "bold")
        )
        self.vs_label.grid(row=0, column=1, padx=20)
        
        self.computer_choice_label = tk.Label(
            self.choice_frame,
            text="Computer: ",
            font=("Arial", 14)
        )
        self.computer_choice_label.grid(row=0, column=2, padx=20)
        
        # Button frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        # Game buttons
        rock_button = tk.Button(
            button_frame,
            text=f"{self.choice_emojis['rock']}\nRock",
            font=("Arial", 12),
            width=10,
            height=3,
            command=lambda: self.play_round('rock'),
            bg="#ffcccb"
        )
        rock_button.grid(row=0, column=0, padx=10)
        
        paper_button = tk.Button(
            button_frame,
            text=f"{self.choice_emojis['paper']}\nPaper",
            font=("Arial", 12),
            width=10,
            height=3,
            command=lambda: self.play_round('paper'),
            bg="#add8e6"
        )
        paper_button.grid(row=0, column=1, padx=10)
        
        scissors_button = tk.Button(
            button_frame,
            text=f"{self.choice_emojis['scissors']}\nScissors",
            font=("Arial", 12),
            width=10,
            height=3,
            command=lambda: self.play_round('scissors'),
            bg="#98fb98"
        )
        scissors_button.grid(row=0, column=2, padx=10)
        
        # Control buttons frame
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=20)
        
        # Reset button
        reset_button = tk.Button(
            control_frame,
            text="Reset Score",
            font=("Arial", 10),
            command=self.reset_game,
            bg="#ffeb9c"
        )
        reset_button.grid(row=0, column=0, padx=10)
        
        # Quit button
        quit_button = tk.Button(
            control_frame,
            text="Quit Game",
            font=("Arial", 10),
            command=self.quit_game,
            bg="#ffa07a"
        )
        quit_button.grid(row=0, column=1, padx=10)
    
    def play_round(self, player_choice):
        """Play a single round of the game"""
        # Computer makes random choice
        computer_choice = random.choice(self.choices)
        
        # Update choice display
        self.player_choice_label.config(
            text=f"You: {self.choice_emojis[player_choice]} {player_choice.title()}"
        )
        self.computer_choice_label.config(
            text=f"Computer: {self.choice_emojis[computer_choice]} {computer_choice.title()}"
        )
        
        # Determine winner
        result = self.determine_winner(player_choice, computer_choice)
        
        # Update score and status
        if result == "player":
            self.player_score += 1
            self.status_label.config(text="🎉 You Win This Round!", fg="green")
        elif result == "computer":
            self.computer_score += 1
            self.status_label.config(text="💻 Computer Wins This Round!", fg="red")
        else:
            self.status_label.config(text="🤝 It's a Tie!", fg="orange")
        
        # Update score display
        self.score_label.config(
            text=f"Player: {self.player_score}  |  Computer: {self.computer_score}"
        )
        
        # Check for milestone scores
        self.check_milestones()
    
    def determine_winner(self, player_choice, computer_choice):
        """Determine the winner of a round"""
        if player_choice == computer_choice:
            return "tie"
        elif self.winning_combinations[player_choice] == computer_choice:
            return "player"
        else:
            return "computer"
    
    def check_milestones(self):
        """Check for score milestones and show congratulatory messages"""
        if self.player_score == 5:
            messagebox.showinfo("Milestone!", "🏆 Congratulations! You've won 5 rounds!")
        elif self.computer_score == 5:
            messagebox.showinfo("Milestone!", "🤖 Computer has won 5 rounds! Keep trying!")
        elif self.player_score == 10:
            messagebox.showinfo("Achievement!", "🌟 Amazing! You've won 10 rounds!")
        elif self.computer_score == 10:
            messagebox.showinfo("Challenge!", "💪 Computer has won 10 rounds! Time for a comeback!")
    
    def reset_game(self):
        """Reset the game scores and status"""
        result = messagebox.askyesno("Reset Game", "Are you sure you want to reset the scores?")
        if result:
            self.player_score = 0
            self.computer_score = 0
            self.score_label.config(
                text=f"Player: {self.player_score}  |  Computer: {self.computer_score}"
            )
            self.status_label.config(text="Choose your move!", fg="black")
            self.player_choice_label.config(text="You: ")
            self.computer_choice_label.config(text="Computer: ")
    
    def quit_game(self):
        """Quit the game with confirmation"""
        result = messagebox.askyesno("Quit Game", "Are you sure you want to quit?")
        if result:
            self.root.quit()


def main():
    """Main function to run the game"""
    root = tk.Tk()
    game = RockPaperScissorsGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
