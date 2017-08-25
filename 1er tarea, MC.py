Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
a=[]
for y in range (100):
    p.append(y)

def min (arreglo):
    aux= arreglo #Se crea un arreglo auxiliar
    result=0
    for num1 in arreglo: #Para cada elemento del arreglo o conjunto
        aux.pop(num1) #Saca el num1 del arreglo-conjunto auxiliar
        for num2 in aux: #Para cada elemento de num2 del conjunto auxiliar
                   if(num1>num2): #Compara si num1 es mayor a num2
                       break #Si lo es, salgo para probar el siguiente num1, si no comaparo num1 con el seiguiente num2
                    result=num1
        result=num1
        break
    return result
SyntaxError: multiple statements found while compiling a single statement
>>> 
