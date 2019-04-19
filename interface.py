from tkinter import *


class Application:
	def __init__(self, master=None):
		#Lista de Containers
		self.containers = [Frame(master), Frame(master), Frame(master), Frame(master)]
		for c in self.containers:
			c.pack()

		#Titulo
		self.titulo = Label(self.containers[0], text="Torre de Hanoi")
		self.titulo["font"] = ("Arial", "10", "bold")
		self.titulo.pack()

		#Botoes:
		self.dfs = Button(self.containers[2])
		self.dfs["text"] = "Busca em Profundidade"
		self.dfs["font"] = ("Arial", "10")
		self.dfs.bind("<Button-1>", self.buscaProfundidade)
		self.dfs.pack(side=LEFT)
		self.hc = Button(self.containers[2])
		self.hc["text"] = "Busca Hill Climbing"
		self.hc["font"] = ("Arial", "10")
		self.hc.bind("<Button-1>", self.buscaHillClimbing)
		self.hc.pack(side=RIGHT)

	def buscaProfundidade(self, event):
		print("teste1")

	def buscaHillClimbing(self, event):
		print("teste2")


root = Tk()
Application(root)
root.mainloop()