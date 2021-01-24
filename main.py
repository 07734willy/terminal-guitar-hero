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

		self.board = self.generate_board()

	def generate_board(self):
		# generates upcoming notes, as 2D list

		board = [self.generate_notes() for _ in range(self.duration)]
		return board
	
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

	def format_board(self):
		# formats just incoming notes (as string)
		...

	def format(self):
		# formats game state as string
		...

	def display_score(self):
		# formats a screen that displays score
		...

	def play(self):
		# play the game
		...

def main():
	
	#stdscr.clear()
	
	curr_game = Game(Difficulty.easy)
	curr_game.play()
	pprint(curr_game.board) 
	




	input()


#curses.wrapper(main)
main() 
