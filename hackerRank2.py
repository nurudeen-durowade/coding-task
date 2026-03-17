"""
 Given an array of intervals [startTime, endTime], merge all overlapping intervals and return a sorted array of non-overlapping intervals.

Example

Input

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output

[[1, 6], [8, 10], [15, 18]]
"""

def mergeHighDefinitionIntervals(intervals):

        intervals.sort(key=lambda x: x[0])

        merge = []

        for interval in intervals:
                if not merge or merge[-1][1] < interval[0]:
                        merge.append(interval)
                else:
                    merge[-1][-1] = max(merge[-1][1], interval[1])
        return merge

print(mergeHighDefinitionIntervals([[1, 3], [2, 6], [8, 10], [15, 18]]))