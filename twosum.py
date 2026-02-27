class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numdict={}
        for i in range(len(nums)):
            j=target-nums[i]
            if j in numdict:
                return [numdict[j],i]
            numdict[nums[i]]=i
