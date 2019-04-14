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
		return self.items == []
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