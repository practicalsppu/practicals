from queue import Queue

def FIFO(pages, n, capacity):
    hits = 0
    page_faults = 0
    allocation_seq = []
    s = set()
    indexes = Queue()

    for i in range(n):
        if len(s) < capacity:
            if pages[i] not in s:
                page_faults += 1
                s.add(pages[i])
                indexes.put(pages[i])
            else:
                hits += 1
        else:
            if pages[i] not in s:
                page_faults += 1
                val = indexes.get()
                s.remove(val)
                s.add(pages[i])
                indexes.put(pages[i])
            else:
                hits += 1
        
        allocation_seq.append(list(s))
    
    misses = page_faults
    miss_ratio =  misses / n
    hit_ratio = hits / n
    print("Allocation Sequence is as follows:")
    for step, frame in enumerate(allocation_seq):
        print(f"Step {step+1} : {frame}")
    
    print(f"Total page faults: {page_faults}")
    print(f"Total Hits: {hits}")
    print(f"Hit Ratio : {hit_ratio}")
    print(f"Miss Ratio : {miss_ratio}")

if __name__ == '__main__':
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    n = len(pages)
    capacity = 4
    FIFO(pages, n, capacity)