# Hari Anbarasu
# This program is intended to be a sudoku solver.
# It will takes as input, a sudoku board with some of the boxes filled in.
# It will output the solved sudoku board.

from copy import deepcopy

# Define global variable for EMPTY
EMPTY = "."

# Hash table to map column headers to array indices
column_hash = {"A": 0, "a": 0, "B": 1, "b": 1, "C": 2, "c": 2, "D": 3, "d": 3,
				 "E": 4, "e": 4, "F": 5, "f": 5, "G": 6, "g": 6, "H": 7, "h": 7, "I": 8, "i": 8}

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

# Function to fill in numbers into a Board object. 
def fill_numbers(board):

	# Inform the user what is happening
	print "You are now filling in numbers. The program will continue to prompt you until you input 'DONE'."

	# Run an infinite loop and break within loop once condition is met
	while True:

		# Get the cell into which a number should be inputted
		cell = raw_input("Enter the cell to input the number into. Enter DONE if you are done filling in numbers: ")

		# If they type DONE, stop taking in numbers.
		if cell == "DONE" or cell == "done" or cell == "D" or cell == "d":
			return

		# A basic sanity check.
		while cell[0] not in column_hash or int(cell[1]) < 0 or int(cell[1]) > 8:
			print "Not a valid cell."
			cell = raw_input("Enter the cell to input the number into. Enter DONE if you are done filling in numbers: ")

		# Get the number that is going in the cell
		number = int(raw_input('Enter the number to be inputted into cell %s: ' %cell))

		# Some basic sanity checks
		while(number < 1 or number > 9):
			print "Not a valid number for a sudoku board."
			number = int(raw_input('Enter the number to be inputted into cell %s: ' %cell))

		# Column is the letter indexed one
		column = column_hash[cell[0]]

		# Row is the number indexed one
		row = int(cell[1])

		# Insert into the board
		board.board[row][column] = number

		# Print the board for verification
		print "Here is the current board:"
		board.print_board()

		# Have an undo button?

def check_row(board, row_num, value):
	for i in range(9):
		if board.board[row_num][i] == value:
			return false
	return true

def check_col(board, col_num, value):
	for i in range(9):
		if board.board[i][col_num] == value:
			return false
	return true

def check_box(board, row_num, col_num, value):
	row_quotient = row_num / 3
	col_quotient = col_num / 3
	for i in range(row_quotient * 3, (row_quotient + 1) * 3):
		for j in range(col_quotient * 3, (col_quotient + 1) * 3):
			if board.board[i][j] == value:
				return false
	return true	

def solve_board(board):
	pass

	


def main():
	new_board = Board()
	print "Welcome to Sudoku Solver!"
	print "This is the current board:"
	new_board.print_board()
	choice = raw_input("Your options are: FILL, SOLVE, or QUIT. ")
	if choice == "FILL" or choice == "fill" or choice == "F" or choice == "f":
		fill_numbers(new_board)
	elif choice == "SOLVE" or choice == "solve" or choice == "S" or choice == "s":
		pass
	elif choice == "QUIT" or choice == "quit" or choice == "Q" or choice == "q":
		return
	else:
		print "You have chosen a wrong command. Exiting."
		return




if __name__ == "__main__":
    main()
