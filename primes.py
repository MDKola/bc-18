def is_prime(n):
    status = True
    if isinstance(n,float):
    	return "Sorry! Prime numbers are whole"
    if (n <= 0):
    	return "Enter a positive number"
    if not isinstance(n,int):
		return "Enter a number"
    else:
	    if n < 2:
	        status = False
	    else:
	        for i in range(2,n):
	            if n % i == 0:
	                status = False
	    return status


	


