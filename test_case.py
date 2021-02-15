# ============================================================
# Defining your own testing here
# ============================================================

import securefileuploaderapi
import NLPanalysisapi
import newsingesterapi

import tracemalloc
import cProfile
import re

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

    
cProfile.run('re.compile("foo|bar")')

logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
