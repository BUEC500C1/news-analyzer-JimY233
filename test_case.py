# ============================================================
# For the result of AWS hosting, please check the screenshot on README.md
# This test_case.py just test the functions used in the NLP API
# ============================================================

import pytest

#search_nlp(search,text) #find the frequency of search in text
from NLP.nlp.nlp_search import *

#NLP_analyze(text)
from NLP.nlp.NLPAPI import *


def test_NLP1():
    text = 'Hello world!'
    sentiment = NLP_analyze(text)
    assert hasattr(sentiment,'score') == True

def test_NLP2():
    text = 'Hello world!'
    sentiment = NLP_analyze(text)
    assert hasattr(sentiment,'magnitude') == True
    
def test_NLP3():
    text = "The COVID 19 pandemic has altered every aspect of American life, from health and work to education and exercise. Over the long term, warns the American Psychological Association, the negative mental health effects of the covid will be serious and long-lasting."
    keyword = "covid"
    freq = nlp_search(keyword,text)
    assert freq == 2
    
if __name__ == '__main__':
    pytest.main()
