from tkinter import *


class Application:
	def __init__(self, master=None):
		#Lista de Containers
		self.containers = []

		#Titulo
		self.titulo = Label(self.primeiroContainer, text="Torre de Hanoi")
		self.titulo["font"] = ("Arial", "10", "bold")
		self.titulo.pack()

		#Botoes:
		self.dfs = Button(self.terceiroContainer)
		self.dfs["text"] = "Busca em Profundidade"
		self.dfs["font"] = ("Arial", "10")
		self.dfs.bind("<Button-1>", self.buscaProfundidade)
		self.dfs.pack(side=LEFT)

	def buscaProfundidade(self, event):
		print("teste")


root = Tk()
Application(root)
root.mainloop()