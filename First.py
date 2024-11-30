def if_scheduled(tasks, n): # n is number of tasks
    float_sum = 0
    for i in range(n):
        float_sum += tasks[i][0] / tasks[i][1]
    return float_sum <= 1

def main():
    tasks = []
    number_of_tasks = int(input())
    for i in range(number_of_tasks):
        input_string = input()
        tasks.append(list(map(int, input_string.split())))
    print(if_scheduled(tasks, number_of_tasks))

if __name__ == '__main__':
    main()

