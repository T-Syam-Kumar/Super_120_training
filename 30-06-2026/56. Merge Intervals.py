def merge(intervals):
    intervals.sort() 
    merged = []
    prev = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= prev[1]:
            prev[1] = max(prev[1], intervals[i][1])
        else:
            merged.append(prev)
            prev = intervals[i]
    merged.append(prev)
    return merged