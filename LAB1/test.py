import numpy as np
import random
random.seed()
file_wiki  = open('norm_wiki_sample.txt', 'r') 
wiki=file_wiki.read()
fulltext=""
for i in range(3100):
    fulltext=fulltext+wiki[random.randint(0,len(wiki)-1)]
words=fulltext.split(" ")
words= [w for w in words if len(w)>0] 
lenghts = [len(w) for w in words]
print(np.mean(lenghts))   
