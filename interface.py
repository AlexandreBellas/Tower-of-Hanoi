import tkinter as tk

class Interface:
	def __init__(self):
		self.program_title = "Tower of Hanoi"
		self.pieces = 3
		
		while True:
			if(self.mainWindow() == 1):
				self.buscaProfundidade()
			else:
				self.buscaHillClimbing()

	def buscaProfundidade(self):
		print("teste1" + self.pieces)

	def buscaHillClimbing(self):
		print("teste2" + self.pieces)

	def mainWindow(self):

		def buttonDFS():
			self.pieces = NumPiecesEntryWidget.get()
			MainWindow.destroy()
			return 1

		def buttonHC():
			self.pieces = NumPiecesEntryWidget.get()
			MainWindow.destroy()
			return 2

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
								width=30)

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

		MainWindow.mainloop()


window = Interface()