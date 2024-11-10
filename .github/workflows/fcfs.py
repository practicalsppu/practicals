def findWaitingTime(processes, n, bt, wt):
    wt[0] = 0
    for i in range(1,n):
        wt[i] = bt[i-1] + wt[i-1]

def findTurnAroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = wt[i] + bt[i]

def drawGantt(processes, n, bt):
    current_time = 0
    gantt_chart = ""
    for i in range(n):
        start_time = current_time
        end_time = start_time + bt[i]
        gantt_chart += f"| P{processes[i]} {end_time - start_time}"
    gantt_chart += '|'
    print(gantt_chart)

def findAvgTime(processes, n, bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0

    findWaitingTime(processes, n, bt, wt)
    findTurnAroundTime(processes, n, bt, wt, tat)
    print("Processes  Burst Time  Waiting Time  Turn Around Time")
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f"{processes[i]} \t {bt[i]} \t  {wt[i]} \t\t {tat[i]}")
    print(f"Average Waiting Time: {total_wt/n}")
    print(f"Average Turn Around Time: {total_tat/n}")
    drawGantt(processes, n, bt)


if __name__ == '__main__':
    processes = [1,2,3]
    bt = [10,5,8]
    n = 3

    findAvgTime(processes, n, bt)
    

    