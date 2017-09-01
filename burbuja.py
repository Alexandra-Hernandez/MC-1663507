def burbuja(A):
	for i in range (0, len(A)-1):
		for j in range(0, len(A)-1):
			if(A[j+1]<A[j]):
				aux = A[j+1]
				A[j+1]=A[j]
				A[j]=aux
	return A

A=[5, 4, 56, 0, 3, 56, 18]
print (A)
burbuja (A)

			
	