def firstfit(blockSize, m, processSize, n):
    allocation = [-1]*n

    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j

                blockSize[j] -=  processSize[i]

                break
        
    print("Process No.    Process Size     Block No.")
    for i in range(n):
        print(f"{i+1}      \t\t{processSize[i]}", end='      \t')
        if allocation[i] != -1:
            print(allocation[i]+1)
        else:
            print("Not Allocated")

if __name__ == "__main__":
    blockSize = [100, 500, 200, 300, 600]
    processSize = [212, 417, 112, 426]
    m = len(blockSize)
    n = len(processSize)
    firstfit(blockSize, m, processSize, n)