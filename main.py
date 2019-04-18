"""
**************************************************************************************
This is the main archive of the Tower of Hanoi problem
**************************************************************************************
"""
#Lariça is watching
#lariça is testing

from models import Pin, State
import time
import os


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
				#Condition to check if uncle is different from nephew
				if (state.diff_uncle(s)):
					state.add_state(s)
				else:
					del s
			else:
				del s
		elif piece < state.pin2.peek():
			s = State()
			state.copy_state(s)
			s.pin2.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				#Condition to check if uncle is different from nephew
				if (state.diff_uncle(s)):
					state.add_state(s)
				else:
					del s
			else:
				del s

		if state.pin3.isEmpty():
			s = State()
			state.copy_state(s)
			s.pin3.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				#Condition to check if uncle is different from nephew
				if (state.diff_uncle(s)):
					state.add_state(s)
				else:
					del s
			else:
				del s
		elif piece < state.pin3.peek():
			s = State()
			state.copy_state(s)
			s.pin3.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				#Condition to check if uncle is different from nephew
				if (state.diff_uncle(s)):
					state.add_state(s)
				else:
					del s
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
				#Condition to check if uncle is different from nephew
				if (state.diff_uncle(s)):
					state.add_state(s)
				else:
					del s
			else:
				del s
		elif piece < state.pin1.peek():
			s = State()
			state.copy_state(s)
			s.pin1.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				#Condition to check if uncle is different from nephew
				if (state.diff_uncle(s)):
					state.add_state(s)
				else:
					del s
			else:
				del s

		if state.pin3.isEmpty():
			s = State()
			state.copy_state(s)
			s.pin3.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				#Condition to check if uncle is different from nephew
				if (state.diff_uncle(s)):
					state.add_state(s)
				else:
					del s
			else:
				del s
		elif piece < state.pin3.peek():
			s = State()
			state.copy_state(s)
			s.pin3.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				#Condition to check if uncle is different from nephew
				if (state.diff_uncle(s)):
					state.add_state(s)
				else:
					del s
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
				#Condition to check if uncle is different from nephew
				if (state.diff_uncle(s)):
					state.add_state(s)
				else:
					del s
			else:
				del s
		elif piece < state.pin1.peek():
			s = State()
			state.copy_state(s)
			s.pin1.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				#Condition to check if uncle is different from nephew
				if (state.diff_uncle(s)):
					state.add_state(s)
				else:
					del s
			else:
				del s

		if state.pin2.isEmpty():
			s = State()
			state.copy_state(s)
			s.pin2.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				#Condition to check if uncle is different from nephew
				if (state.diff_uncle(s)):
					state.add_state(s)
				else:
					del s
			else:
				del s
		elif piece < state.pin2.peek():
			s = State()
			state.copy_state(s)
			s.pin2.push(piece)
			s.add_father(state)
			#Condition to check if grandpa is different fron grandson
			if (state.father[0].isDifferent(s)):
				#Condition to check if uncle is different from nephew
				if (state.diff_uncle(s)):
					state.add_state(s)
				else:
					del s
			else:
				del s

		state.pin3.push(piece)

passos = 0

def dfs(estado, states_gone=[]):
	if estado.pin1.isEmpty() and (estado.pin2.isEmpty()):# or estado.pin2.isEmpty()):
		print("Estado final alcançado")
		quit()

	#Printa no terminal como esta o estado atual
	print("----------------Estado Atual----------------")
	estado.print_state()

	#Gera automaticamente os proximos estados
	generate_next_states(estado)

	#TODO: add method to print neighbor in the State class in models.py
	#Printa todos os filhos do estado inicial
	for i in range(0, estado.num_neighbor()):
		print("-------------------Filho %d-------------------" % i)
		estado.next_states[i].print_state()

	#input("Aperta ai krai")
	#os.system("clear")

	#time.sleep(5)
	flag = 0

	for est in estado.next_states:
		
		for gone in states_gone:
			if not est.isDifferent(gone):
				flag = 1
				break
			
		if flag == 1:
			break

		states_gone.append(est)
		global passos
		passos += 1
		print("passos = %d" % passos)
		dfs(est, states_gone)

		passos += 1
		print("passos = %d" % passos)
		estado.print_state_reduced()


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
place_holder_father.add_state(s)
s.pin1.push(2)
s.pin1.push(1)
s.pin1.push(0)
s.add_father(place_holder_father)

estado_atual = s
entrada = 0

dfs(s)


# #TODO: run the depth search iteratively
# #TODO: add an algorithm to store in a file all states that we already went through (dynamic programming)
# #TODO: using that file, add an algorithm to run the depth search recursively
# while(entrada != "exit"):
# 	#Printa no terminal como esta o estado inicial
# 	print("----------------Estado Atual----------------")
# 	estado_atual.print_state()

# 	#Gera automaticamente os proximos estados
# 	generate_next_states(estado_atual)

# 	#TODO: add method to print neighbor in the State class in models.py
# 	#Printa todos vizinhos do estado inicial
# 	for i in range(0, estado_atual.num_neighbor()):
# 		print("-------------------Filho %d-------------------" % i)
# 		estado_atual.next_states[i].print_state()

# 	entrada = input("Filho a percorrer: ")
# 	if entrada != "exit":
# 		estado_atual = estado_atual.next_states[int(entrada)]
