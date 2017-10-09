import math
def primo (n):
	for i in range(2, round(n**(1/2)+1)):
		if n&i==0:
			return("no es primo")
	return ("es primo")
