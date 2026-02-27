class Solution(object):
    def searchInsert(self, nums, target):
        low=0
        high=len(nums)-1
        if target>nums[high]:
            return high+1
        elif target<nums[low] or low==high:
            return low
        else:
            while(low<high):
                mid=(low+high)//2
                if high==low+1 and nums[mid]!=target:
                    return mid+1
                elif nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    high=mid
                else:
                    low=mid
            
