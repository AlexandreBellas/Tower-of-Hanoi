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

while True:
	num_pieces = int(input("Número de peças: "))

	s = State(initial_state_num_pieces=num_pieces)

	input("Oi, eu sou o potato. Aperte enter para continuar com as buscas!")

	busca = Search()

	busca.dfs(s, [])
	input("Muito bem! Cabou um DFS. Enter pro Hill Climbing.")

	busca.hillClimbing(s)
	input("Very good! Finished a hill climbing. Enter to restart.")

	os.system("clear")

print("Numero de passos %d" % passos)