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
				print "%3s" %self.board[i][j]
			print "\n"