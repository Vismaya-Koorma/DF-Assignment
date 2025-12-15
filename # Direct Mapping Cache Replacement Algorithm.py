# Direct Mapping Cache Replacement Algorithm

cache_size = int(input("Enter cache size: "))
cache = [-1] * cache_size

n = int(input("Enter number of memory blocks: "))
blocks = list(map(int, input("Enter memory block sequence: ").split()))

hit = 0
miss = 0

for block in blocks:
    index = block % cache_size

    if cache[index] == block:
        print(f"Block {block} → Cache HIT")
        hit += 1
    else:
        print(f"Block {block} → Cache MISS (placed in line {index})")
        cache[index] = block
        miss += 1

print("\nFinal Cache State:", cache)
print("Total Hits :", hit)
print("Total Miss:", miss)
