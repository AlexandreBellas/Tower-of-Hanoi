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

#Função de busca em profundidade (dfs)
def dfs(estado, states_gone=[]):
	if estado.pins[0].isEmpty() and (estado.pins[1].isEmpty()):
		print("----------------Estado Atual----------------")
		estado.printState()
		print("Estado final alcançado!")
		return 0

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
		if(dfs(est, states_gone) == 0):
			return 0
		else:
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
# s = State()
# place_holder_father = State()
# place_holder_father.addState(s)


# N = 3
# for i in range(N):
# 	s.pins[0].push(N-i-1)

# s.addFather(place_holder_father)

s = State()
place_holder_father = State()
place_holder_father.addState(s)


N = 3
for i in range(N):
	s.pins[0].push(N-i-1)

s.addFather(place_holder_father)

while True:
	input("Oi, eu sou o potato. Aperte enter para continuar com a DFS!")
	
	passos = 0
	
	dfs(s, [])
	
	print("Muito bem! Cabou um DFS. Perae um minuto.")
	time.sleep(2)

	os.system("clear")

print("Numero de passos %d" % passos)