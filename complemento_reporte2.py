class Pila:
	def __init__(self):
		self.pila = []
	
	def obtener(self):
		return self.pila.pop()
	def meter(self, e):
		self.pila.append(e)
		return len(self.pila)
	@property
	def longitud(self):
		return len(self.pila)

class Fila:
	def __init__(self):
		self.fila = []
	
	def obtener(self):
		return self.fila.pop()
	def meter(self, e):
		self.fila.insert(0,e)
		return len(self.fila)
	@property
	def longitud(self):
		return len(self.fila)

class Grafo:
	def __init__(self):
		self.V=set()
		self.E=dict()
		self.vecinos=dict()
		
	def agrega(self, v):
		self.V.add(v)
		if not v in self.vecinos:
			self.vecinos[v]=set()
	def conecta(self, v, u, peso=1):
		self.agrega(v)
		self.agrega(u)
		self.E[(v, u)] = self.E[(u, v)] = peso
		self.vecinos[v].add(u)
		self.vecinos[u].add(v)
	@property
	def complemento(self):
		comp = Grafo()
		for v in self.V:
			for w in self.V:
				if v != w and (v, w) not in self.E:
					comp.conecta(v, w, 1)

def bfs(grafo, nodo_inicial):
	visitados=[nodo_inicial]
	f=Fila()
	f.meter(nodo_inicial)
	while f.longitud>0:
		na= f.obtener()
		vecinos= grafo.vecinos[na]
		for nodo in vecinos:
			if  nodo not in visitados:
				visitados.append(nodo)
				f.meter(nodo) 
	return visitados

def dfs(grafo, nodo_inicial):
	visitados=[]
	f=Pila()
	f.meter(nodo_inicial)
	while f.longitud>0:
		na= f.obtener()
		if na in visitados:
			continue
		visitados.append(na)
		vecinos= grafo.vecinos[na]
		for nodo in vecinos:
			if  nodo not in visitados:
				f.meter(nodo) 
	return visitados



graph=Grafo()
graph.conecta(1,2)
graph.conecta(1,3)
graph.conecta(3,4)
graph.conecta(3,7)
graph.conecta(2,5)
graph.conecta(2,8)
graph.conecta(1,6)
print(bfs(graph,1))
print(dfs(graph,1))

#resultados: bfs = [1, 2, 3, 6, 8, 5, 4, 7] y dfs = [1, 6, 3, 7, 4, 2, 5, 8]