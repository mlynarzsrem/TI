import random

random.seed()
wiki  = open('norm_hamlet.txt', 'r').read()
words=wiki.split(" ")
words= [w for w in words if len(w)>0] 

fulltext ='the '
lastWord ='the'
for i in range(40):
	indices = [i+1 for i, x in enumerate(words) if x == lastWord and i+1 <len(words)]
	toChoose  = indices[random.randint(0,len(indices)-1)]
	lastWord= words[toChoose]
	fulltext=fulltext+words[toChoose]+' '
print(fulltext)


