import tkinter as tk
from tkinter import messagebox as msgb
from models import State, Pin
from search import Search
import time
import threading as thr

class Interface:
	def __init__(self):
		self.program_title = "Tower of Hanoi"
		self.pieces = 3

		self.LabelDFS = 0
		self.LabelHC = 0

		self.canvasHeight = 350
		self.canvasWidth = 700
		
		while True:
			self.mainWindow()
				

	def buscaProfundidade(self):

		def executeDFS():
			busca.dfs(s, [], self)

		def jumpToEnd():
			busca.tempo_espera = 0

		def on_closing():
			jumpToEnd()
			time.sleep(1)
			DFSWindow.destroy()

		#print("teste1" + self.pieces)
		DFSWindow = tk.Tk()
		DFSWindow.title("Depth First Search algorithm")

		#Label
		self.LabelDFS = tk.Label(DFSWindow,
							text="",
							font="Calibri 14")

		#Canvas
		self.Canvas = tk.Canvas(DFSWindow, 
							bg="white", 
							height=self.canvasHeight, 
							width=self.canvasWidth)

		#Button for jumping to the end
		ButtonDFS = tk.Button(DFSWindow,
							text="Jump to the end!",
							font="Calibri 10",
							command=jumpToEnd,
							width="30",
							height="3")

		#Packing
		#self.LabelDFS.pack(side=tk.TOP, padx=100, pady=10)
		self.Canvas.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
		ButtonDFS.pack(side=tk.BOTTOM, pady=30)

		#Setup of the search
		s = State(initial_state_num_pieces=self.pieces)
		busca = Search()

		t = thr.Thread(target=executeDFS)
		t.start()

		DFSWindow.protocol("WM_DELETE_WINDOW", on_closing)

		DFSWindow.mainloop()

	def buscaHillClimbing(self):
		
		def executeHillClimbing():
			busca.hillClimbing(s, self)

		def jumpToEnd():
			busca.tempo_espera=False

		def on_closing():
			jumpToEnd()
			time.sleep(1)
			HCWindow.destroy()

		#print("teste2" + self.pieces)
		HCWindow = tk.Tk()
		HCWindow.title("Hill Climbing heuristic")

		#Label
		self.LabelHC = tk.Label(HCWindow,
							text="",
							font="Calibri 14")

		#Canvas
		self.Canvas = tk.Canvas(HCWindow, 
							bg="white", 
							height=self.canvasHeight, 
							width=self.canvasWidth)

		#Button for jumping to the end
		ButtonHC = tk.Button(HCWindow,
							text="Jump to the end!",
							font="Calibri 10",
							command=jumpToEnd,
							width="30",
							height="3")

		#Packing
		self.LabelHC.pack(side=tk.TOP, padx=100, pady=10)
		self.Canvas.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
		ButtonHC.pack(side=tk.BOTTOM, pady=30)

		#Setup of the search
		s = State(initial_state_num_pieces=self.pieces)
		busca = Search()

		t = thr.Thread(target=executeHillClimbing)
		t.start()

		HCWindow.protocol("WM_DELETE_WINDOW", on_closing)

		HCWindow.mainloop()

	def drawState(self, state=None, passos=None):
		#Apaga o Canvas
		self.Canvas.delete("all")

		s = State()
		state.copyState(s)
		pinAux = [Pin() for j in range(3)]
		for j in range(3):
			for i in range(0, state.pins[j].size()):
				block = state.pins[j].pop()
				pinAux[j].push(block)

		#Define o tamanho dos pinos
		pinWidth = 10
		pinHeight = 300

		#Define o tamanho do menor bloco
		minBlockWidth = self.canvasWidth/6*self.pieces
		minBlockHeight = pinHeight/self.pieces

		#Criando os Pinos
		self.Canvas.create_rectangle(self.canvasWidth/4 -pinWidth/2, 
								self.canvasHeight -pinHeight, 
								self.canvasWidth/4 +pinWidth/2, 
								self.canvasHeight, 
								fill="black")
		self.Canvas.create_rectangle(self.canvasWidth/2 -pinWidth/2, 
								self.canvasHeight -pinHeight, 
								self.canvasWidth/2 +pinWidth/2, 
								self.canvasHeight, 
								fill="black")
		self.Canvas.create_rectangle(3*self.canvasWidth/4 -pinWidth/2, 
								self.canvasHeight -pinHeight, 
								3*self.canvasWidth/4 +pinWidth/2, 
								self.canvasHeight, 
								fill="black")

		for j in range(len(pinAux)):
			towerHeight = 0
			for i in range(0, pinAux[j].size()):
				block = pinAux[j].pop()
				blockX0 = ((j+1)*self.canvasWidth/4) - minBlockWidth*(block+1)/2
				blockY0 = self.canvasHeight - (towerHeight + minBlockHeight*(block+1))
				blockX1 = ((j+1)*self.canvasWidth/4) + minBlockWidth*(block+1)/2 + 1
				blockY1 = self.canvasHeight - towerHeight
				towerHeight += minBlockHeight*(block+1) + 1
				self.Canvas.create_rectangle(blockX0, blockY0, blockX1, blockY1, fill="grey")

	def mainWindow(self):

		def verifyEntryWidgetContent():
			entry = NumPiecesEntryWidget.get()
			if entry == "":
				msgb.showerror("Error", "Don't let the text box empty!")
				return False
			else:
				try:
					entry = int(entry)
					return True
				except ValueError:
					msgb.showerror("Error", "Put a valid number.")
					return False

		def buttonDFS():
			if verifyEntryWidgetContent():
				self.pieces = int(NumPiecesEntryWidget.get())
				MainWindow.destroy()
				self.buscaProfundidade()

		def buttonHC():
			if verifyEntryWidgetContent():
				self.pieces = int(NumPiecesEntryWidget.get())
				MainWindow.destroy()
				self.buscaHillClimbing()

		def on_closing():
			if msgb.askokcancel("Quit", "Do you want to quit?"):
				quit()


		MainWindow = tk.Tk()
		MainWindow.title("Tower of Hanoi")

		#Titulo
		LabelTitulo = tk.Label(MainWindow,
								text="Main Menu",
								font="Calibri 14 bold")
		

		#Subtitulo
		LabelSubtitulo = tk.Label(MainWindow,
									text="Choose your algorithm!",
									font="Calibri 12",
									height=5)

		#Titulo Entry widget
		LabelTituloEntryWidget = tk.Label(MainWindow,
									text="Enter here the number of pieces",
									font="Calibri 10")

		#Entry widget to choose the number of pieces
		NumPiecesEntryWidget = tk.Entry(MainWindow,
								width=30,
								justify=tk.RIGHT)
		NumPiecesEntryWidget.insert(1, "3")

		#Botoes:
		ButtonDFS = tk.Button(MainWindow,
								text="Depth First Search - DFS",
								font="Calibri 10",
								command=buttonDFS,
								width=30,
								height=5)

		ButtonHC = tk.Button(MainWindow,
								text="Hill Climbing heuristic",
								font="Calibri 10",
								command=buttonHC,
								width=30,
								height=5)

		#Packing
		LabelTitulo.pack(side=tk.TOP)
		LabelSubtitulo.pack(side=tk.TOP)
		LabelTituloEntryWidget.pack(side=tk.TOP)
		NumPiecesEntryWidget.pack(side=tk.TOP)
		ButtonDFS.pack(side=tk.LEFT, padx=50, pady=40)
		ButtonHC.pack(side=tk.RIGHT, padx=50, pady=20)

		#'X' click handler
		MainWindow.protocol("WM_DELETE_WINDOW", on_closing)

		MainWindow.mainloop()