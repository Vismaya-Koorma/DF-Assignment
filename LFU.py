def lfu_page_replacement():

    memory_size = int(input("Enter memory size: "))
    cache_size = int(input("Enter cache (frame) size: "))

    reference_string = list(map(int, input("Enter page reference string (space-separated): ").split()))

   
    cache = []
    frequency = {}
    page_faults = 0

    print("\nPage\tCache\t\tFault")

    for page in reference_string:
        fault = False

        if page not in cache:
            page_faults += 1
            fault = True

            
            if len(cache) < cache_size:
                cache.append(page)
                frequency[page] = 1
            else:
                
                lfu_page = min(cache, key=lambda x: frequency[x])
                
              
                cache.remove(lfu_page)
                del frequency[lfu_page]

                cache.append(page)
                frequency[page] = 1
        else:
           
            frequency[page] += 1

        print(f"{page}\t{cache}\t\t{'Yes' if fault else 'No'}")

    print("\nTotal Page Faults:", page_faults)


if __name__ == "__main__":
    lfu_page_replacement()