from Resources.LinkedList import *

class Vertex:

	def __init__(self,name):
		self.name = name
		self.edges = LinkedList()

	def setEdge(self, destination):
		self.edges.add(destination)