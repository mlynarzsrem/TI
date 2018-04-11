import math
from Entity import Entity
from collections import Counter
import threading
import os
class EntropyCalculator:
    def __init__(self,filename):
        with open(filename) as f:
            self.text = f.read()
            self.filename = str(filename).split('/')[-1].split('.')[0]
        self.words = self.text.split(" ")
        self.words = [w for w in self.words if len(w) > 0]
        self.wordsCounter = Counter(self.words)
        self.charsCounter = Counter([c for c in self.text])
        self.wordsEntropy=0
        self.charsEntropy =0
        self.wordsCondEntropies = []
        self.charsCondEntropies = []
        self.calculateEntropies()
        self.printScore()

    def printScore(self):
        text =""
        print("Nazwa pliku: "+self.filename)
        score = "Entropia słów wynosi: " + str(self.wordsEntropy)
        print(score)
        text += score+ "\n"
        score = "Entropia znaków wynosi: " + str(self.charsEntropy)
        print(score)
        text += score + "\n\n"
        for i in range(1, 6):
            score = "Entropia warunkowa wyrazów rzędu " + str(i) + " wynosi: " + str(self.wordsCondEntropies[i-1])
            print(score)
            text += score + "\n"
        text+="\n"
        for i in range(1, 6):
            score = "Entropia warunkowa znaków rzędu " + str(i) + " wynosi: " + str(self.charsCondEntropies[i - 1])
            print(score)
            text += score + "\n"
        scoreFileName = "results/"+self.filename+"_res.txt"
        file = open(scoreFileName,"w")
        file.write(text)
        file.close()
        print("Zapisano do pliku")

    def calculateWordsCondEntropy(self):
        for i in range(1,6):
            entropy = self.getCondEntropy(self.words,self.wordsCounter,i)
            self.wordsCondEntropies.append(entropy)
    def calculateCharsCondEntropy(self):
        for i in range(1,6):
            entropy = self.getCondEntropy(self.text, self.charsCounter,i)
            self.charsCondEntropies.append(entropy)
    def calculateEntropies(self):
        print("Przetwarzam: "+self.filename)
        print("Obliczam entopie słów.")
        self.wordsEntropy = self.getWordsEntropy(1)
        print("Obliczam entropie znaków.")
        self.charsEntropy = self.getCharsEntropy(1)
        print("Obliczam entropie warunkową słów")
        t1 =threading.Thread(target=self.calculateWordsCondEntropy)
        print("Obliczam entropie warunkową znaków")
        t2=threading.Thread(target=self.calculateCharsCondEntropy)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    def getCharsEntropy(self,eRange):
        entropy =0.0
        chars = [c for c in self.text]
        if(eRange>1):
            charsCombinationsList = self.getListOfN(chars,eRange)
        else:
            charsCombinationsList=chars
        charsCounter = Counter(charsCombinationsList)
        for cnt in charsCounter.values():
            P =cnt/float(len(charsCombinationsList))
            entropy += P*math.log2(P)
        return entropy*-1.0

    def getListOfN(self,list,N):
        newList = []
        for i in range(len(list)):
            if(i + N <len(list)):
                newList.append(tuple(list[i:i+N]))
        return newList
    def getWordsEntropy(self,eRange):
        entropy =0.0
        if(eRange>1):
            wordsCombinationsList = self.getListOfN(self.words,eRange)
        else:
            wordsCombinationsList = self.words.copy()
        counter = Counter(wordsCombinationsList)
        for cnt in counter.values():
            P =cnt/float(len(self.words))
            entropy += P*math.log2(P)
        return entropy*-1.0

    def getCondEntropy(self,text,counter,N):
        entropy =0.0
        result = {}
        allComb =0
        for i in range(len(text)):
            if(i + N <len(text)):
                allComb+=1
                element = text[i:i+N]
                if(isinstance(element,list)):
                    element = tuple(element)
                child = None
                if(i-1>=0):
                    child = text[i-1]
                if (element not in result):
                    result[element] = Entity(element,None,child)
                else:
                    result[element].incrementCounter()
                    if(child is not None):
                        result[element].addChild(child)
        for key in result.keys():
            entity = result[key]
            occNumber = entity.getCount()
            children = entity.getChildrenCounter()
            childrenNumber = entity.getChildrenNumber()
            childrenProbs =0.0
            PX = occNumber/float(allComb)
            for child in children.keys():
                PYX = children[child]/float(childrenNumber)
                childrenProbs+=PYX*math.log2(PYX)
            entropy+=childrenProbs*PX
        return entropy*-1.0

entropies = []
path = "files/tocompare"
for filename in os.listdir("files/tocompare"):
    ec = EntropyCalculator(path+"/"+filename)
    entropies.append(ec)
path = "files/tocheck"
for filename in os.listdir("files/tocheck"):
    ec = EntropyCalculator(path+"/"+filename)
    entropies.append(ec)

text="filename;EZ;ES;ES1;ES2;ES3;ES4;ES5;EZ1;EZ2;EZ3;EZ4;EZ5;\n"
for ent in entropies:
    text+=str(ent.filename)+";"+str(ent.charsEntropy)+";"+str(ent.wordsEntropy)+";"
    text+=str(ent.wordsCondEntropies[0])+";"+str(ent.wordsCondEntropies[1])+";"+str(ent.wordsCondEntropies[2])+";"+str(ent.wordsCondEntropies[3])+";"+str(ent.wordsCondEntropies[4])+";"
    text += str(ent.charsCondEntropies[0]) + ";" + str(ent.charsCondEntropies[1]) + ";" + str(ent.charsCondEntropies[2]) + ";" + str(ent.charsCondEntropies[3]) + ";" + str(ent.charsCondEntropies[4]) + ";\n"

scoreFileName = "results/globalresults.txt"
file = open(scoreFileName, "w")
file.write(text)
file.close()