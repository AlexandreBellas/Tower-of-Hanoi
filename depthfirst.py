from models import Pin, State

#Função de busca em profundidade (dfs)
class Dfs:
	def __init__(self, passos):
		self.passos = passos

	def busca(self, estado, states_gone=[]):
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
			self.passos += 1
			print("passos: %d " % self.passos)

			#Recursivamente, busca em profundidade no filho
			if(self.busca(est, states_gone) == 0):
				return 0
			else:
				#Se volta da recursão, é feito um passo a mais
				self.passos += 1
				print("passos: %d" % self.passos)

				#Na volta da recursao printa na tela o estado que esta voltando
				print("----------------Estado Atual----------------")
				estado.printState()