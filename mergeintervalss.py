class Solution(object):
    def merge(self, intervals):

        intervals.sort()
        merged = []
        for i in intervals:
            if not merged or merged[-1][1]<i[0]: #no overlapping or empty list
                merged.append(i)
            else: #overlappimg
                merged[-1][1]=max(merged[-1][1],i[1])
        return merged
