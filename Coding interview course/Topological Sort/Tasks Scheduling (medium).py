from collections import deque, defaultdict


def is_scheduling_possible(tasks, prerequisites):
    if tasks <= 0:
        return False
    dependency_map = defaultdict(list)
    no_of_prerequisites = defaultdict(int)
    schedule = deque()
    ans = []
    for prerequisite, task in prerequisites:
        no_of_prerequisites[task] += 1
        dependency_map[prerequisite].append(task)
    for task in range(tasks):
        if no_of_prerequisites[task] == 0:
            schedule.append(task)
    while schedule:
        task = schedule.popleft()
        ans.append(task)
        for child_task in dependency_map[task]:
            no_of_prerequisites[child_task] -= 1
            if no_of_prerequisites[child_task] == 0:
                schedule.append(child_task)
    if len(ans) != tasks:
        return False
    return True


def main():
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))


main()
