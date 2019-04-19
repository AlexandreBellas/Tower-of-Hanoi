from models import Pin, State
import time

#Função de busca em profundidade (dfs)
class Search:
	#Constructor
	def __init__(self):
		self.passos = 0
		self.tempo_espera = True
		self.tempo = 1

	#This function is auxiliar to print on the stdin or on the UI
	def __includeTextToInterface(self, text, mode, increment=False, interface=None):
		if interface == None:
			print(text)
		else:
			if mode == 'hc':
				if increment:
					interface.LabelHC['text'] += text
				else:
					interface.LabelHC['text'] = text
			elif mode == 'dfs':
				if increment:
					interface.LabelDFS['text'] += text
				else:
					interface.LabelDFS['text'] = text


	#=============================================================================#

	#Auxiliar function to set passos to 0
	def dfs(self, estado, states_gone=[], interface=None):
		self.passos = 0
		self.__dfsAlgorithm(estado, states_gone, interface)

	#DFS algorithm
	def __dfsAlgorithm(self, estado, states_gone=[], interface=None):
		if estado.pins[0].isEmpty() and (estado.pins[1].isEmpty()):
			text = "----------------Estado Atual----------------\n\n" + estado.printStateString() + "\nEstado final alcançado!\n"  
			self.__includeTextToInterface(text=text, mode='dfs', increment=True, interface=interface)
			return 0

		#Printa no terminal como esta o estado atual
		text = "----------------Estado Atual----------------\n\n" + estado.printStateString()
		self.__includeTextToInterface(text=text, mode='dfs', increment=True, interface=interface)

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

			#Espera-se um tempo para o usuário
			if self.tempo_espera:
				time.sleep(self.tempo)

			#Acrescenta-se o número de passos
			self.passos += 1
			text = "passos: " + str(self.passos) + "\n\n"
			self.__includeTextToInterface(text=text, mode='dfs', interface=interface)

			#Recursivamente, busca em profundidade no filho
			if(self.__dfsAlgorithm(est, states_gone, interface) == 0):
				return 0
			else:
				#Se volta da recursão, é feito um passo a mais
				self.passos += 1
				text = "passos: " + str(self.passos) + "\n\n"
				self.__includeTextToInterface(text=text, mode='dfs', interface=interface)

				#Na volta da recursao printa na tela o estado que esta voltando
				text = "----------------Estado Atual----------------\n\n" + estado.printStateString()
				self.__includeTextToInterface(text=text, mode='dfs', increment=True, interface=interface)

	#=============================================================================#

	#Auxiliar function to set passos to 0
	def hillClimbing(self, estado, interface=None):
		self.passos = 0
		self.__hillClimbingAlgorithm(estado, interface)

	#Private function that auxiliates hill climbing algorithm
	def __calculateScore(self, estado):
		return 2*len(estado.pins[0].items) + len(estado.pins[1].items)

	#Heuristic algorithm hill climbing
	def __hillClimbingAlgorithm(self, estado, interface=None):
		self.passos += 1
		text = "passos: " + str(self.passos) + "\n\n"
		self.__includeTextToInterface(text=text, mode='hc', interface=interface)
		#print("passos: %d" % self.passos)
		
		#Verificação se está no estado final
		if estado.pins[0].isEmpty() and (estado.pins[1].isEmpty()):
			text = "----------------Estado Atual----------------\n\n" + estado.printStateString() + "\nEstado final alcançado!\n"  
			self.__includeTextToInterface(text=text, mode='hc', increment=True, interface=interface)
			return

		#Printando estado atual
		text = "----------------Estado Atual----------------\n\n" + estado.printStateString()
		self.__includeTextToInterface(text=text, mode='hc', increment=True, interface=interface)

		#Gerando todos os próximos estados
		estado.generateNextStates()

		#Calculando o score de todos os próximos estados
		scores = []
		for est in estado.next_states:
			scores.append(self.__calculateScore(est))

		#Tempo para percepção do usuário
		if self.tempo_espera:
			time.sleep(self.tempo)

		#Indo recursivamente para o próximo estado com menor score
		self.__hillClimbingAlgorithm(estado.next_states[scores.index(min(scores))], interface)

	#=============================================================================#