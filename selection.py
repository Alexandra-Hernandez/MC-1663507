cnt=0
def selection(arr):
	global cnt
	for i in range(0,len(arr)-1):
		val= i
		for j in range(i+1, len(arr)):
			cnt= cnt + 1
			if arr[j]< arr[val]:
				val=j
		if val != i:
			aux=arr[i]
			arr[i]=arr[val]
			arr[val]=aux
	return arr, cnt

a=[4, 5, 6, 0, 1, 6]
print (a)
selection(a)