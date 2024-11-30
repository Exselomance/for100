tasks = []
with open("tasks2.txt", "r") as file:
    for line in file:
        R_i, C_i, T_i, task_id = map(int, line.split())
        tasks.append((R_i, C_i, T_i, task_id))

tasks.sort()

time = 0
queue = []
missed_tasks = []

for task in tasks:
    # для каждой задачи
    R_i, C_i, T_i, task_id = task

    while queue and time < R_i:
        min_task = queue[0]
        for item in queue:
            if item[1] < min_task[1]:
                min_task = item
        queue.remove(min_task)

        C_curr, T_curr, task_curr_id = min_task

        if time + C_curr <= T_curr:
            time += C_curr
        else:
            missed_tasks.append(task_curr_id)
            time = T_curr

    queue.append((C_i, T_i, task_id))
    time = max(time, R_i)

while queue:
    min_task = queue[0]
    for item in queue:
        if item[1] < min_task[1]:
            min_task = item
    queue.remove(min_task)

    C_curr, T_curr, task_curr_id = min_task

    if time + C_curr <= T_curr:
        time += C_curr
    else:
        missed_tasks.append(task_curr_id)
        time = T_curr

if missed_tasks:
    print("Задачи, которые опоздали:", missed_tasks)
else:
    print("Все задачи завершились вовремя!")
