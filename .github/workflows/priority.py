def findWaitingTime(processes, n, wt):
    wt[0] = 0
    for i in range(1,n):
        wt[i] = processes[i-1][1] + wt[i-1]

def findTurnAroundTime(processes, n, wt, tat):
    for i in range(n):
        tat[i] = processes[i][1] + wt[i]


def findAvgTime(processes, n):
    wt = [0]*n
    tat = [0] * n
    total_wt = 0
    total_tat = 0

    findWaitingTime(processes, n, wt)
    findTurnAroundTime(processes, n, wt, tat)



def priorityScheduling(proc, n):
    proc = sorted(proc, key=lambda proc : proc[2], reverse=True)

    print("Order in which process gets executed")
    for i in proc:
        print(i[0], end='')
    findAvgTime(proc, n)


if __name__ == "__main__":
    proc = [[1,10,1],[2,5,0], [3,8,1]]
    n = 3
    priorityScheduling(proc, n)