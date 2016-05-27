# Hari Anbarasu
# This program is intended to be a sudoku solver.
# It will takes as input, a sudoku board with some of the boxes filled in.
# It will output the solved sudoku board.

# The Board class which will be used for the game board.
class Board(object):

	# Initialized to be a blank 9x9 board.
	def __init__(self):
		self.board = [['.' for x in range(9)] for y in range(9)]

	# Class function to print the current Board
	def print_board(self):
		for i in range(9):
			for j in range(9):
				if(i + 1) % 3 == 0 and i != 8 and j == 8:
					print "%3s" %self.board[i][j]
				else:
					print "%3s" %self.board[i][j],

				if (j + 1) % 3 == 0 and j != 8:
					print "%3s" %"|",

			if (i + 1) % 3 == 0 and i != 8:
				for k in range(2):
					print "-" * 13, "+",
				print "-" * 13
			else:
				print "\n"

board = Board()
board.print_board()