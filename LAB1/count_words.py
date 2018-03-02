import random
random.seed()
file_wiki  = open('norm_wiki_sample.txt', 'r') 
wiki=file_wiki.read()
dict1={}
probs = {}
size_wiki=len(wiki)
text="abcdefghijklmnopqrstuvwxyz "
for a in text:
    dict1[a]= wiki.count(a)
    probs[a] =float(wiki.count(a))/float(size_wiki)
text_probs=""
words_count= 10000
for a in text:
    text_probs=text_probs + a*int(probs[a]*words_count)
fulltext=""
for i in range(100):
    fulltext=fulltext+text_probs[random.randint(0,len(text)-1)]   
