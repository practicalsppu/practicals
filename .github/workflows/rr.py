def findWaitingTime(processes, n, bt, wt, quantum):
    rem_bt = [0] * n
    gantt = []
    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0

    while(1):
        done = True
        for i in range(n):
            if(rem_bt[i] > 0):
                done = False
                if(rem_bt[i] > quantum):
                    start_time = t
                    t += quantum
                    end_time = quantum
                    rem_bt[i] -= quantum
                    gantt.append((processes[i], start_time, end_time))
                
                else:
                    start_time = t
                    t = t + rem_bt[i]
                    end_time = t
                    wt[i] = t - bt[i]

                    rem_bt[i] = 0
                    gantt.append((processes[i], start_time, end_time))
        if done == True:
            break
    return gantt

def FindTurnAroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def drawGantt(gantt):
    for entry in gantt:
        process, start, end = entry
        print(f"| P{process} ", end = '')
    print("|")

    print("0", end='')

    for entry in gantt:
        process, start, end = entry
        print(f"   {end}", end=' ')
    print('\n')

def findAvgTime(processes, n, bt, quantum):
    wt = [0] * n
    tat = [0] * n

    gantt = findWaitingTime(processes, n, bt, wt, quantum)
    FindTurnAroundTime(processes, n, bt, wt, tat)
    
    print("Processes     Burst Time       Waiting Time        Turn Around Time")

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_tat += tat[i]
        total_wt += wt[i]
        print(f" {i+1}        {bt[i]}           {wt[i]}             {tat[i]}")
    
    print(f"Average Waiting Time: {total_wt / n}")
    print(f"Average Turn Around Time: {total_tat/n}")
    print("Gantt Chart: ")
    drawGantt(gantt)


if __name__ == "__main__":

    # Process id's
    proc = [1, 2, 3]
    n = 3

    # Burst time of all processes
    burst_time = [10, 5, 8]

    # Time quantum
    quantum = 2
    findAvgTime(proc, n, burst_time, quantum)

