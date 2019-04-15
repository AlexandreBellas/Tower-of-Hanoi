"""
**************************************************************************************
This is the main archive of the Tower of Hanoi problem
**************************************************************************************
"""
from models import Pin, State


#TODO: add method to generate next states to State class in models.py
#TODO: add condition to check if the next state isn't equal to an uncle state
def generate_next_states(state):

	if (state.pin1.isEmpty() == False):
		piece = state.pin1.pop()

		if state.pin2.isEmpty():
			s = State()
			state.copy_state(s)
			s.pin2.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				state.add_state(s)
			else:
				del s
		elif piece < state.pin2.peek():
			s = State()
			state.copy_state(s)
			s.pin2.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				state.add_state(s)
			else:
				del s

		if state.pin3.isEmpty():
			s = State()
			state.copy_state(s)
			s.pin3.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				state.add_state(s)
			else:
				del s
		elif piece < state.pin3.peek():
			s = State()
			state.copy_state(s)
			s.pin3.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				state.add_state(s)
			else:
				del s

		state.pin1.push(piece)

	if (state.pin2.isEmpty() == False):
		piece = state.pin2.pop()

		if state.pin1.isEmpty():
			s = State()
			state.copy_state(s)
			s.pin1.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				state.add_state(s)
			else:
				del s
		elif piece < state.pin1.peek():
			s = State()
			state.copy_state(s)
			s.pin1.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				state.add_state(s)
			else:
				del s

		if state.pin3.isEmpty():
			s = State()
			state.copy_state(s)
			s.pin3.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				state.add_state(s)
			else:
				del s
		elif piece < state.pin3.peek():
			s = State()
			state.copy_state(s)
			s.pin3.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				state.add_state(s)
			else:
				del s

		state.pin2.push(piece)

	if (state.pin3.isEmpty() == False):
		piece = state.pin3.pop()

		if state.pin1.isEmpty():
			s = State()
			state.copy_state(s)
			s.pin1.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				state.add_state(s)
			else:
				del s
		elif piece < state.pin1.peek():
			s = State()
			state.copy_state(s)
			s.pin1.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				state.add_state(s)
			else:
				del s

		if state.pin2.isEmpty():
			s = State()
			state.copy_state(s)
			s.pin2.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				state.add_state(s)
			else:
				del s
		elif piece < state.pin2.peek():
			s = State()
			state.copy_state(s)
			s.pin2.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				state.add_state(s)
			else:
				del s

		state.pin3.push(piece)

"""
First State for 3 pieces:

 0
 1
 2		
pin1  pin2  pin3
"""
#creating the first state for a Tower of Hanoi with 3 pieces:
#TODO: automatically create the initial state for N pieces
s = State()
place_holder_father = State()
s.pin1.push(2)
s.pin1.push(1)
s.pin1.push(0)
s.add_father(place_holder_father)

estado_atual = s
entrada = 0
#TODO: run the depth search iteratively
#TODO: add an algorithm to store in a file all states that we already went through (dynamic programming)
#TODO: using that file, add an algorithm to run the depth search recursively
while(entrada != "exit"):
	#Printa no terminal como esta o estado inicial
	print("----------------Estado Atual----------------")
	estado_atual.print_state()

	#Gera automaticamente os próximos estados
	generate_next_states(estado_atual)

	#TODO: add method to print neighbor in the State class in models.py
	#Printa todos vizinhos do estado inicial
	for i in range(0, estado_atual.num_neighbor()):
		print("------------------Vizinho %d------------------" % i)
		estado_atual.next_states[i].print_state()

	entrada = input("Vizinho a percorrer: ")
	if entrada != "exit":
		estado_atual = estado_atual.next_states[int(entrada)]
