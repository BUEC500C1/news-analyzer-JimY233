# ============================================================
# Defining your own testing here
# ============================================================

import securefileuploaderapi
import NLPanalysisapi
import newsingesterapi

import tracemalloc

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

