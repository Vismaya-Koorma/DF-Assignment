# Direct Mapping Page Replacement Algorithm

def direct_mapping(page_frames, page_sequence):
    n = len(page_frames)
    memory = [-1] * n  # Initialize memory frames with -1 (empty)
    hits = 0
    misses = 0

    for page in page_sequence:
        index = page % n  # Direct mapping index
        if memory[index] == page:
            hits += 1
            print(f"Page {page} already in memory at frame {index} -> HIT")
        else:
            misses += 1
            print(f"Page {page} loaded into frame {index} -> MISS")
            memory[index] = page
        
        print(f"Memory State: {memory}\n")
    
    print(f"Total Hits: {hits}")
    print(f"Total Misses: {misses}")

# Example Usage
frames = int(input("Enter number of memory frames: "))
pages = list(map(int, input("Enter page sequence separated by spaces: ").split()))

direct_mapping([0]*frames, pages)
