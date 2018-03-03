import numpy as np
import random
random.seed()
wiki  = open('norm_wiki_sample.txt', 'r').read() 
chars=""
for c in wiki:
	if chars.find(c)==-1:
		chars=chars+c
chars = ''.join(sorted(chars))
print("Chars founded: {"+chars+"}\n")
dict1={}
for w in chars:
	dict1[w] = [wiki[pos + 1] for pos, char in enumerate(wiki) if char == w and (pos +1)<len(wiki)]
print("Creating started!\n")
finalText="Probability"

for i in range(5000):
	charsAfter = dict1[finalText[-1]]
	finalText =  finalText + charsAfter[random.randint(0,len(charsAfter)-1)]
print(finalText)	