class Node:
	def __init__(self,element,isRoot=False):
		self.root = element
		self.isRoot =isRoot
		self.leftChild = None
		self.rightChild = None
	def addLeftChild(self,child):
		self.leftChild = child
	def addRightChild(self,child):
		self.rightChild = child
	def addAnyChild(self,child):
		if(self.leftChild is None):
			self.addLeftChild(child)
		else:
			self.addRightChild(child)