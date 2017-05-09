class Primes(object):
	def __init__(self):
		pass

	def is_prime(n):
	    status = True
	    if type(n) is int:
		    if n < 2:
		        status = False
		    else:
		        for i in range(2,n):
		            if n % i == 0:
		                status = False
		    return status

	


