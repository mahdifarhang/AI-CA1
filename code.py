import numpy.genfromtxt

n_queens = 8
input_file_name = 'in1.csv'
data = genfromtxt(input_file_name, delimiter=',')


print(data)

# def __print_grid__(data):
# 	for i in range(n_queens):
# 		for j in range(n_queens):
# 			if board[i][j] = 0:
# 				print('O', end = '')
# 			else:
# 				print('X', end = '')
# 		print()