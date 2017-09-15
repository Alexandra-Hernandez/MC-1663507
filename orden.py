cnt_burbuja=0
cnt_insertion=0
cnt_selection=0
cnt_quick=0
def burbuja(A):
	global cnt_burbuja
	cnt_burbuja=0
	for i in range (0, len(A)-1):
		for j in range(0, len(A)-1):
			cnt_burbuja+=1
			if(A[j+1]<A[j]):
				aux = A[j+1]
				A[j+1]=A[j]
				A[j]=aux
	return cnt_burbuja



def orden_por_inserccion(array):
	global cnt_insertion
	cnt_insertion=0
	for indice in range(1, len(array)):
		valor = array[indice]
		i=indice-1       
		while i>=0:
			cnt_insertion+=1
			if valor<array[i]:
				array[i+1]=array[i]
				array[i]=valor
				i-=1
			else:
				break
	return cnt_insertion



def selection(arr):
	global cnt_selection
	cnt_selection=0
	for i in range(0,len(arr)-1):
		val= i
		for j in range(i+1, len(arr)):
			cnt_selection+=1
			if arr[j]< arr[val]:
				val=j
		if val != i:
			aux=arr[i]
			arr[i]=arr[val]
			arr[val]=aux
	return cnt_selection


def quicksort(arr):
	global cnt_quick
	if len(arr)<=1:
		return arr
	p=arr.pop(0)
	menores,mayores=[],[]	
	for e in arr:
		cnt_quick+=1
		if e<=p:
			menores.append(e)	
		else:
			mayores.append(e)
	#print(cnt_quick)
	#return quicksort(menores) + [p] + quicksort(mayores)

import random
def rndar(longitud):
	arr=[]
	for r in range(longitud):
		arr.append(random.randint(0,longitud))
	return arr

import copy
L=4
print("Longitud", "Burbuja", "Selection", "Insertion", "Quick")
while L<1100:
	for replica in range(30):
		
		
		
		arr = rndar(L)
		a, b, c, d = copy.deepcopy(arr), copy.deepcopy(arr), copy.deepcopy(arr), copy.deepcopy(arr)
		bc = burbuja(a)
		ic = orden_por_inserccion(b)
		sc = selection(c)
		cnt_quick=0
		qc = quicksort(d)
	
		print(L, bc, ic, sc, qc)
		
	L*=2 