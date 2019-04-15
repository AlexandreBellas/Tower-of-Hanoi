"""
**************************************************************************************
This archive contains all objects used for the Tower of Hanoi problem
They are:
State - an object consisting of three pins and an array of next state's
Pin - an object that works just like a stack (Last in - First out) for pieces
Pieces - int's and the size of each one is represented by it's number
Ex: In a tower of hanoi problem of 3 pieces
	we have the pieces 0 1 2, in which 0 is the smallest and 2 the largest
**************************************************************************************
"""
class Pin:
	#Constructor:
	def __init__(self):
		self.items = []

	#Methods:
	#Retorna true se a pilha esta vazia, false caso contrario
	def isEmpty(self):
		return (self.items == [])
	#Adiciona na pilha
	def push(self, item):
		self.items.append(item)
	#Remove da pilha e retorna o valor
	def pop(self):
		return self.items.pop()
	#Retorna o valor sem remover da pilha
	def peek(self):
		return self.items[len(self.items)-1]
	#Retorna o tamanho da pilha
	def size(self):
		return len(self.items)

class State:
	#Constructor:
	def __init__(self):
		self.pin1 = Pin()
		self.pin2 = Pin()
		self.pin3 = Pin()
		self.next_states = []
		self.father = []

	#Methods:
	#Retorna true se o estado "state" for diferente do estado atual, false caso contrario
	def isDifferent(self, state):
		if self.pin1.items != state.pin1.items:
			return True
		elif self.pin2.items != state.pin2.items:
			return True
		elif self.pin3.items != state.pin3.items:
			return True
		else:
			return False
	#Adiciona um estado na lista de estados vizinhos
	def add_state(self, state):
		#Garantees that the neighbor is a different state
		if self.isDifferent(state):
			self.next_states.append(state)
	#Copia o estado atual em um novo estado
	def copy_state(self, state):
		for i in range(0, self.pin1.size()):
			state.pin1.push(self.pin1.items[i])
		for i in range(0, self.pin2.size()):
			state.pin2.push(self.pin2.items[i])
		for i in range(0, self.pin3.size()):
			state.pin3.push(self.pin3.items[i])
	#Retorna o numero de estados vizinhos
	def num_neighbor(self):
		return len(self.next_states)
	#Adiciona um pai
	def add_father(self, state):
		self.father.append(state)
#	Printa no terminal o estado dos pinos com as peças
#	Formato do print para uma torre de hanoi com 3 peças no estado inicial:
#	0
#	1
#	2
#	Pino 1 ^ 
#
#	<empty>
#
#	Pino 2 ^ 
#
#	<empty>
#
#	Pino 3 ^ 
	def print_state(self):
		s = State()
		self.copy_state(s)
		if s.pin1.isEmpty():
			print("<empty>\n")
		for i in range(0, s.pin1.size()):
			print(s.pin1.pop(), end='\n')
		print("Pino 1 ^ ", end='\n\n')
		if s.pin2.isEmpty():
			print("<empty>\n")
		for i in range(0, s.pin2.size()):
			print(s.pin2.pop(), end='\n')
		print("Pino 2 ^ ", end='\n\n')
		if s.pin3.isEmpty():
			print("<empty>\n")
		for i in range(0, s.pin3.size()):
			print(s.pin3.pop(), end='\n')
		print("Pino 3 ^ ", end='\n\n')
