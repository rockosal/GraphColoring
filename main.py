import read
import random
from CSP import doCSP
import sys

# if len(sys.argv) != 2:
#         print("Usage: %s input_file" % sys.argv[0])
#         sys.exit()

sys.setrecursionlimit(100000)


random.seed(12345678901)
nodes = read.read_problem("data/gc_4_1")
doCSP.backtrack_search(nodes)




