from collections import defaultdict

def pageFaults(pages, n, capacity):
    frames = []
    allocation_seq = []
    page_faults = 0
    hits = 0
    page_freq = defaultdict(int)

    for page in pages:
        if page in frames:
            hits += 1
            page_freq[page] += 1
        else:
            page_faults += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                mfu_page = max(frames, key = lambda x : page_freq[x])
                frames.remove(mfu_page)
                frames.append(page)
            page_freq[page] = 1
        
        allocation_seq.append(list(frames))
    miss_ratio = page_faults / n
    hit_ratio = hits / n

    
    print("Page Allocation Sequence (frames at each step):")
    for step, frame in enumerate(allocation_seq):
        print(f"Step {step + 1}: {frame}")

    
    print(f"\nTotal Page Faults (Misses): {page_faults}")
    print(f"Cache Miss Ratio: {miss_ratio:.2f}")
    print(f"Cache Hit Ratio: {hit_ratio:.2f}")

    return page_faults


if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    n = len(pages)
    capacity = 4
    pageFaults(pages, n, capacity)