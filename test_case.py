# ============================================================
# Defining your own testing here
# ============================================================

from SecureFileUploader.FileIngester import *
from NewsIngester.newsingester import *
from NLP_Analysis.nlpanalysis import *

import tracemalloc
import cProfile

import logging

def test_case():
  assert 1 == 1
  

tracemalloc.start()

# ... run your application ...
test_case()

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)

    
cProfile.run("20+10")

logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
