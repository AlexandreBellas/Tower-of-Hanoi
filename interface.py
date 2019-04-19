from tkinter import *


class Application:
	def __init__(self, master=None):
		#Primeiro Container
		self.primeiroContainer = Frame(master)
		#self.primeiroContainer["pady"] = 10
		self.primeiroContainer.pack()

		#Segundo Container
		self.segundoContainer = Frame(master)
		#self.segundoContainer["padx"] = 20
		self.segundoContainer.pack()

		#terceiro container
		self.terceiroContainer = Frame(master)
		#self.terceiroContainer["pady"] = 20
		self.terceiroContainer.pack()

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