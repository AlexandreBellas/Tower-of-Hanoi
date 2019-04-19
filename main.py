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

s = State()
place_holder_father = State()
place_holder_father.addState(s)

N = 3
for i in range(N):
	s.pins[0].push(N-i-1)

s.addFather(place_holder_father)


while True:
	input("Oi, eu sou o potato. Aperte enter para continuar com as buscas!")

	busca = Search()

	busca.dfs(s, [])
	print("Muito bem! Cabou um DFS. Perae um minuto.")
	time.sleep(2)

	busca.hillClimbing(s)
	print("Very good! Finished a hill climbing. Wait there a minute.")
	time.sleep(2)

	os.system("clear")

print("Numero de passos %d" % passos)