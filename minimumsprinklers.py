class Solution:
    def minSprinkler(self, gallery, n):

        intervals = []

        for i in range(n):
            if gallery[i] != -1:
                left = max(0, i - gallery[i])
                right = min(n -1, i + gallery[i])
                intervals.append([left, right])

        intervals.sort()

        count = 0
        i = 0
        covered = 0

        while covered < n:
            farthest = covered - 1

            while i < len(intervals) and intervals[i][0] <= covered:
                farthest = max(farthest, intervals[i][1])
                i += 1

            if farthest < covered:
                return -1

            count += 1
            covered = farthest + 1

        return count
