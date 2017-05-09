def data_type(arguement):
	if type(arguement) is str:
		return len(arguement)

	elif (arguement) is None:
		return "no value"

	elif type(arguement) is bool:
		return arguement

	elif type(arguement) is int:
		if arguement < 100:
			return "less than 100"
		elif arguement == 100:
			return "equal to 100"
		else:
			return"more than 100"

	elif type(arguement) is list:
		if len(arguement) > 2:
			return arguement[2]
		else:
			return None
	else:
		return "Invalid input"




