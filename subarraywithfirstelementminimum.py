class Solution:
    def validSubarrays(self, nums):
        n = len(nums)
        stack = []
        result = 0

        for i in range(n):
            
            while stack and nums[stack[-1]] > nums[i]:
                idx = stack.pop()
                result += i - idx

            stack.append(i)

        # Remaining elements extend till end
        while stack:
            idx = stack.pop()
            result += n - idx

        return result
