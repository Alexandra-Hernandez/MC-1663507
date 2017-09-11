cnt = 0
def orden_por_inserccion(array):
	global cnt
	for indice in range(1, len(array)):
		valor = array[indice]#valor es el elemento que vamos a comparar 
		i=indice-1     #i es el valor anterior al elemento que estamos comparando     
		while i>=0:
			cnt+=1
			if valor<array[i]:#comparamos valor con el elemento anterior 
				array[i+1]=array[i]
				array[i]=valor
				i-=1
			else:
				break
	return array, cnt 

a=[4, 5, 6, 0, 1, 6]
print(a)
orden_por_inserccion(a)