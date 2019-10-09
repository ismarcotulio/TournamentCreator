from Core.Resources.Graph.LinkedList import *
from Core.Resources.Graph.Vertex import *


class Graph:

	def __init__(self):
		self.vertices = LinkedList()

	def print(self):
		if self.vertices.first == None:
			print("No vertices")
		else:
			current = self.vertices.first
			while current:
				print("%s" %(current.item.name))
				currentEdge = current.item.edges.first
				while currentEdge:
					print("\t %s" %(currentEdge.item.name))
					currentEdge = currentEdge.next
				current = current.next

	def addVertex(self,name):
		self.vertices.add(Vertex(name))

	def addEdge(self, origin, destination):
		if self.vertices.first == None:
			return False
		else:
			vertex = self.vertices.search(origin)
			if vertex != False:
				edge = vertex.item.edges.AlreadyExist(destination)
				if edge == False:
					vertex.item.setEdge(Vertex(destination))
