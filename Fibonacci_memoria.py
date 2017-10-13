memo={}
cnt2=0
def fibonacci(n):
	global memo, cnt2
	cnt2+=1
	if n==0 or n==1:
        	return(1)
	if n in memo:
        	return memo[n]
	else:
        	val=fibonacci(n-2)+fibonacci(n-1)
        	memo[n]=val
        	return val

for i in range (2, 10): 
	cnt2=0
	print(i, fibonacci(i), cnt2 )