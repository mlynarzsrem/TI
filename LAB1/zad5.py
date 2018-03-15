import re
import random
import numpy as np
random.seed()
wiki  = open('norm_wiki_sample.txt', 'r').read() 

def getNextChars(s):
    return [wiki[m.end()] for m in re.finditer(s, wiki) if (m.end() + 1)<len(wiki) ]

def generateWords(cnt,number):    
    finalText="Probability"
    print(finalText, end='', flush=True)
    for i in range(number):
        charsAfter = getNextChars(finalText[-1*(cnt):])
        #print(charsAfter)
        #print('\n')
        #print(finalText[-1*(cnt):]+'\n')
        tmpCnt= cnt
        while(len(charsAfter)==0):
            tmpCnt=tmpCnt-1
            charsAfter = getNextChars(finalText[-1*(tmpCnt):])
        newChar = charsAfter[random.randint(0,len(charsAfter)-1)]
        finalText =  finalText + newChar
        print(newChar, end='', flush=True)	
    return finalText

for x in [5] :   
    text = generateWords(x,100)
    print('\n Rzad: '+str(x))
    words=text.split(" ")
    words= [w for w in words if len(w)>0] 
    lenghts = [len(w) for w in words]
    print("\n Srednia: ")
    print(np.mean(lenghts))
