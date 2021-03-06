from heapq import heappop, heappush
from copy import deepcopy
import random

import time
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst] 
    l = [] # empty list that will store current permutation
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)
    return l
class Pila(object):
    def __init__(self):
        self.a=[]
    def obtener(self):
        return self.a.pop()
    def meter(self,e):
        self.a.append(e)
        return len(self.a)
    @property
    def longitud(self):
        return len(self.a)
class Grafo:
 
    def __init__(self):
        self.V = set() # un conjunto
        self.E = dict() # un mapeo de pesos de aristas
        self.vecinos = dict() # un mapeo
 
    def agrega(self, v):
        self.V.add(v)
        if not v in self.vecinos: # vecindad de v
            self.vecinos[v] = set() # inicialmente no tiene nada
 
    def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v, u)] = self.E[(u, v)] = peso # en ambos sentidos
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
 
    def complemento(self):
        comp= Grafo()
        for v in self.V:
            for w in self.V:
                if v != w and (v, w) not in self.E:
                    comp.conecta(v, w, 1)
        return comp

    
    def DFS(self,ni):
        visitados =[]
        f=Pila()
        f.meter(ni)
        while(f.longitud>0):
            na = f.obtener()
            visitados.append(na)
            ln = self.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados

    def PAV(self):
        perm=permutation(list(self.V))
        mejor=-1
        camino=[]
        for w in perm:
            peso=0
            for i in range(len(w)-1):
                peso+=self.E[(w[i],w[i+1])]
            peso+=self.E[(w[-1],w[0])]
            if peso<mejor or mejor==-1:
                mejor=peso
                camino=w
        return camino

g= Grafo()
g.conecta('1','2', 6.6)
g.conecta('1','3', 17.1)
g.conecta('1','4', 2.6)
g.conecta('1','5', 12.7)
g.conecta('1','6', 13.9)
g.conecta('1','7', 3.9)
g.conecta('1','8', 7.4)
g.conecta('1','9', 6.6)
g.conecta('1','10', 19)
g.conecta('2','3', 10.5)
g.conecta('2','4', 7.4)
g.conecta('2','5', 6.7)
g.conecta('2','6', 22.2)
g.conecta('2','7', 3.7)
g.conecta('2','8', 7.4)
g.conecta('2','9', 9.8)
g.conecta('2','10', 19.4)
g.conecta('3','4', 17)
g.conecta('3','5', 12.4)
g.conecta('3','6', 28)
g.conecta('3','7', 11.6)
g.conecta('3','8', 12.1)
g.conecta('3','9', 16.7)
g.conecta('3','10', 27.4)
g.conecta('4','5', 14)
g.conecta('4','6', 17.7)
g.conecta('4','7', 6.3)
g.conecta('4','8', 8.8)
g.conecta('4','9', 7.2)
g.conecta('4','10', 29.4)
g.conecta('5','6', 27.3)
g.conecta('5','7', 7.6)
g.conecta('5','8', 11)
g.conecta('5','9', 16.2)
g.conecta('5','10', 18.8)
g.conecta('6','7', 20)
g.conecta('6','8', 18)
g.conecta('6','9', 11.8)
g.conecta('6','10', 32.8)
g.conecta('7','8', 3.1)
g.conecta('7','9', 10.5)
g.conecta('7','10', 24.8)
g.conecta('8','9', 8.5)
g.conecta('8','10', 26.4)
g.conecta('9','10', 33.2)


tim=time.clock()
camino=g.PAV()
dfs=camino
mejor=0
for i in range(len(dfs)-1):
    mejor+=g.E[(dfs[i],dfs[i+1])]
mejor+=g.E[(dfs[-1],dfs[0])]
print("El mejor camino fue el siguiente: ")
for k in camino:
    print(k,'->')
print(camino[0])
print("\nCon un costo de ",mejor)
print("Tiempo de ejecucion: ",time.clock()-tim)
print("\n--------------------------------------------------\n\n")

    
