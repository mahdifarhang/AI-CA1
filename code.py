from numpy import genfromtxt
from itertools import combinations as com
from time import time
n_queens = 8
input_file_name = 'test_b.csv'

def num_of_column_and_row_threats(my_data):
	column_threats = 0
	row_threats = 0
	for i in range(n_queens):
		num_of_queens_column = 0
		num_of_queens_row = 0
		for j in range(n_queens):
			if (my_data[j][1] == i + 1):
				num_of_queens_column += 1
			if (my_data[j][0] == i + 1):
				num_of_queens_row += 1
		if (num_of_queens_column > 1):
			column_threats += num_of_queens_column - 1
		if (num_of_queens_row > 1):
			row_threats += num_of_queens_row - 1
	return column_threats + row_threats

# we could count number of rows or columns without queens and the answer would have been the same

def num_of_diameter_threats(my_data):
	threats = 0
	blacklist = []
	for i in range(n_queens):
		for j in range(i + 1, n_queens):
			if (j in blacklist):
				continue
			if (abs(my_data[i][0] - my_data[j][0]) == abs(my_data[i][1] - my_data[j][1])):
				# print(i, j)
				threats += 1
				blacklist.append(j)
# if the abs wasn't there, we could get num of main diameter threats
# if the abs wasn't there and a minus was behind the right part of equation, we could get num of non_main diameter threats
	return threats

def num_of_threats(my_data):
	return num_of_diameter_threats(my_data) + num_of_column_and_row_threats(my_data)

def danger(my_data):
	dangers = 0
	for i in range(n_queens):
		for j in range(i + 1, n_queens):
			if(my_data[i][0] == my_data[j][0] or my_data[i][1] == my_data[j][1] or abs(my_data[i][0] - my_data[j][0]) == abs(my_data[i][1] - my_data[j][1])):
				dangers += 1
	return int(dangers / 2)




#	moves:
#	0	1	2
#	7		3
#	6	5	4 
num_of_moves = 8

def is_duplicate_element(my_data, element):
	num_of_existed = 0
	for i in range(n_queens):
		if (my_data[i][0] == element[0] and my_data[i][1] == element[1]):
			if (num_of_existed > 0):
				return True
			num_of_existed += 1
	return False

def move_if_possible(my_data, queen_no, move_no):
	temp = []
	temp.append(my_data[queen_no][0])
	temp.append(my_data[queen_no][1])
	if (move_no == 1):
		my_data[queen_no] = [my_data[queen_no][0] - 1, my_data[queen_no][1]]
		if (my_data[queen_no][0] < 1 or is_duplicate_element(my_data, my_data[queen_no])):
			my_data[queen_no][0] = temp[0]
			my_data[queen_no][1] = temp[1]
			return False
		return True
	elif (move_no == 3):
		my_data[queen_no] = [my_data[queen_no][0], my_data[queen_no][1] + 1]
		if (my_data[queen_no][1] > num_of_moves or is_duplicate_element(my_data, my_data[queen_no])):
			my_data[queen_no][0] = temp[0]
			my_data[queen_no][1] = temp[1]
			return False
		return True
	elif (move_no == 5):
		my_data[queen_no] = [my_data[queen_no][0] + 1, my_data[queen_no][1]]
		if (my_data[queen_no][0] > num_of_moves or is_duplicate_element(my_data, my_data[queen_no])):
			my_data[queen_no][0] = temp[0]
			my_data[queen_no][1] = temp[1]
			return False
		return True
	elif (move_no == 7):
		my_data[queen_no] = [my_data[queen_no][0], my_data[queen_no][1] - 1]
		if (my_data[queen_no][1] < 1 or is_duplicate_element(my_data, my_data[queen_no])):
			my_data[queen_no][0] = temp[0]
			my_data[queen_no][1] = temp[1]
			return False
		return True
	elif (move_no == 0):
		my_data[queen_no] = [my_data[queen_no][0] - 1, my_data[queen_no][1] - 1]
		if (my_data[queen_no][0] < 1 or my_data[queen_no][1] < 1 or is_duplicate_element(my_data, my_data[queen_no])):
			my_data[queen_no][0] = temp[0]
			my_data[queen_no][1] = temp[1]
			return False
		return True
	elif (move_no == 2):
		my_data[queen_no] = [my_data[queen_no][0] - 1, my_data[queen_no][1] + 1]
		if (my_data[queen_no][0] < 1 or my_data[queen_no][1] > num_of_moves or is_duplicate_element(my_data, my_data[queen_no])):
			my_data[queen_no][0] = temp[0]
			my_data[queen_no][1] = temp[1]
			return False
		return True
	elif (move_no == 4):
		my_data[queen_no] = [my_data[queen_no][0] + 1, my_data[queen_no][1] + 1]
		if (my_data[queen_no][0] > num_of_moves or my_data[queen_no][1] > num_of_moves or is_duplicate_element(my_data, my_data[queen_no])):
			my_data[queen_no][0] = temp[0]
			my_data[queen_no][1] = temp[1]
			return False
		return True
	elif (move_no == 6):
		my_data[queen_no] = [my_data[queen_no][0] + 1, my_data[queen_no][1] - 1]
		if (my_data[queen_no][0] > num_of_moves or my_data[queen_no][1] < 1 or is_duplicate_element(my_data, my_data[queen_no])):
			my_data[queen_no][0] = temp[0]
			my_data[queen_no][1] = temp[1]
			return False
		return True

def print_grid(my_data):
	for i in range(n_queens):
		for j in range(n_queens):
			flag = False
			for k in range(n_queens):
				if (my_data[k][0] == i + 1 and my_data[k][1] == j + 1):
					print('X', end = ' ')
					flag = True
					break
			if (flag == False):
				print('O', end = ' ')
		print()


def copy_board(my_data):
	temp = []
	for i in range(n_queens):
		temp.append([int(my_data[i][0]), int(my_data[i][1])])
	return temp
def generate_next_children(my_data):
	children = []
	for i in range(n_queens):
		for j in range(num_of_moves):
			if(move_if_possible(my_data, i, j)):
				# children.append([(q_pos if q_pos != parent_q else child_q) for q_pos in my_data])
				children.append(copy_board(my_data))
				if (j < 4):
					move_if_possible(my_data, i, j + 4)
				else:
					move_if_possible(my_data, i, j - 4)
	return children


def IDS(root_grid):
	i = 1
	while (True):
		result = DFS(root_grid, i)
		if (result != None):
			return result
		i += 1


def DFS(root_grid, limit):
	s = [(root_grid, 0)]
	all_moves = 0
	while len(s) > 0:
		all_moves += 1
		parent_grid, parent_level = s.pop(0)
		if parent_level > limit:
			continue
		if (num_of_threats(parent_grid) == 0):
			return parent_grid, limit, all_moves
		for child_grid in generate_next_children(parent_grid):
			s.append((child_grid, parent_level + 1))

# def BFS()





def A_star(root_grid):
	nodes = [root_grid]
	levels = [0]
	measures = [0 + num_of_threats(root_grid)]
	moves = 0
	while(True):
		moves += 1
		min_index = measures.index(min(measures))
		node = nodes.pop(min_index)
		level = levels.pop(min_index)
		measure = measures.pop(min_index)
		if (num_of_threats == 0):
			return node, level, moves
		temp = generate_next_children(node)
		for i in range(len((temp))):
			nodes.append(temp[i])
			levels.append(level + 1)
			measures.append(level + 1 + num_of_threats(temp[i]))






temp_data = genfromtxt(input_file_name, delimiter=',')
data = copy_board(temp_data)
t1 = time()
a, b, c = (A_star(data))
t2 = time()
if (a != None):
	print_grid(a)
else:
	print(None)
print(b, 'level')
print(c, 'all moves')
print(t2 - t1, 'time')
