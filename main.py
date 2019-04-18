"""
**************************************************************************************
This is the main archive of the Tower of Hanoi problem
**************************************************************************************
"""
#Larica is watching
#larica is testing

from models import Pin, State
import time
import os


passos = 0

def dfs(estado, states_gone=[]):
	if estado.pins[0].isEmpty() and (estado.pins[1].isEmpty()):
		print("Estado final alcançado")
		quit()

	#Printa no terminal como esta o estado atual
	print("----------------Estado Atual----------------")
	estado.printState()

	#Gera automaticamente os proximos estados
	estado.generateNextStates()

	#TODO: add method to print neighbor in the State class in models.py
	#Printa todos os filhos do estado inicial
	for i in range(0, estado.numNeighbor()):
		print("-------------------Filho %d-------------------" % i)
		estado.next_states[i].printState()

	#input("Aperta ai krai")
	#os.system("clear")

	#time.sleep(5)
	flag = 0

	for est in estado.next_states:
		
		for gone in states_gone:
			if not est.isItemDifferent(gone):
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
		#estado.print_state_reduced()


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
place_holder_father.addState(s)

N = 3
for i in range(N):
	s.pins[0].push(N-i-1)

s.addFather(place_holder_father)

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
# 	for i in range(0, estado_atual.numNeighbor()):
# 		print("-------------------Filho %d-------------------" % i)
# 		estado_atual.next_states[i].print_state()

# 	entrada = input("Filho a percorrer: ")
# 	if entrada != "exit":
# 		estado_atual = estado_atual.next_states[int(entrada)]
