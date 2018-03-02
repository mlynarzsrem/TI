import random
import numpy as np
fulltext=""
text="abcdefghijklmnopqrstuvwxyz "
print(len(text))
random.seed()
for i in range(100):
    fulltext=fulltext+text[random.randint(0,len(text)-1)]
#print(fulltext)
words=fulltext.split(" ")
words= [w for w in words if len(w)>0] 
lenghts = [len(w) for w in words]
print(np.mean(lenghts))

