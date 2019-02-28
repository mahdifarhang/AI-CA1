import numpy.genfromtxt

n_queens = 8



data = [[0 for x in range(n_queens)] for y in range(n_queens)]

def __print_grid__(data):
	for i in range(n_queens):
		for j in range(n_queens):
			if board[i][j] = 0:
				print('O', end = '')
			else:
				print('X', end = '')
		print()

