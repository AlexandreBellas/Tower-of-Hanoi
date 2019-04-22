"""
**************************************************************************************
This is the main archive of the Tower of Hanoi problem
**************************************************************************************
"""
#Larica is watching
#larica is testing

from search import Search
from models import State
import time
import os

#Executará até o fim
while True:
	#É necessária uma entrada numérica
	try:
		num_pieces = int(input("Número de peças (insira 0 para sair): "))
	except ValueError:
		os.system("clear")
		print("Insira números válidos.")
		continue

	#Condição de saída do programa
	if num_pieces == 0:
		os.system("clear")
		quit()

	#Criação do estado inicial com o número de peças inserido
	s = State(initial_state_num_pieces=num_pieces)

	#Instanciação de um objeto de busca
	busca = Search()

	#Realização da busca DFS
	busca.dfs(s, [])
	input("Final do algoritmo DFS. Pressione enter para seguir para a heurística Hill Climbing.\n")

	busca.hillClimbing(s)
	input("Final da heurística Hill Climbing. Pressione enter para reiniciar.\n")

	os.system("clear")