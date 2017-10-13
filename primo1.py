cnt=0
def primo (n):
	global cnt
	cnt=0
	for i in range(2, round(n**(1/2)+1)):
		cnt+=1
		if n%i==0:
			return("no es primo")
	return ("es primo")

primo(3)
primo(73)
primo(25)