tasks = []
with open("tasks3.txt", "r") as file:
    for line in file:
        R_i, C_i, T_i, task_id = map(int, line.split())
        tasks.append((R_i, C_i, T_i, task_id))
tasks.sort()

time = 0
active_tasks = []
missed_tasks = []
S = 1

def calculate_laxity(task, current_time):
    R_i, C_i, T_i, task_id = task
    return T_i - C_i - current_time

while tasks or active_tasks:
    while tasks and tasks[0][0] <= time:
        active_tasks.append(tasks.pop(0))

    active_tasks = [
        task for task in active_tasks if calculate_laxity(task, time) >= 0
    ]
    missed_tasks.extend(
        [task[3] for task in active_tasks if calculate_laxity(task, time) < 0]
    )
    active_tasks = [
        task for task in active_tasks if calculate_laxity(task, time) >= 0
    ]

    if not active_tasks:
        if tasks:
            time = tasks[0][0]
        continue

    active_tasks.sort(key=lambda task: calculate_laxity(task, time))

    R_i, C_i, T_i, task_id = active_tasks.pop(0)

    next_time = time + C_i

    preempted = False
    while tasks and tasks[0][0] < next_time:
        new_task = tasks.pop(0)
        active_tasks.append(new_task)
        active_tasks.sort(key=lambda task: calculate_laxity(task, time))
        if calculate_laxity(new_task, time + S) < T_i - C_i - time:
            active_tasks.append((R_i, C_i, T_i, task_id))
            time += S
            preempted = True
            break

    if not preempted:
        time = next_time

for task in active_tasks:
    R_i, C_i, T_i, task_id = task
    if time + C_i <= T_i:
        time += C_i
    else:
        missed_tasks.append(task_id)

if missed_tasks:
    print("Задачи, которые опоздали:", missed_tasks)
else:
    print("Все задачи завершились вовремя!")
