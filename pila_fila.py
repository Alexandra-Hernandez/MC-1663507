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

p = Pila()
p.meter(1)
p.meter(2)
p.meter(2)
p.meter(3)
p.meter(100)
p.meter(84563)

print(p.longitud)
print(p.obtener())
print(p.obtener())


l = Fila()
l.meter(1)
l.meter(2)
l.meter(2)
l.meter(3)
l.meter(100)
l.meter(84563)

print(l.longitud)
print(l.obtener())
print(l.obtener())