import random

random.seed()
wiki  = open('norm_hamlet.txt', 'r').read()
words=wiki.split(" ")
words= [w for w in words if len(w)>0] 
fulltext =' '
for i in range(8):
	fulltext=fulltext+words[random.randint(0,len(words)-1)]+' '
print(fulltext)
