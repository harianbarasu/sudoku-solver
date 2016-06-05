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

		# A really crude way to add the letter headings. 
		# Come up with a better way.

		print "%3s" %" ",
		print "%3s" %"A",
		print "%3s" %"B",
		print "%3s" %"C",
		print "%3s" %" ",
		print "%3s" %"D",
		print "%3s" %"E",
		print "%3s" %"F",
		print "%3s" %" ",
		print "%3s" %"G",
		print "%3s" %"H",
		print "%3s" %"I"

		print "TEST"

		# A variable to be used to print the row boxes.
		# Try to think of a better way.
		row_counter = 0

		# Loop to iterate over the rows
		for i in range(9):

			# Loop to iterate over the columns
			for j in range(9):

				# Prior to printing the first column print the row number
				if j == 0:
					print "%3s" %row_counter,
					row_counter += 1

				# If the next row is going to have dashes and pluses
				# use the standard print function for better display
				if(i + 1) % 3 == 0 and i != 8 and j == 8:
					print "%3s" %self.board[i][j]
				else:
					print "%3s" %self.board[i][j],

				# Every 3 columns, add a divider to show gap between squares
				if (j + 1) % 3 == 0 and j != 8:
					print "%3s" %"|",

			# Every 3 rows, print a row of dashes and pluses to show gap
			if (i + 1) % 3 == 0 and i != 8:
				print " " * 3,
				for k in range(2):
					print "-" * 13, "+",
				print "-" * 13
			else:
				print "\n"

def main():

if __name__ == "__main__":
    main()