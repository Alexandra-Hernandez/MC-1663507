import random
cnt=0

def quicksort(arr):
	global cnt
	if len(arr)<=1:
		return arr
	p=arr.pop(0)
	menores,mayores=[],[]	
	for e in arr:
		cnt+=1
		if e<=p:
			menores.append(e)	
		else:
			mayores.append(e)
	return quicksort(menores) + [p] + qicksort(mayores)
def rndar(long):
	arr=[]
	for i in range(long):
		arr.append(random,randint(0,long))
	return arr
l=10

while l<=10:
	for replica in range(10):
		ori=rndar(1)
		arr=qicksort(ori)
		print(1,cnt,arr,ori)
		cnt=0
	l*=2
]