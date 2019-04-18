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
		#TODO: Encapsular a verificacao do tamanho
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
		self.pins = [Pin() for j in range(3)]
		self.next_states = []
		self.father = 0

	#Methods:
	#Retorna true se o estado "state" for diferente do estado atual, false caso contrario
	def isItemDifferent(self, state):
		for pin_self, pin_state in zip(self.pins, state.pins):
			if pin_self.items != pin_state.items:
				return True
		return False

	#Adiciona um estado na lista de estados vizinhos
	def addState(self, state):
		#Garantees that the neighbor is a different state
		if self.isItemDifferent(state):
			self.next_states.append(state)
	#Copia o estado atual em um novo estado
	def copyState(self, state):
		for j in range(len(self.pins)):
			for i in range(self.pins[j].size()):
				state.pins[j].push(self.pins[j].items[i])

	#Retorna o numero de estados vizinhos
	def numNeighbor(self):
		return len(self.next_states)
	#Adiciona um pai
	def addFather(self, state):
		self.father = state
	#Verifica se os irmaos do estado atual sao diferente do estado
	def diffUncle(self, state):
		for i in range (self.father.numNeighbor()):
			if not self.father.next_states[i].isItemDifferent(state):
				return False
		return True
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
	def printState(self):
		s = State()
		self.copyState(s)
		for j in range(len(self.pins)):
			if s.pins[j].isEmpty():
				print("<empty>\n")
			for i in range(0, s.pins[j].size()):
				print(s.pins[j].pop(), end='\n')
			print("Pino %d ^ " % j, end='\n\n')

	
	def generateNextStates(self):
		for i in range(len(self.pins)):
			if not self.pins[i].isEmpty():
				piece = self.pins[i].pop()
				for j in range(len(self.pins)):
					if j != i:
						if self.pins[j].isEmpty():
							s = State()
							self.copyState(s)
							s.pins[j].push(piece)
							s.addFather(self)
							#Condition to check if grandpa is different fron grandson
							if (self.father.isItemDifferent(s)):
								#Condition to check if uncle is different from nephew
								if (self.diffUncle(s)):
									self.addState(s)
								else:
									del s
							else:
								del s
						elif piece < self.pins[j].peek():
							s = State()
							self.copyState(s)
							s.pins[j].push(piece)
							s.addFather(self)
							#Condition to check if grandpa is different fron grandson
							if (self.father.isItemDifferent(s)):
								#Condition to check if uncle is different from nephew
								if (self.diffUncle(s)):
									self.addState(s)
								else:
									del s
							else:
								del s
				#Voltando a peca original no seu lugar devido
				self.pins[i].push(piece)