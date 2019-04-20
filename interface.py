from tkinter import *
from models import Pin,State

class Interface(Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.program_title = "Tower of Hanoi"
		self.pieces = 3
		self.canvasHeight = 350
		self.canvasWidth = 700
		self.containters = [Frame(master), Frame(master), Frame(master), Frame(master)]
		for c in self.containters:
			c.pack(side=TOP)
		self.createWidgets()
		

	def buscaProfundidade(self):
		print("teste1" + self.pieces)

	def buscaHillClimbing(self):
		print("teste2" + self.pieces)

	def buttonDFS(self):
		self.pieces = self.NumPiecesEntryWidget.get()
		self.drawState()
		print("teste1" + self.pieces)

	def buttonHC(self):
		self.pieces = self.NumPiecesEntryWidget.get()
		self.drawState()
		print("teste2" + self.pieces)

	def createWidgets(self):
		#Titulo da Janela
		self.master.title("Tower of Hanoi")

		#Titulo
		LabelTitulo = Label(self.containters[0], text="Main Menu", font="Calibri 14 bold")

		#Subtitulo
		LabelSubtitulo = Label(self.containters[0], text="Choose your algorithm!", font="Calibri 12", height=5)

		#Canvas
		self.Canvas = Canvas(self.containters[1], bd=4, bg="white", height=self.canvasHeight, width=self.canvasWidth)

		#Titulo Entry widget
		LabelTituloEntryWidget = Label(self.containters[2], text="Enter here the number of pieces", font="Calibri 10")

		#Entry widget to choose the number of pieces
		self.NumPiecesEntryWidget = Entry(self.containters[2], width=30)

		#Botoes:
		ButtonDFS = Button(self.containters[3], text="Depth First Search - DFS", font="Calibri 10", command=self.buttonDFS, width=30, height=5)
		ButtonHC = Button(self.containters[3], text="Hill Climbing Heuristic", font="Calibri 10", command=self.buttonHC, width=30, height=5)

		#Packing
		LabelTitulo.pack(side=TOP)
		LabelSubtitulo.pack(side=BOTTOM)
		self.Canvas.pack(expand=True, fill=BOTH)
		LabelTituloEntryWidget.pack(side=TOP)
		self.NumPiecesEntryWidget.pack(side=BOTTOM)
		ButtonDFS.pack(side=LEFT, padx=50, pady=40)
		ButtonHC.pack(side=RIGHT, padx=50, pady=20)

	def drawState(self):
		self.Canvas.delete("all")
		#s = State()
		#state.copyState(s)
		self.Canvas.create_rectangle(self.canvasWidth/4 -5, self.canvasHeight - 300, self.canvasWidth/4 + 5, self.canvasHeight, fill="black")
		self.Canvas.create_rectangle(self.canvasWidth/2 - 5, self.canvasHeight - 300, self.canvasWidth/2 + 5, self.canvasHeight, fill="black")
		self.Canvas.create_rectangle(3*self.canvasWidth/4 -5, self.canvasHeight - 300, 3*self.canvasWidth/4 + 5, self.canvasHeight, fill="black")

root = Tk()
interface = Interface(master=root)
interface.mainloop()