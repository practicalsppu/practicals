def get_processes(n):
    processes = []
    print("Enter burst Time")
    for i in range(n):
        burst_time = int(input(f"P{i+1}"))
        processes.append({"pid": i+1, "burst_time": burst_time})
    return processes

def calculate_waiting_time(processes):
    n = len(processes)
    processes.sort(key=lambda x : x['burst_time'])
    processes[0]["waiting_time"] = 0

    for i in range(1, n):
        processes[i]["waiting_time"] = processes[i-1]["waiting_time"] + processes[i-1]["burst_time"]


def calculate_turn_around_time(processes):
    for process in processes:
        process['turn_around_time'] = process['burst_time'] + process['waiting_time']

def calculate_avg_time(processes):
    total_waiting_time = sum(process['waiting_time'] for process in processes)
    total_tat = sum(process['turn_around_time'] for process in processes)
    avg_waiting_time = total_waiting_time / len(processes)
    avg_tat = total_tat / len(processes)
    return avg_waiting_time, avg_tat

def show(processes, avg_waiting_time, avg_tat):
    print("P    \tBT    \tWT    \tTAT")
    for process in processes:
        print(f"P{process['pid']}    \t{process['burst_time']}    \t{process['waiting_time']}    \t{process['turn_around_time']}")
    print(f"Average Waiting Time is: {avg_waiting_time}")
    print(f"Average Turn Around Time: {avg_tat}")

def main():
    n = int(input("Enter number of processes: "))
    processes = get_processes(n)
    calculate_waiting_time(processes)
    calculate_turn_around_time(processes)
    avg_wt, avg_tat = calculate_avg_time(processes)
    show(processes, avg_wt, avg_tat)

if __name__ == '__main__':
    main()