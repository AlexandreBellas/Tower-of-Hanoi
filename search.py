from models import Pin, State
import time

#Função de busca em profundidade (dfs)
class Search:
	#Constructor
	def __init__(self):
		self.passos = 0
		self.tempo_espera = True
		self.tempo = 0

	#=============================================================================#

	#Auxiliar function to set passos to 0
	def dfs(self, estado, states_gone=[]):
		self.passos = 0
		self.__dfsAlgorithm(estado, states_gone)

	#DFS algorithm
	def __dfsAlgorithm(self, estado, states_gone=[]):
		if estado.pins[0].isEmpty() and (estado.pins[1].isEmpty()):
			text = "----------------Estado Atual----------------\n\n" + estado.printStateString() + "\nEstado final alcançado!\n"  
			print(text)
			return 0

		#Printa no terminal como esta o estado atual
		text = "----------------Estado Atual----------------\n\n" + estado.printStateString()
		print(text)

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
			print(text)

			#Recursivamente, busca em profundidade no filho
			if(self.__dfsAlgorithm(est, states_gone) == 0):
				return 0
			else:
				#Se volta da recursão, é feito um passo a mais
				self.passos += 1
				text = "passos: " + str(self.passos) + "\n\n"
				print(text)

				#Na volta da recursao printa na tela o estado que esta voltando
				text = "----------------Estado Atual----------------\n\n" + estado.printStateString()
				print(text)

	#=============================================================================#

	#Auxiliar function to set passos to 0
	def hillClimbing(self, estado):
		self.passos = 0
		self.__hillClimbingAlgorithm(estado)

	#Private function that auxiliates hill climbing algorithm
	def __calculateScore(self, estado):
		return 2*len(estado.pins[0].items) + len(estado.pins[1].items)

	#Heuristic algorithm hill climbing
	def __hillClimbingAlgorithm(self, estado):
		self.passos += 1
		text = "passos: " + str(self.passos) + "\n\n"
		print(text)
		#print("passos: %d" % self.passos)
		
		#Verificação se está no estado final
		if estado.pins[0].isEmpty() and (estado.pins[1].isEmpty()):
			text = "----------------Estado Atual----------------\n\n" + estado.printStateString() + "\nEstado final alcançado!\n"  
			print(text)
			return 0

		#Printando estado atual
		text = "----------------Estado Atual----------------\n\n" + estado.printStateString()
		print(text)

		#Gerando todos os próximos estados
		estado.generateNextStates(check_grandpas_and_uncles=True)

		#Calculando o score de todos os próximos estados
		scores = []
		for est in estado.next_states:
			scores.append(self.__calculateScore(est))

		#Tempo para percepção do usuário
		if self.tempo_espera:
			time.sleep(self.tempo)

		scores_sorted = sorted(scores)
		print(scores)
		print(scores_sorted)

		#Indo recursivamente para o próximo estado do menor score ao maior score
		for scr in scores_sorted:
			scr = scores_sorted[0]
			print("scores.index(scr) =", scores.index(scr))
			print("pino 0 prox estado =", estado.next_states[scores.index(scr)].pins[0].items)
			print("pino 1 prox estado =", estado.next_states[scores.index(scr)].pins[1].items)
			print("pino 2 prox estado =", estado.next_states[scores.index(scr)].pins[2].items)
			input("Enter para continuar!")
			if self.__hillClimbingAlgorithm(estado.next_states[scores.index(scr)]) == 0:
				return 0

		#self.__hillClimbingAlgorithm(estado.next_states[scores.index(min(scores))])

	#=============================================================================#