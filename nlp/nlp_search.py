import nltk
from nltk.probability import FreqDist
import logging

def convert(lis): 
    return "".join('%s' %i for i in lis) 

def search_nlp(search,text):
    content = ""
    if isinstance(text,str):
        content = text
    elif isinstance(text,tuple) or isinstance(text,list):
        content = convert(text)
    word = nltk.word_tokenize(content)
    freqdist = FreqDist(word)
    if search in freqdist.keys():
        dist = freqdist[search]
        return dist
    else:
        return 0