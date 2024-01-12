import random
a='''Abuse
Adult
Agent
Anger
Apple
Award
Basis
Beach
Birth
Block
Blood
Board
Brain
Bread
Break
Brown
Buyer
Cause
Chain
Chair
Chest
Chief
Child
China
Claim
Class
Clock
Coach
Coast
Court
Cover
Cream
Crime
Cross
Crowd
Crown
Cycle
Dance
Death
Depth
Doubt
Draft
Drama
Dream
Dress
Drink
Drive
Earth
Enemy
Entry
Error
Event
Faith
Fault
Field
Fight
Final
Floor
Focus
Force
Frame
Frank
Front
Fruit
Glass
Grant
Grass
Green
Group
Guide
Heart
Henry
Horse
Hotel
House
Image
Index
Input
Issue
Japan
Jones
Judge
Knife
Laura
Layer
Level
Lewis
Light
Limit
Lunch
Major
March
Match
Metal
Model
Money
Month
Motor
Mouth
Music
Night
Noise'''
words_list=a.splitlines()
class Hangman():
    def _init_(self,plist):
        self.word = ""
        self.hidden = ""
        self.incorrect = 0
        self.used = set()
        
    def get_word(self,word):
         f=random.randint(0,len(words_list))
         word=words_list[f]
         return word
    
    def start_game(self,plist):
        self.word = self.get_word(plist).lower()
        self.hidden = ["_"] * len(self.word)
        self.incorrect = 0
        self.used = set()
    
    def display_hidden_word(self):
        print(" ".join(self.hidden))
    
    def display_incorrect_guesses(self):
        print(f"Incorrect Guesses: {self.incorrect}")
    
    def display_used_letters(self):
        print("Used Letters: " + " ".join(self.used))
    
    def display_hangman(self):
        if self.incorrect == 0:
            print("""
             _____
            |     |
                 |
                 |
                 |
                 |
                 |
            _________
            """)
        elif self.incorrect == 1:
            print("""
             _____
            |     |
            O     |
                  |
                  |
                  |
                  |
            _________
            """)
        elif self.incorrect == 2:
            print("""
             _____
            |     |
            O     |
            |     |
                  |
                  |
                  |
            _________
            """)
        elif self.incorrect == 3:
            print("""
             _____
            |     |
            O     |
           /|     |
                  |
                  |
                  |
            _________
            """)
        elif self.incorrect == 4:
            print("""
             _____
            |     |
            O     |
           /|\    |
                  |
                  |
                  |
            _________
            """)
        elif self.incorrect == 5:
            print("""
             _____
            |     |
            O     |
           /|\    |
           / \    |
                  |
                  |
            _________
            """)

    
    def game(self,plist):
        self.start_game(plist)
        while self.incorrect < 6 and "_" in self.hidden:
            self.display_hidden_word()
            self.display_incorrect_guesses()
            self.display_used_letters()
            self.display_hangman()
            guess = input("Guess a letter: ").lower()
            if guess in self.used:
                print("You have already used that letter. Try another letter.")
                continue
            self.used.add(guess)
            if guess in self.word:
                for i in range(len(self.word)):
                    if self.word[i] == guess:
                        self.hidden[i] = guess
                print("Correct Guess!")
            else:
                self.incorrect += 1
                print("Incorrect Guess.")
        if "_" not in self.hidden:
            self.display_hidden_word()
            print("You won! The word was",self.word)
        if self.incorrect==6:
            print("You Lost! The word was",self.word)

class TicTacToe:
    def __init__(self):
        self.board = [" "," "," "," "," "," "," "," "," "]
        self.players = ["Player 1", "Player 2"]
        self.symbols = ["X", "O"]

    def print_board(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")

    def moves(self, player_name, symbol):
        while True:
            try:
                move = int(input(f"{player_name} ({symbol}), enter your move : "))
                if move in range(1, 10) and self.board[move - 1] == " ":
                    return move
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

    def update_board(self, symbol, move):
        self.board[move - 1] = symbol

    def is_winning_combination(self, symbol):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combination in winning_combinations:
            if all(self.board[i] == symbol for i in combination):
                return True
        return False

    def full(self):
         for space in self.board:
            if space == " ":
               return False
         return True


    def winner(self):
        if self.is_winning_combination("X"):
            return "Player 1"
        elif self.is_winning_combination("O"):
            return "Player 2"
        else:
            return None

    def play_game(self):
         print("Welcome to Tic Tac Toe!\n")
         self.print_board()
         current_player = 0
         while True:
               player_name = self.players[current_player]
               symbol = self.symbols[current_player]
               print(f"{player_name}({symbol}) turn")
               move = self.moves(player_name, symbol)
               self.update_board(symbol, move)
               self.print_board()
               winner = self.winner()
               if winner:
                  print(f"{winner} wins!")
                  break
               elif self.full():
                  print("Tie")
                  break
               if current_player == 0:
                  current_player = 1
               else:
                  current_player = 0


while True:
    
    print('Welcome To Game Arena !')
    print('')
    
    games=['Hangman','Tic-Tac-Toe','rock-paper scissors','Exit']
    z=0
    for i in games:
        print(z+1,'.',i)
        z=z+1
    n=int(input("Enter the game you would like to play: "))
    if n==1:
        game = Hangman()
        game.game(words_list)
    if n==2:
        game = TicTacToe()
        game.play_game()
    if n==3:
        print('Best of three Rounds, Best of luck !')
       
        count = 0
        c = 0
        for i in range(3):
            print('Round',i+1,'. Best of Luck !')
            lst=['Rock','Paper','Scissors']
            z=1
            for i in lst:
                print(z,i)
                z+=1
            x = (input('Enter your choice :'))
            y = random.randint(1, 3)
            y=int(y)
            x=int(x)
            if (int(x) == 1 and y == 1) or (int(x) == 2 and y == 2) or (int(x) == 3 and y == 3):
                print('Your choice:',lst[x-1])
                print("Computer's choice:",lst[y-1])
                print("Its a Tie in this round !!")
            elif int(x) == 1 and y == 2:
                print('Your choice:',lst[x-1])
                print("Computer's choice:",lst[y-1])
                print("Computer won this round !")
                c += 1
            elif int(x) == 1 and y == 3:
                count += 1
                print('Your choice:',lst[x-1])
                print("Computer's choice:",lst[y-1])
                print("You won this round !!")
            elif int(x) == 2 and y == 1:
                count += 1
                print('Your choice:',lst[x-1])
                print("Computer's choice:",lst[y-1])
                print("You won this round !!")
            elif int(x) == 2 and y == 3:
                print('Your choice:',lst[x-1])
                print("Computer's choice:",lst[y-1])
                print("Computer won this round !")
                
                c += 1
            elif int(x) == 3 and y == 1:
                print('Your choice:',lst[x-1])
                print("Computer's choice:",lst[y-1])
                print("Computer won this round !")
                
                c += 1
            elif int(x) == 3 and y == 2:
                count += 1
                print('Your choice:',lst[x-1])
                print("Computer's choice:",lst[y-1])
                print("You won this round !!")
            else:
                print('Your choice:',lst[x-1])
                print("Computer's choice:",lst[y-1])
                print("Incorrect input !")
        if count > c:
            print("YOU won the Best of 3 Match !!")
        elif count == c:
            print("Its a TIE between You and Computer !!")
        else:
            print("COMPUTER won the Best of 3 Match !")
    if n==4:
        break

    