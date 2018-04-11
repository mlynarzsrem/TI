from collections import Counter

class Entity:
    def __init__(self,object,parent,child):
        self.object =object
        self.objectCount = 1
        self.parents =[]
        self.children = []
        if(parent is not None):
            self.parents.append(parent)
        if(child is not None):
            self.children.append(child)
    def getChildrenNumber(self):
        return len(self.children)
    def getParentsNumber(self):
        return len(self.parents)
    def getChildrenCounter(self):
        return Counter(self.children)
    def getParentsCounter(self):
        return Counter(self.parents)
    def incrementCounter(self):
        self.objectCount+=1
    def getCount(self):
        return self.objectCount
    def addChild(self,child):
        self.children.append(child)
    def addParent(self,parent):
        self.parents.append(parent)