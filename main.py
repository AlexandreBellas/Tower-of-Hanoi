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

#Função de busca em profundidade (dfs)
def dfs(estado, states_gone=[]):
	if estado.pins[0].isEmpty() and (estado.pins[1].isEmpty()):
		print("----------------Estado Atual----------------")
		estado.printState()
		print("Estado final alcançado!")
		quit()

	#Printa no terminal como esta o estado atual
	print("----------------Estado Atual----------------")
	estado.printState()

	#Gera automaticamente os proximos estados
	estado.generateNextStates()

	#Printa todos os filhos do estado atual
	#estado.printNeighbors()

	flag = 0

	#Para cada estado filho
	for est in estado.next_states:
		
		#verificar se já não se passou nele
		for gone in states_gone:
			if not est.isItemDifferent(gone):
				#Se já passou, flag recebe 1
				flag = 1
				break
		
		#Essa verificação é necessária para ir ao próximo estado
		if flag == 1:
			break

		#Se não passou, acrescenta-se aos estados já passados
		states_gone.append(est)

		#Acrescenta-se o número de passos
		global passos
		passos += 1
		print("passos: %d " % passos)

		#Recursivamente, busca em profundidade no filho
		dfs(est, states_gone)

		#Se volta da recursão, é feito um passo a mais
		passos += 1
		print("passos: %d" % passos)

		#Na volta da recursao printa na tela o estado que esta voltando
		print("----------------Estado Atual----------------")
		estado.printState()



"""
First State for 3 pieces:

 0
 1
 2
pin1  pin2  pin3
"""
#creating the first state for a Tower of Hanoi with 3 pieces:
s = State()
place_holder_father = State()
place_holder_father.addState(s)


N = 3
for i in range(N):
	s.pins[0].push(N-i-1)

s.addFather(place_holder_father)

dfs(s)

print("Numero de passos %d" % passos)