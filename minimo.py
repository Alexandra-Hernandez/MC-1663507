def ordenar (a):
	contadora=0
	T=len(a)
	w=0
	while(w!=(T-1)):
		w=0
		for k in range(T-1):
			contadora=contadora+1
			if(a[k]<=a[k+1]):
				w=w+1
			else:
				tem=a[k]
				a[k]=a[k+1]
				a[k+1]=tem
	return a, contadora 
a=[]
for i in range(100):
    a.append(i)

import random
random.shuffle(a)
ordenar(a)
