def merge(intervals:list):
    intervals.sort(key=lambda x: x[0])
    # print(intervals)
    current_max = intervals[0][1]
    current_interval = intervals[0]
    merged_intervals = list()
    merged_interval = [current_interval[0], current_interval[1]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= current_max:
            merged_interval = [current_interval[0], intervals[i][1]]
            current_max = intervals[i][1]
            current_interval = merged_interval
            # print(current_max, current_interval)
        else:
            merged_intervals.append(merged_interval)
            current_max = intervals[i][1]
            current_interval = intervals[i]
            merged_interval = [current_interval[0], current_interval[1]]

    merged_intervals.append(merged_interval)
    return merged_intervals

intervals = [[10, 16], [1, 3], [2, 6], [15, 18], [8, 10]]
print("TEST 1:")
print(merge(intervals), end="\n\n")

intervals = [[10, 16], [1, 3], [2, 6], [15, 18], [8, 10], [25, 28]]
print("TEST 2:")
print(merge(intervals), end="\n\n")

intervals = [[10, 16], [1, 3], [25, 28]]
print("TEST 3:")
print(merge(intervals), end="\n\n")

intervals = [[10, 16], [1, 3], [4, 6], [15, 18], [8, 10], [25, 28]]
print("TEST 4:")
print(merge(intervals), end="\n\n")