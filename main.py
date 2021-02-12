import curses
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
        self.lineno = 0
        self.duration = 20
        self.strings = 4
        self.num_lines_visible = 10
        self.lives = 3

        self.board = self.generate_empty_board()

    def generate_empty_board(self):
        # generates upcoming notes, as 2D list
        blank_lines = [[False]*self.strings for _ in range(self.num_lines_visible)] 
        #board = [self.generate_notes() for _ in range(self.duration)]
        
        return blank_lines #+ board
    
    def update_board(self):
        del self.board[0]
        self.board.append(self.generate_notes())
    

    def generate_notes(self):
        # generates a single row of board
        options = (0,)*3 + (1,)*1 + (2,)*1
        note_count = choice(options) 
        blank_count = self.strings - note_count 
                
        notes = [False]*blank_count + [True]*note_count

        shuffle(notes)
        return notes
                
                
    def get_keys(self):
        # user input
        ...

    def format_line(self, line):
        formatted = []
        for note in line:
            symbol = "X" if note else " "
            formatted.append(symbol)

        return " ".join(formatted)

        


    def format_board(self):
        # formats just incoming notes (as string)
        #TODO print only next n lines, pad with empty lines if neccessary
        visible_lines = self.board[self.lineno:self.lineno + self.num_lines_visible]
        return "\n".join(map(self.format_line, visible_lines[::-1]))
        
    
    def format(self):
        # formats game state as string
        formatted_keys = " ".join("ASDF") 
        formatted_hyps = "-" * 7
        formatted_board = self.format_board()

        result = f"{formatted_board}\n{formatted_hyps}\n{formatted_keys}"

        return result

    def display_score(self):
        # formats a screen that displays score
        ...

    def play(self):
        # play the game
        for _ in range(6):
            print(self.format())
            self.update_board()




def main():
    
    #stdscr.clear()
    
    curr_game = Game(Difficulty.easy)
    curr_game.play()
    #pprint(curr_game.board) 
    print(curr_game.format())
    




    input()


#curses.wrapper(main)
main() 



