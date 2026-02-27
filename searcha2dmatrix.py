class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)
        n=len(matrix[0])
        low=0
        high=m*n-1
        while low<=high:
            mid=(low+high)//2 #eg: 5 (indexed)
            row=mid//n #5//4= 1st row (indexed)
            col=mid%n #5%4=1st element (indexed)
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                low=mid+1
            else:
                high=mid-1
        return False
