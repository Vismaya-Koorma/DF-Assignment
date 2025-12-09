from typing import List, Any


def fifo(blocks,cache_size):
    cache = []
    increment = 0
    hits = 0
    miss = 0
    print(''' +++++ fifo Cache simulation+++++''')
    print("\n")
    for block in blocks:

        if block in cache:
            hits = hits+1
            print(f"Block {block}: Hit   cache:{cache}")

        else:
            miss = miss+1

            if len(cache) < cache_size:
                cache.append(block)
            else:
                cache[increment] = block
                increment=(increment +1)% cache_size

            print(f"block {block} : MISS Cache : {cache}")

    hit_ratio = hits / len(blocks)

    print("--- FINAL RESULT ---")
    print("\n")
    print("Total Hits   :", hits)
    print("Total Misses :", miss)
    print(" The Hit Ratio    :", round(hit_ratio, 2))


blocks=[3,5,1,2,5,7,0,3]
cache_size=3
fifo(blocks, cache_size)