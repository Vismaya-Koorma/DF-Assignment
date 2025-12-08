from typing import List, Any


def fifo(blocks,cache_size):


cache= []
increment=0
hits=0
miss=0

print(''' +++++ fifo Cache simulation+++++''')

for block in blocks:

    if block in cache:
        hits = hits+1


blocks= [3,5,1,2,5,7,0,3]
cache_size=3