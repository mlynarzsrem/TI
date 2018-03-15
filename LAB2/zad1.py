from itertools import groupby
import random
import operator
random.seed()
import collections
wiki  = open('norm_hamlet.txt', 'r').read()

words=wiki.split(" ")
words= [w for w in words if len(w)>0] 

counter=collections.Counter(words)
print(counter.most_common(3))
print(1110/float(len(wiki)))