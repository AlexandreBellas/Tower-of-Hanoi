from tkinter import *

class Interface(Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.program_title = "Tower of Hanoi"
		self.pieces = 3
		self.containters = [Frame(master), Frame(master), Frame(master)]
		for c in self.containters:
			c.pack()
		self.createWidgets()
		

	def buscaProfundidade(self):
		print("teste1" + self.pieces)

	def buscaHillClimbing(self):
		print("teste2" + self.pieces)

	def buttonDFS(self):
		self.pieces = self.NumPiecesEntryWidget.get()
		print("teste1" + self.pieces)

	def buttonHC(self):
		self.pieces = self.NumPiecesEntryWidget.get()
		print("teste2" + self.pieces)

	def createWidgets(self):
		#Titulo da Janela
		self.master.title("Tower of Hanoi")

		#Titulo
		LabelTitulo = Label(self.containters[0], text="Main Menu", font="Calibri 14 bold")

		#Subtitulo
		LabelSubtitulo = Label(self.containters[0], text="Choose your algorithm!", font="Calibri 12", height=5)

		#Titulo Entry widget
		LabelTituloEntryWidget = Label(self.containters[1], text="Enter here the number of pieces", font="Calibri 10")

		#Entry widget to choose the number of pieces
		self.NumPiecesEntryWidget = Entry(self.containters[1], width=30)

		#Botoes:
		ButtonDFS = Button(self.containters[2], text="Depth First Search - DFS", font="Calibri 10", command=self.buttonDFS, width=30, height=5)
		ButtonHC = Button(self.containters[2], text="Hill Climbing Heuristic", font="Calibri 10", command=self.buttonHC, width=30, height=5)

		#Packing
		LabelTitulo.pack(side=TOP)
		LabelSubtitulo.pack(side=BOTTOM)
		LabelTituloEntryWidget.pack(side=TOP)
		self.NumPiecesEntryWidget.pack(side=BOTTOM)
		ButtonDFS.pack(side=LEFT, padx=50, pady=40)
		ButtonHC.pack(side=RIGHT, padx=50, pady=20)

root = Tk()
interface = Interface(master=root)
interface.mainloop()