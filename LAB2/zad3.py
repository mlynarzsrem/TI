import random

random.seed()
wiki  = open('norm_wiki_sample.txt', 'r').read()
words=wiki.split(" ")
words= [w for w in words if len(w)>0] 

def first_degree():
    fulltext ='the '
    lastWord ='the'
    for i in range(40):
        indices = [i+1 for i, x in enumerate(words) if x == lastWord and i+1 <len(words)]
        toChoose  = indices[random.randint(0,len(indices)-1)]
        lastWord= words[toChoose]
        fulltext=fulltext+words[toChoose]+' '
    print(fulltext)

def second_degree(listOfWords):
    searched = listOfWords
    if(len(searched)<2):
        indices = [i+1 for i, x in enumerate(words) if x == searched[0] and i+1 <len(words)]
        toChoose = random.randint(0,len(words)-1)
        searched.append(words[toChoose])
    print(searched)
    fulltext =searched[0] +' '+searched[1]+' '
    for i in range(50):
        indices = [i+2 for i, x in enumerate(words) if x == searched[0] and words[i+1]==searched[1] and i+2 <len(words)]
        if(len(indices)==0):
            toChoose = random.randint(0,len(words)-1)
        else:
            toChoose  = indices[random.randint(0,len(indices)-1)]
        fulltext=fulltext+words[toChoose]+' '
        searched.append(words[toChoose])
        searched.pop(0)
    print(fulltext)

second_degree(['probability']) 
