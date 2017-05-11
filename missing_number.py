def find_missing(list_A, list_B):
	#the function compares two lists and returns the missing number

	if len(list_A) == len(list_B) == 0:
		return 0

	if not set(list_A).symmetric_difference(set(list_B)):
		return 0
	else:
		return list(set(list_A).symmetric_difference(set(list_B)))[0]

list_A = [1,2,3,4,5]
list_B = [1,2,3]
print (find_missing(list_A, list_B))