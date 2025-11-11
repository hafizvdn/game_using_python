import tkinter as tk
from tkinter import ttk, messagebox
import random
from typing import Optional

class GameCollection:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Python Games Collection")
        self.root.geometry("400x500")
        self.root.configure(bg='#2c3e50')
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        self.create_main_menu()
    
    def create_main_menu(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Main frame
        main_frame = tk.Frame(self.root, bg='#2c3e50', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="🎮 PYTHON GAMES", 
                              font=('Arial', 20, 'bold'), 
                              fg='#ecf0f1', bg='#2c3e50')
        title_label.pack(pady=20)
        
        # Game buttons
        games = [
            ("🎯 Number Guessing", self.start_number_game, '#e74c3c'),
            ("⭕ Tic-Tac-Toe", self.start_tictactoe, '#3498db'),
            ("🪨📄✂️ Rock-Paper-Scissors", self.start_rps, '#2ecc71'),
            ("🔤 Word Guessing", self.start_word_game, '#f39c12'),
            ("🎲 Memory Game", self.start_memory_game, '#9b59b6')
        ]
        
        for game_name, command, color in games:
            btn = tk.Button(main_frame, text=game_name,
                           command=command,
                           font=('Arial', 12, 'bold'),
                           bg=color, fg='white',
                           width=25, height=2,
                           relief='raised', bd=3,
                           activebackground=self.darken_color(color))
            btn.pack(pady=10)
        
        # Exit button
        exit_btn = tk.Button(main_frame, text="🚪 Exit",
                            command=self.root.quit,
                            font=('Arial', 10),
                            bg='#34495e', fg='white',
                            width=15, height=1)
        exit_btn.pack(pady=20)
    
    def darken_color(self, color):
        # Simple color darkening for hover effect
        color_map = {
            '#e74c3c': '#c0392b',
            '#3498db': '#2980b9',
            '#2ecc71': '#27ae60',
            '#f39c12': '#e67e22',
            '#9b59b6': '#8e44ad'
        }
        return color_map.get(color, color)
    
    def start_number_game(self):
        NumberGuessingGUI(self.root, self.create_main_menu)
    
    def start_tictactoe(self):
        TicTacToeGUI(self.root, self.create_main_menu)
    
    def start_rps(self):
        RockPaperScissorsGUI(self.root, self.create_main_menu)
    
    def start_word_game(self):
        WordGuessingGUI(self.root, self.create_main_menu)
    
    def start_memory_game(self):
        MemoryGameGUI(self.root, self.create_main_menu)

class NumberGuessingGUI:
    def __init__(self, root, return_callback):
        self.root = root
        self.return_callback = return_callback
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 7
        
        self.setup_gui()
    
    def setup_gui(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.geometry("500x600")
        self.root.configure(bg='#e74c3c')
        
        main_frame = tk.Frame(self.root, bg='#e74c3c', padx=30, pady=30)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title = tk.Label(main_frame, text="🎯 Number Guessing Game",
                        font=('Arial', 18, 'bold'),
                        fg='white', bg='#e74c3c')
        title.pack(pady=20)
        
        # Instructions
        instructions = tk.Label(main_frame, 
                               text=f"I'm thinking of a number between 1 and 100!\nYou have {self.max_attempts} attempts to guess it.",
                               font=('Arial', 12),
                               fg='white', bg='#e74c3c',
                               justify=tk.CENTER)
        instructions.pack(pady=10)
        
        # Attempts counter
        self.attempts_label = tk.Label(main_frame, text=f"Attempts: {self.attempts}/{self.max_attempts}",
                                      font=('Arial', 14, 'bold'),
                                      fg='white', bg='#e74c3c')
        self.attempts_label.pack(pady=10)
        
        # Entry frame
        entry_frame = tk.Frame(main_frame, bg='#e74c3c')
        entry_frame.pack(pady=20)
        
        tk.Label(entry_frame, text="Your guess:",
                font=('Arial', 12),
                fg='white', bg='#e74c3c').pack()
        
        self.guess_entry = tk.Entry(entry_frame, font=('Arial', 16),
                                   width=10, justify='center')
        self.guess_entry.pack(pady=10)
        self.guess_entry.bind('<Return>', lambda e: self.make_guess())
        
        # Guess button
        guess_btn = tk.Button(entry_frame, text="Guess!",
                             command=self.make_guess,
                             font=('Arial', 14, 'bold'),
                             bg='white', fg='#e74c3c',
                             width=15, height=2)
        guess_btn.pack(pady=10)
        
        # Result label
        self.result_label = tk.Label(main_frame, text="",
                                    font=('Arial', 14, 'bold'),
                                    fg='white', bg='#e74c3c',
                                    height=3)
        self.result_label.pack(pady=20)
        
        # Control buttons
        btn_frame = tk.Frame(main_frame, bg='#e74c3c')
        btn_frame.pack(pady=20)
        
        new_game_btn = tk.Button(btn_frame, text="New Game",
                                command=self.new_game,
                                font=('Arial', 10),
                                bg='#f39c12', fg='white')
        new_game_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn = tk.Button(btn_frame, text="Back to Menu",
                            command=self.return_callback,
                            font=('Arial', 10),
                            bg='#34495e', fg='white')
        back_btn.pack(side=tk.LEFT, padx=10)
        
        self.guess_entry.focus()
    
    def make_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1
            self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
            
            if guess == self.secret_number:
                self.result_label.config(text=f"🎉 Congratulations!\nYou guessed it in {self.attempts} attempts!",
                                       fg='#2ecc71')
                self.guess_entry.config(state='disabled')
                return
            
            elif guess < self.secret_number:
                hint = "📈 Too low! Try higher."
            else:
                hint = "📉 Too high! Try lower."
            
            remaining = self.max_attempts - self.attempts
            if remaining > 0:
                self.result_label.config(text=f"{hint}\n{remaining} attempts left")
            else:
                self.result_label.config(text=f"😔 Game Over!\nThe number was {self.secret_number}")
                self.guess_entry.config(state='disabled')
            
            self.guess_entry.delete(0, tk.END)
            
        except ValueError:
            self.result_label.config(text="Please enter a valid number!", fg='#f1c40f')
    
    def new_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
        self.result_label.config(text="", fg='white')
        self.guess_entry.config(state='normal')
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

class TicTacToeGUI:
    def __init__(self, root, return_callback):
        self.root = root
        self.return_callback = return_callback
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.buttons = []
        self.game_over = False
        
        self.setup_gui()
    
    def setup_gui(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.geometry("400x500")
        self.root.configure(bg='#3498db')
        
        main_frame = tk.Frame(self.root, bg='#3498db', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title = tk.Label(main_frame, text="⭕ Tic-Tac-Toe",
                        font=('Arial', 18, 'bold'),
                        fg='white', bg='#3498db')
        title.pack(pady=20)
        
        # Player indicator
        self.player_label = tk.Label(main_frame, text=f"Player {self.current_player}'s turn",
                                    font=('Arial', 14, 'bold'),
                                    fg='white', bg='#3498db')
        self.player_label.pack(pady=10)
        
        # Game board
        board_frame = tk.Frame(main_frame, bg='#3498db')
        board_frame.pack(pady=20)
        
        self.buttons = []
        for i in range(9):
            row, col = divmod(i, 3)
            btn = tk.Button(board_frame, text=' ',
                           font=('Arial', 20, 'bold'),
                           width=4, height=2,
                           bg='white', fg='#2c3e50',
                           command=lambda idx=i: self.make_move(idx))
            btn.grid(row=row, column=col, padx=2, pady=2)
            self.buttons.append(btn)
        
        # Control buttons
        btn_frame = tk.Frame(main_frame, bg='#3498db')
        btn_frame.pack(pady=20)
        
        new_game_btn = tk.Button(btn_frame, text="New Game",
                                command=self.new_game,
                                font=('Arial', 10),
                                bg='#f39c12', fg='white')
        new_game_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn = tk.Button(btn_frame, text="Back to Menu",
                            command=self.return_callback,
                            font=('Arial', 10),
                            bg='#34495e', fg='white')
        back_btn.pack(side=tk.LEFT, padx=10)
    
    def make_move(self, position):
        if self.board[position] == ' ' and not self.game_over:
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player,
                                        fg='#e74c3c' if self.current_player == 'X' else '#2ecc71')
            
            winner = self.check_winner()
            if winner:
                if winner == 'Tie':
                    self.player_label.config(text="🤝 It's a tie!")
                else:
                    self.player_label.config(text=f"🎉 Player {winner} wins!")
                self.game_over = True
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.player_label.config(text=f"Player {self.current_player}'s turn")
    
    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' '):
                return self.board[combo[0]]
        
        if ' ' not in self.board:
            return 'Tie'
        
        return None
    
    def new_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.game_over = False
        self.player_label.config(text=f"Player {self.current_player}'s turn")
        
        for btn in self.buttons:
            btn.config(text=' ', fg='#2c3e50')

class RockPaperScissorsGUI:
    def __init__(self, root, return_callback):
        self.root = root
        self.return_callback = return_callback
        self.player_score = 0
        self.computer_score = 0
        self.choices = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}
        
        self.setup_gui()
    
    def setup_gui(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.geometry("500x600")
        self.root.configure(bg='#2ecc71')
        
        main_frame = tk.Frame(self.root, bg='#2ecc71', padx=30, pady=30)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title = tk.Label(main_frame, text="🪨📄✂️ Rock-Paper-Scissors",
                        font=('Arial', 16, 'bold'),
                        fg='white', bg='#2ecc71')
        title.pack(pady=20)
        
        # Score
        self.score_label = tk.Label(main_frame, text=f"You: {self.player_score}  |  Computer: {self.computer_score}",
                                   font=('Arial', 14, 'bold'),
                                   fg='white', bg='#2ecc71')
        self.score_label.pack(pady=10)
        
        # Choices display
        display_frame = tk.Frame(main_frame, bg='#2ecc71')
        display_frame.pack(pady=20)
        
        tk.Label(display_frame, text="You", font=('Arial', 12, 'bold'),
                fg='white', bg='#2ecc71').grid(row=0, column=0, padx=20)
        tk.Label(display_frame, text="Computer", font=('Arial', 12, 'bold'),
                fg='white', bg='#2ecc71').grid(row=0, column=2, padx=20)
        
        self.player_choice_label = tk.Label(display_frame, text="?",
                                          font=('Arial', 40),
                                          bg='white', width=3, height=2)
        self.player_choice_label.grid(row=1, column=0, padx=20, pady=10)
        
        tk.Label(display_frame, text="VS", font=('Arial', 16, 'bold'),
                fg='white', bg='#2ecc71').grid(row=1, column=1, padx=10)
        
        self.computer_choice_label = tk.Label(display_frame, text="?",
                                            font=('Arial', 40),
                                            bg='white', width=3, height=2)
        self.computer_choice_label.grid(row=1, column=2, padx=20, pady=10)
        
        # Result label
        self.result_label = tk.Label(main_frame, text="Choose your move!",
                                   font=('Arial', 14, 'bold'),
                                   fg='white', bg='#2ecc71',
                                   height=2)
        self.result_label.pack(pady=20)
        
        # Choice buttons
        choices_frame = tk.Frame(main_frame, bg='#2ecc71')
        choices_frame.pack(pady=20)
        
        for choice, emoji in self.choices.items():
            btn = tk.Button(choices_frame, text=f"{emoji}\n{choice.title()}",
                           font=('Arial', 12, 'bold'),
                           bg='white', fg='#2c3e50',
                           width=10, height=3,
                           command=lambda c=choice: self.play_round(c))
            btn.pack(side=tk.LEFT, padx=10)
        
        # Control buttons
        btn_frame = tk.Frame(main_frame, bg='#2ecc71')
        btn_frame.pack(pady=30)
        
        reset_btn = tk.Button(btn_frame, text="Reset Score",
                             command=self.reset_score,
                             font=('Arial', 10),
                             bg='#f39c12', fg='white')
        reset_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn = tk.Button(btn_frame, text="Back to Menu",
                            command=self.return_callback,
                            font=('Arial', 10),
                            bg='#34495e', fg='white')
        back_btn.pack(side=tk.LEFT, padx=10)
    
    def play_round(self, player_choice):
        computer_choice = random.choice(list(self.choices.keys()))
        
        # Update display
        self.player_choice_label.config(text=self.choices[player_choice])
        self.computer_choice_label.config(text=self.choices[computer_choice])
        
        # Determine winner
        winner = self.get_winner(player_choice, computer_choice)
        
        if winner == 'tie':
            self.result_label.config(text="🤝 It's a tie!")
        elif winner == 'player':
            self.result_label.config(text="🎉 You win this round!")
            self.player_score += 1
        else:
            self.result_label.config(text="🤖 Computer wins this round!")
            self.computer_score += 1
        
        self.score_label.config(text=f"You: {self.player_score}  |  Computer: {self.computer_score}")
        
        # Check for game winner
        if self.player_score >= 5:
            self.result_label.config(text="🏆 YOU WIN THE GAME!")
        elif self.computer_score >= 5:
            self.result_label.config(text="🤖 COMPUTER WINS THE GAME!")
    
    def get_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return 'tie'
        elif (player_choice == 'rock' and computer_choice == 'scissors' or
              player_choice == 'paper' and computer_choice == 'rock' or
              player_choice == 'scissors' and computer_choice == 'paper'):
            return 'player'
        else:
            return 'computer'
    
    def reset_score(self):
        self.player_score = 0
        self.computer_score = 0
        self.score_label.config(text=f"You: {self.player_score}  |  Computer: {self.computer_score}")
        self.result_label.config(text="Choose your move!")
        self.player_choice_label.config(text="?")
        self.computer_choice_label.config(text="?")

class WordGuessingGUI:
    def __init__(self, root, return_callback):
        self.root = root
        self.return_callback = return_callback
        self.words = [
            'PYTHON', 'COMPUTER', 'PROGRAMMING', 'KEYBOARD', 'MONITOR',
            'SOFTWARE', 'HARDWARE', 'INTERNET', 'WEBSITE', 'CODING'
        ]
        self.word = random.choice(self.words)
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_wrong_guesses = 6
        
        self.setup_gui()
    
    def setup_gui(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.geometry("600x700")
        self.root.configure(bg='#f39c12')
        
        main_frame = tk.Frame(self.root, bg='#f39c12', padx=30, pady=30)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title = tk.Label(main_frame, text="🔤 Word Guessing Game",
                        font=('Arial', 18, 'bold'),
                        fg='white', bg='#f39c12')
        title.pack(pady=20)
        
        # Hangman display
        self.hangman_label = tk.Label(main_frame, text=self.get_hangman_display(),
                                     font=('Courier', 10),
                                     fg='white', bg='#f39c12',
                                     justify=tk.LEFT)
        self.hangman_label.pack(pady=10)
        
        # Word display
        self.word_label = tk.Label(main_frame, text=self.get_word_display(),
                                  font=('Arial', 24, 'bold'),
                                  fg='white', bg='#f39c12',
                                  height=2)
        self.word_label.pack(pady=20)
        
        # Wrong guesses counter
        self.wrong_label = tk.Label(main_frame, text=f"Wrong guesses: {self.wrong_guesses}/{self.max_wrong_guesses}",
                                   font=('Arial', 12, 'bold'),
                                   fg='white', bg='#f39c12')
        self.wrong_label.pack(pady=10)
        
        # Guessed letters
        self.guessed_label = tk.Label(main_frame, text="Guessed: ",
                                     font=('Arial', 12),
                                     fg='white', bg='#f39c12')
        self.guessed_label.pack(pady=5)
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg='#f39c12')
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="Guess a letter:",
                font=('Arial', 12),
                fg='white', bg='#f39c12').pack()
        
        self.letter_entry = tk.Entry(input_frame, font=('Arial', 16),
                                    width=5, justify='center')
        self.letter_entry.pack(pady=10)
        self.letter_entry.bind('<Return>', lambda e: self.guess_letter())
        
        guess_btn = tk.Button(input_frame, text="Guess!",
                             command=self.guess_letter,
                             font=('Arial', 12, 'bold'),
                             bg='white', fg='#f39c12',
                             width=10)
        guess_btn.pack(pady=10)
        
        # Result label
        self.result_label = tk.Label(main_frame, text="",
                                    font=('Arial', 14, 'bold'),
                                    fg='white', bg='#f39c12',
                                    height=2)
        self.result_label.pack(pady=20)
        
        # Control buttons
        btn_frame = tk.Frame(main_frame, bg='#f39c12')
        btn_frame.pack(pady=20)
        
        new_game_btn = tk.Button(btn_frame, text="New Word",
                                command=self.new_game,
                                font=('Arial', 10),
                                bg='#e74c3c', fg='white')
        new_game_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn = tk.Button(btn_frame, text="Back to Menu",
                            command=self.return_callback,
                            font=('Arial', 10),
                            bg='#34495e', fg='white')
        back_btn.pack(side=tk.LEFT, padx=10)
        
        self.letter_entry.focus()
    
    def get_word_display(self):
        display = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + ' '
            else:
                display += '_ '
        return display.strip()
    
    def get_hangman_display(self):
        stages = [
            "  +---+\n      |\n      |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
        ]
        return stages[self.wrong_guesses]
    
    def guess_letter(self):
        guess = self.letter_entry.get().upper().strip()
        
        if len(guess) != 1 or not guess.isalpha():
            self.result_label.config(text="Please enter a single letter!")
            self.letter_entry.delete(0, tk.END)
            return
        
        if guess in self.guessed_letters:
            self.result_label.config(text="You already guessed that letter!")
            self.letter_entry.delete(0, tk.END)
            return
        
        self.guessed_letters.add(guess)
        self.letter_entry.delete(0, tk.END)
        
        if guess in self.word:
            self.result_label.config(text=f"Good guess! '{guess}' is in the word.")
            # Check if word is complete
            if all(letter in self.guessed_letters for letter in self.word):
                self.result_label.config(text="🎉 Congratulations! You won!")
                self.letter_entry.config(state='disabled')
        else:
            self.wrong_guesses += 1
            self.result_label.config(text=f"Sorry, '{guess}' is not in the word.")
            
            if self.wrong_guesses >= self.max_wrong_guesses:
                self.result_label.config(text=f"😔 Game Over! The word was: {self.word}")
                self.letter_entry.config(state='disabled')
        
        # Update displays
        self.word_label.config(text=self.get_word_display())
        self.hangman_label.config(text=self.get_hangman_display())
        self.wrong_label.config(text=f"Wrong guesses: {self.wrong_guesses}/{self.max_wrong_guesses}")
        self.guessed_label.config(text=f"Guessed: {', '.join(sorted(self.guessed_letters))}")
    
    def new_game(self):
        self.word = random.choice(self.words)
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.result_label.config(text="")
        self.letter_entry.config(state='normal')
        
        # Update displays
        self.word_label.config(text=self.get_word_display())
        self.hangman_label.config(text=self.get_hangman_display())
        self.wrong_label.config(text=f"Wrong guesses: {self.wrong_guesses}/{self.max_wrong_guesses}")
        self.guessed_label.config(text="Guessed: ")
        self.letter_entry.focus()

class MemoryGameGUI:
    def __init__(self, root, return_callback):
        self.root = root
        self.return_callback = return_callback
        self.cards = []
        self.buttons = []
        self.flipped = []
        self.matched = []
        self.attempts = 0
        self.setup_game()
        
        self.setup_gui()
    
    def setup_game(self):
        # Create pairs of cards
        symbols = ['🎈', '🎨', '🎸', '🎭', '🎯', '🎪', '🎨', '🎲']
        self.cards = symbols + symbols
        random.shuffle(self.cards)
    
    def setup_gui(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.geometry("500x600")
        self.root.configure(bg='#9b59b6')
        
        main_frame = tk.Frame(self.root, bg='#9b59b6', padx=30, pady=30)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title = tk.Label(main_frame, text="🎲 Memory Game",
                        font=('Arial', 18, 'bold'),
                        fg='white', bg='#9b59b6')
        title.pack(pady=20)
        
        # Attempts counter
        self.attempts_label = tk.Label(main_frame, text=f"Attempts: {self.attempts}",
                                      font=('Arial', 14, 'bold'),
                                      fg='white', bg='#9b59b6')
        self.attempts_label.pack(pady=10)
        
        # Game board
        board_frame = tk.Frame(main_frame, bg='#9b59b6')
        board_frame.pack(pady=20)
        
        self.buttons = []
        for i in range(16):
            row, col = divmod(i, 4)
            btn = tk.Button(board_frame, text='?',
                           font=('Arial', 20),
                           width=3, height=2,
                           bg='white', fg='#2c3e50',
                           command=lambda idx=i: self.flip_card(idx))
            btn.grid(row=row, column=col, padx=2, pady=2)
            self.buttons.append(btn)
        
        # Result label
        self.result_label = tk.Label(main_frame, text="Find all the matching pairs!",
                                   font=('Arial', 12, 'bold'),
                                   fg='white', bg='#9b59b6',
                                   height=2)
        self.result_label.pack(pady=20)
        
        # Control buttons
        btn_frame = tk.Frame(main_frame, bg='#9b59b6')
        btn_frame.pack(pady=20)
        
        new_game_btn = tk.Button(btn_frame, text="New Game",
                                command=self.new_game,
                                font=('Arial', 10),
                                bg='#e74c3c', fg='white')
        new_game_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn = tk.Button(btn_frame, text="Back to Menu",
                            command=self.return_callback,
                            font=('Arial', 10),
                            bg='#34495e', fg='white')
        back_btn.pack(side=tk.LEFT, padx=10)
    
    def flip_card(self, index):
        if len(self.flipped) < 2 and index not in self.flipped and index not in self.matched:
            self.buttons[index].config(text=self.cards[index])
            self.flipped.append(index)
            
            if len(self.flipped) == 2:
                self.attempts += 1
                self.attempts_label.config(text=f"Attempts: {self.attempts}")
                self.root.after(1000, self.check_match)
    
    def check_match(self):
        if len(self.flipped) == 2:
            idx1, idx2 = self.flipped
            
            if self.cards[idx1] == self.cards[idx2]:
                # Match found
                self.matched.extend([idx1, idx2])
                self.buttons[idx1].config(bg='#2ecc71')
                self.buttons[idx2].config(bg='#2ecc71')
                self.result_label.config(text="Great! You found a match! 🎉")
                
                # Check if game is complete
                if len(self.matched) == 16:
                    self.result_label.config(text=f"🏆 Congratulations! You won in {self.attempts} attempts!")
            else:
                # No match, flip back
                self.buttons[idx1].config(text='?')
                self.buttons[idx2].config(text='?')
                self.result_label.config(text="No match. Try again!")
            
            self.flipped = []
    
    def new_game(self):
        self.setup_game()
        self.flipped = []
        self.matched = []
        self.attempts = 0
        self.attempts_label.config(text=f"Attempts: {self.attempts}")
        self.result_label.config(text="Find all the matching pairs!")
        
        for btn in self.buttons:
            btn.config(text='?', bg='white')

def main():
    root = tk.Tk()
    app = GameCollection(root)
    root.mainloop()

if __name__ == "__main__":
    main()