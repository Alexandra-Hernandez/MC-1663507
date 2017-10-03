def primo(n):
	a=0
	cnt=0
	for i in range(1,n+1):
		cnt=cnt+1
		if((n%i)==0):
			a=a+1
	if a>2:
		return ("Es numero compuesto"), cnt
	if a==2:
		return("Es numero primo"), cnt

	
		