from collections import Counter
import pickle
from bitarray import bitarray
import filecmp
import numpy as np
class MySimpleEncoder:
    def convertTo8Bits(self,byte):
        binary_rep = "{0:b}".format(byte)
        while (len(binary_rep) < 8):
            binary_rep = '0' + binary_rep
        return binary_rep
#return self.encoding[c]
    def encode(self,text):
        letters = Counter(text)
        encoding = self.preapreEncodning(letters)
        encodingBytes=pickle._dumps(encoding)+bitarray('111111').tobytes()
        encoded = ''.join(list(map(lambda x:encoding[x],text)))
        encoded = bitarray(encoded).tobytes()
        return encodingBytes+encoded
    def decode(self,bytes):
        breakPoint =  bitarray('111111').tobytes()
        index =bytes.find(breakPoint)
        encoding = pickle.loads(bytes[0:index])
        encoding = {v: k for k, v in encoding.items()}
        bytes= bytes[index+1:len(bytes)]
        bits=''.join(list(map(self.convertTo8Bits,bytes)))
        bits =bits[0:-2]
        byteList = [bits[x:x+6] for x in range(0, len(bits),6)]
        decoded = ''.join(list(map(lambda x: encoding[x], byteList)))
        return decoded
    def load(self,filename):
        with open(filename, "rb") as f:
            bytes =f.read()
            decoded = self.decode(bytes)
            with open("decoded.txt","w") as w:
                w.write(decoded)
    def save(self,filename):
        with open(filename,'r') as f:
            text = f.read()
            encoded =self.encode(text)
            with open("encode.dat","wb") as w:
                w.write(encoded)
    def preapreEncodning(self,letters):
        encoding = {}
        count =0
        for l in letters.keys():
            binary_rep ="{0:b}".format(count)
            while(len(binary_rep)<6):
                binary_rep='0'+binary_rep
            encoding[l] =binary_rep
            count+=1
        return encoding

file ="norm_wiki_sample.txt"
mse = MySimpleEncoder()
mse.save(file)
mse.load('encode.dat')
print(filecmp.cmp(file, 'decoded.txt'))