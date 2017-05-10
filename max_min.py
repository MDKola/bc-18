def find_max_min(my_list):
	max_min_list = []
	for number in my_list:
		if number == min(my_list):
			max_min_list.append(number)
		if number == max(my_list):
			max_min_list.append(number)
		if min(my_list) == max(my_list):
			return [len(my_list)]
		
		
	return sorted(max_min_list)
print (find_max_min([4,4,4,4]))