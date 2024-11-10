def pageFaults(pages, n, capacity):
    hits = 0
    page_faults = 0
    frames = []
    allocation_seq = []
    
    for i in range(n):
        page = pages[i]
        if page in frames:
            hits += 1
        else:
            page_faults += 1
            if len(frames) < capacity:
                frames.append(page)
            
            else:
                farthest = i+1
                page_to_rep = -1
                index_to_rep = -1

                for j in range(len(frames)):
                    if frames[j] not in pages[i+1:]:
                        page_to_rep = frames[j]
                        index_to_rep = j
                        break
                    else:
                        farthest = pages[i+1:].index(frames[j]) + i + 1
                        page_to_rep = frames[j]
                        index_to_rep = j
                
                frames[index_to_rep] = page
        allocation_seq.append(list(frames))

    hit_ratio = hits / n
    miss_ratio = page_faults / n

    for step, frame in enumerate(allocation_seq):
        print(f"Step {step + 1} : {frame}")
    
    print(f"Total Page Faults {page_faults}")
    
    print(f"Total Hits: {hits}")
    print(f"Misses: {page_faults}")
    print(f"Hit Ratio: {hit_ratio}")
    print(f"Miss Ratio: {miss_ratio}")
    print("Entry at each step will be:")
if __name__ == '__main__':
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    n = len(pages)
    capacity = 4
    pageFaults(pages, n, capacity)