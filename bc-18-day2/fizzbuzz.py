def fizz_buzz(number):
	if (number % 5 == 0) and (number % 3 == 0):
		return "FizzBuzz"
	elif number%3 == 0:
		return "Fizz"
	elif number%5 == 0:
		return "Buzz"
	
	elif number%3 != 0 or number%5 != 0:
		return number
