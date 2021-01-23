import curses


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

		self.board = self.generate_board()

	def generate_board(self):
		# generates upcoming notes, as 2D list
		...
	
	def generate_notes(self):
		# generates a single row of board
		...

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

def main(stdscr):
	stdscr.clear()
	
	curr_game = Game(Difficulty.easy)
	curr_game.play()


	input()


curses.wrapper(main)

