import numpy as np
import collections
wiki  = open('norm_wiki_sample.txt', 'r').read() 
#Find all existing characters
chars=""
for c in wiki:
	if chars.find(c)==-1:
		chars=chars+c
chars = ''.join(sorted(chars))
print("Chars founded: {"+chars+"}\n")
#Count apperances of each character in the text 
apps = {}
for c in chars:
    apps[c] = wiki.count(c)
char1 = max(apps, key=lambda i: apps[i])
apps.pop(char1)
char2 = max(apps, key=lambda i: apps[i])
print('Najczesciej wystepuja: "'+char1+'" i "'+char2+'"')
dict1={}
for w in [char1,char2]:
    list1 = [wiki[pos + 1] for pos, char in enumerate(wiki) if char == w and (pos +1)<len(wiki)]
    counter = collections.Counter(list1)
    total = sum(counter.values(), 0.0)
    counter = {k: v / total for k, v in counter.items()}
    dict1[w]=counter
    print('Dla "'+w+'"\n')
    print(dict1[w])
    print("\n")