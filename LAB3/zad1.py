import math
"""
file_wiki  = open('norm_wiki_sample.txt', 'r') 
wiki=file_wiki.read()
probs = {}
size_wiki=len(wiki)
"""
text="abcdefghijklmnopqrstuvwxyz 0123456789"
prob = 1/float(len(text))
print(prob)
entropy = 0.0
for i in range(len(text)):
	entropy+= prob*math.log2(prob)
print(entropy*-1)
""""
for a in text:
    probs[a] =float(wiki.count(a))/float(size_wiki)
	"""
