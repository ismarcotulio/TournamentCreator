from PyQt5 import QtWidgets, uic
from Core.Resources.Graph.Graph import *
from Core.Memory.Memory import *

def openParticipants():
	dlg2.show()

app = QtWidgets.QApplication([])
dlg = uic.loadUi("Core/GUI/main.ui")
dlg2 = uic.loadUi("Core/GUI/Participants.ui")



dlg.Add.clicked.connect(openParticipants)


TDAGraph = Graph()
memory = Memory("Core/Memory/mem.tsv")
dictGraph = memory.TSVtoDict()
memory.DicttoTDA(dictGraph, TDAGraph)
memory.exit()
print(" ")
TDAGraph.print()


dlg.show()
app.exec()