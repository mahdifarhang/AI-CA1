from numpy import genfromtxt

n_queens = 8
input_file_name = 'in1.csv'

def num_of_culumn_threats(my_data):
	threats = 0
	for i in range(n_queens):
		num_of_queens = 0
		for j in range(n_queens):
			if (my_data[j][1] == i + 1):
				num_of_queens += 1
		if (num_of_queens > 1):
			threats += num_of_queens - 1
	return threats

def num_of_row_threats(my_data):
	threats = 0
	for i in range(n_queens):
		num_of_queens = 0
		for j in range(n_queens):
			if (my_data[j][0] == i + 1):
				num_of_queens += 1
		if (num_of_queens > 1):
			threats += num_of_queens - 1
	return threats

# we could count number of rows or columns without queens and the answer would have been the same

def num_of_diameter_threats(my_data):
	threats = 0
	blacklist = []
	for i in range(n_queens):
		for j in range(i + 1, n_queens):
			if (j in blacklist):
				continue
			if (abs(data[i][0] - data[j][0]) == abs(data[i][1] - data[j][1])):
				threats += 1
				blacklist.append(j)
# if the abs wasn't there, we could get num of main diameter threats
# if the abs wasn't there and a minus was behind the right part of equation, we could get num of non_main diameter threats
	return threats

def num_of_threats(my_data):
	return num_of_row_threats(my_data) + num_of_culumn_threats(my_data) + num_of_diameter_threats(my_data)


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
		temp.append([my_data[i][0], my_data[i][1]])
	return temp

def DFS(my_data, k):
	print(k)
	print_grid(my_data)
	if (num_of_threats(my_data) == 0):
		return my_data
	for i in range(n_queens):
		for j in range(num_of_moves):
			if(move_if_possible(my_data, i, j)):
				return(DFS(my_data, k + 1))
				if (j < 4):
					move_if_possible(my_data, i, j + 4)
				else:
					move_if_possible(my_data, i, j - 4)





temp_data = genfromtxt(input_file_name, delimiter=',')
data = copy_board(temp_data)
print_grid(data)
print(num_of_threats(data))
print(end = '\n\n\n')
print_grid(DFS(data, 0))





# k = 0
# for i in range(n_queens):
# 	for j in range(8):
# 		threats = num_of_threats(data)
# 		if(move_if_possible(data, i, j)):
# 			if (num_of_threats(data) > threats):
# 				if (j < 4):
# 					move_if_possible(data, i, j + 4)
# 				else:
# 					move_if_possible(data, i, j - 4)
# 				k += 1
# 			else:
# 				print_grid(data)
# 				print(num_of_threats(data))
# 				print()
# 		else:
# 			k += 1
# print(k)

