class Memory:

	def __init__(self, filename):
		self.f = open(filename,"r")
		self.contentF = self.f.read()
		self.content = self.contentF.strip()
		self.dict = {}
		self.dictString = ""

	def TSVtoDict(self):
		rows = self.content.split("\n")
		self.dictString = "{%s" %(self.TSVtoDictInner(rows))
		self.dict = eval(self.dictString)
		return self.dict

	def TSVtoDictInner(self, rows, contador = 0,nextTabs = None):
		columns = rows[contador].split("\t")
		currentTabs = len(columns) - 1
		value = "%s" %(columns[len(columns)-1])
		value = value.split(":")

		if len(rows)-1 != contador:
			nextColumns = rows[contador+1].split("\t")
			nextTabs = len(nextColumns)-1

		print(" ")
		print(value)
		print("tabs actuales, %s"%currentTabs)
		print("tabs siguientes, %s"%nextTabs)


		if len(rows)-1 != contador:
			if currentTabs == 0:
				return '"%s":[{ %s' %(value[0],self.TSVtoDictInner(rows,contador+1))
			elif currentTabs == 1:
				return '"%s":{%s'%(value[0],self.TSVtoDictInner(rows,contador+1))
			elif currentTabs == 2 and nextTabs == 2:
				return '"%s":"%s",%s' %(value[0],value[1],self.TSVtoDictInner(rows,contador+1))
			elif currentTabs == 2 and nextTabs == 1:
				return '"%s":"%s",},%s' %(value[0],value[1],self.TSVtoDictInner(rows,contador+1))
			elif currentTabs == 2 and nextTabs == 0:
				return '"%s":"%s"} }],%s' %(value[0],value[1],self.TSVtoDictInner(rows,contador+1))
		else:
			if currentTabs == 0:
				return '"%s":"%s"}' %(value[0],value[1])
			elif currentTabs == 1:
				return '"%s":"%s" }]}' %(value[0],value[1])
			elif currentTabs == 2:
				return '"%s":"%s" } }]}' %(value[0],value[1])


	def DicttoTDA(self, graphDict, graphTDA):
		for k,v in graphDict.items():
			graphTDA.addVertex(k)
			for k2,v2 in v[0].items():
				graphTDA.addEdge(k,k2)

	def exit(self):
		self.f.close()


