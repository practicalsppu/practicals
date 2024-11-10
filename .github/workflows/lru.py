def page_faults(pages, n, capacity):
    frame = []
    pagefault = 0
    hits = 0
    allocation_seq = []

    for page in pages:
        if page in frame:
            frame.remove(page)
            frame.append(page)
            hits += 1
        else:
            pagefault += 1
            if len(frame)<capacity:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
            
        allocation_seq.append(list(frame))

    miss = pagefault
    miss_ratio = miss / n
    hit_ratio  = hits / n
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
    page_faults(pages, n, capacity)