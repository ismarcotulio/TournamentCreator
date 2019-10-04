from Resources.LinkedList import *
from Resources.Vertex import *


class Graph:

	def __init__(self):
		self.vertices = LinkedList()

	def addVertex(self,name):
		self.vertices.add(Vertex(name))

	def addEdge(self, origin, destination);
		if self.vertices.first == None:
			return False
		else:
			vertex = self.vertices.search(origin)
			if vertex != False:
				edge = vertex.item.edges.AlreadyExist(destination)
				if edge == False:
					vertex.item.setEdge(destination)