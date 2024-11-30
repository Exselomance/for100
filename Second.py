tasks = [
    (0, 2, 5, 1),
    (2, 3, 8, 2),
    (4, 1, 6, 3),
    (6, 4, 10, 4),
    (7, 2, 9, 5),
]

tasks.sort()

time = 0
queue = []
missed_tasks = []

for task in tasks:
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
