# Hari Anbarasu
# This program is intended to be a sudoku solver.
# It will takes as input, a sudoku board with some of the boxes filled in.
# It will output the solved sudoku board.

from copy import deepcopy

# Define global variable for EMPTY
EMPTY = "."

# Hash table to map column headers to array indices
column_hash = {
	"A": 0, "a": 0, "B": 1, "b": 1, "C": 2, "c": 2, "D": 3, "d": 3,
	"E": 4, "e": 4, "F": 5, "f": 5, "G": 6, "g": 6, "H": 7, "h": 7,
	"I": 8, "i": 8}

unsolved_locations = []

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

	for row_num in range(9):
		row = raw_input("Please enter the numbers found in row %d, in order, separated by commas. If there is no number, enter 0: " % (row_num))
		row_list = [x.strip() for x in row.split(',')]
		for col_num in range(9):
			if(int(row_list[col_num]) < 0 or int(row_list[col_num]) > 9):
				print "Not a valid number to be entered. Quitting."
				return
			if int(row_list[col_num]) == 0:
				board.board[row_num][col_num] = EMPTY
			else:
				board.board[row_num][col_num] = int(row_list[col_num])
		print "Here is the current board:"
		board.print_board()
	find_unsolved_locations(board)
	solve_board(board)
	print "This is the final board:"
	board.print_board()

def check_row(board, row_num, value):
	for i in range(9):
		if board.board[row_num][i] == value:
			return False
	return True

def check_col(board, col_num, value):
	for i in range(9):
		if board.board[i][col_num] == value:
			return False
	return True

def check_box(board, row_num, col_num, value):
	row_quotient = row_num / 3
	col_quotient = col_num / 3
	for i in range(row_quotient * 3, (row_quotient + 1) * 3):
		for j in range(col_quotient * 3, (col_quotient + 1) * 3):
			if board.board[i][j] == value:
				return False
	return True	

def find_unsolved_locations(board):
	for i in range(9):
		for j in range(9):
			if board.board[i][j] == EMPTY:
				unsolved_locations.append((i, j))

def valid_move(board, row_num, col_num, value):
	if check_row(board, row_num, value) and check_col(board, col_num, value) \
	and check_box(board, row_num, col_num, value):
		return True
	return False

def solve_board(board):
	if not unsolved_locations:
		return True
	for i in range(1, 10):
		row, col = unsolved_locations.pop()
		if valid_move(board, row, col, i):
			board.board[row][col] = i
			result = solve_board(board)
			if not result:
				board.board[row][col] = EMPTY
				unsolved_locations.append((row, col))
			else:
				return True
		else:
			unsolved_locations.append((row, col))
	return False

def main():
	new_board = Board()
	print "Welcome to Sudoku Solver!"
	print "This is the current board:"
	new_board.print_board()
	choice = raw_input("Your options are: FILL, SOLVE, or QUIT. ")
	if choice == "FILL" or choice == "fill" or choice == "F" or choice == "f":
		fill_numbers(new_board)
	elif choice == "SOLVE" or choice == "solve" or choice == "S" or choice == "s":
		find_unsolved_locations(new_board)
		solve_board(new_board)
		print "This is the final board:"
		new_board.print_board()
	elif choice == "QUIT" or choice == "quit" or choice == "Q" or choice == "q":
		return
	else:
		print "You have chosen a wrong command. Exiting."
		return




if __name__ == "__main__":
    main()
