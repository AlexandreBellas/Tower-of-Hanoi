def calculateScore(state):
	return 2*len(state.pins[0]) + len(state.pins[1])

def hillClimbing(estado):
	#Verificação se está no estado final
	if estado.pins[0].isEmpty() and (estado.pins[1].isEmpty()):
		print("----------------Estado Atual----------------")
		estado.printState()
		print("Estado final alcançado!")
		quit()

	#Printando estado atual
	print("----------------Estado Atual----------------")
	estado.printState()

	#Gerando todos os próximos estados
	estado.generateNextStates()

	#Calculando o score de todos os próximos estados
	scores = []
	for est in estado.next_states:
		scores.append(calculateScore(est))

	#Indo recursivamente para o próximo estado com menor score
	hillClimbing(scores[scores.index(min(scores))])



