"""
**************************************************************************************
This is the main archive of the Tower of Hanoi problem
**************************************************************************************
"""
#Larica is watching
#larica is testing

from models import Pin, State
from search import Search
import time
import os

s = State(initial_state_num_pieces=3)

while True:
	input("Oi, eu sou o potato. Aperte enter para continuar com as buscas!")

	busca = Search()

	busca.dfs(s, [])
	print("Muito bem! Cabou um DFS. Perae um minuto.")
	time.sleep(2)

	busca.hillClimbing(s)
	print("Very good! Finished a hill climbing. Wait there a minute.")
	time.sleep(2)

	#os.system("clear")

print("Numero de passos %d" % passos)