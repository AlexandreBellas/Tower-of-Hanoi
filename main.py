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
from depthfirst import Dfs

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

	profundidade = Dfs(passos)
	profundidade.busca(s, [])
	
	print("Muito bem! Cabou um DFS. Perae um minuto.")
	time.sleep(2)

	os.system("clear")

print("Numero de passos %d" % passos)