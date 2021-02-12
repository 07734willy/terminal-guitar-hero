import curses
import time
from random import shuffle, choice
from pprint import pprint


class Difficulty:
    easy = 1
    medium = 2
    hard = 3

class Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty

        self.points = 0
        self.duration = 20
        self.columns = 4
        self.num_lines_visible = 10
        self.lives = 3
        

        self.board = self.generate_empty_board()
        self.clear_keys()

    def generate_empty_board(self):
        # generates upcoming notes, as 2D list
        blank_lines = [[False] * self.columns for _ in range(self.num_lines_visible)] 

        return blank_lines
    
    def update_board(self):
        del self.board[0]
        self.board.append(self.generate_notes())
   
    @property
    def current_line(self):
        return self.board[0]
    

    def generate_notes(self):
        # generates a single row of board
        options = (0,)*3 + (1,)*1 + (2,)*1
        note_count = choice(options) 
        blank_count = self.columns - note_count 
                
        notes = [False]*blank_count + [True]*note_count

        shuffle(notes)
        return notes
                
                
    def get_keys(self):
        # user input
        ch = input()
        try:
            key_index = ["asdf".index(ch.lower())]
            if not self.current_line[key_index]:
                self.lives -= 1
            self.keys[key_index] = True
        except:
            pass
        
    def clear_keys(self):
        self.keys = [False]*self.columns

    def check_keys(self):
        return self.keys == self.current_line

    def format_line(self, line):
        formatted = []
        for note in line:
            symbol = "X" if note else " "
            formatted.append(symbol)

        return " ".join(formatted)

        


    def format_board(self):
        # formats just incoming notes (as string)
        #TODO print only next n lines, pad with empty lines if neccessary
        return "\n".join(map(self.format_line, self.board[::-1]))
        
    
    def format(self):
        # formats game state as string
        formatted_keys = " ".join("ASDF") 
        formatted_hyps = "-" * 7
        formatted_board = self.format_board()
        formatted_score = self.format_score()
        formatted_lives = self.format_lives()

        result = f"{formatted_score}\n\n{formatted_board}\n{formatted_hyps}\n{formatted_keys}\n\n{formatted_lives}"

        return result

    def format_score(self):
        # formats a screen that displays score
        return f"SCORE: {self.points}"
    
    def format_lives(self):
        return f"LIVES: {self.lives}"
        

    def play(self):
        # play the game
        while self.lives:
            print(self.format())
            time.sleep(1)
            if not self.check_keys():
                self.lives -= 1
            self.clear_keys()
            self.update_board()
            self.points += 1





def main():
    
    #stdscr.clear()
    
    curr_game = Game(Difficulty.easy)
    curr_game.play()
    #pprint(curr_game.board) 
    print(curr_game.format())
    




    input()


#curses.wrapper(main)
main() 



