from collections import Counter
import pickle
class MySimpleEncoder:
    def init2(self,filename=None):
        self.text=None
        self.encoding =None
        if(filename!=None):
            with open(filename,"r") as f:
                self.text=f.read()
                self.letters = Counter(self.text)
                self.encoding = None

    def encode(self,text):
        letters = Counter(text)
        encoding = self.preapreEncodning(letters)
        score=pickle._dumps(encoding)+encoding['break']
        for c in text:
            score+=encoding[c]
        return score
    def decode(self,bytes):
        breakPoint = str.encode('111111')
        index =bytes.find(breakPoint)
        encoding = pickle.loads(bytes[0:index])
        toDeocde = bytes[index:]
        pass
    def load(self,filename):
        pass
    def save(self,filename):
        pass
    def preapreEncodning(self,letters):
        encoding = {}
        count =0
        encoding['break']=str.encode('111111')
        for l in letters.keys():
            binary_rep ="{0:b}".format(count)
            while(len(binary_rep)<6):
                binary_rep='0'+binary_rep
            encoding[l] = str.encode(binary_rep)
            count+=1
        return encoding

with open("norm_wiki_sample.txt","r") as f:
    text = f.read()
mse = MySimpleEncoder()
print(mse.encode("ala ma kota"))