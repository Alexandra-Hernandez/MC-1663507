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
graph.conecta(2,5)
graph.conecta(1,6)
print(dfs(graph,1))