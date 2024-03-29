from Core.Resources.Graph.Node import *

class LinkedList:

	def __init__(self):
		self.first = None

	def add(self,item):
		if self.first == None:
			self.first = Node(item)
		else:
			if self.AlreadyExist(item.name) == False:
				current = self.first
				while(current.next):
					current = current.next
				current.next = Node(item)
			else:
				return False

	def search(self, name):
		current = self.first
		while(current):
			if current.item.name == name:
				return current
			current = current.next
		return False		

	def AlreadyExist(self, name):
		current = self.first
		while(current):
			if current.item.name == name:
				return True
			current = current.next
		return False		




