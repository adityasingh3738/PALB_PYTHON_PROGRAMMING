class Solution:
    def hasTripletSum(self, arr, target):
        n=len(arr)
        for i in range(n):
            rem=target-arr[i]
            sum=set()
            for j in range(i+1,n):
                if rem-arr[j] in sum:
                    return True
                sum.add(arr[j])
        return False
        
