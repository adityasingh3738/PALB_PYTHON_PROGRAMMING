class Solution:
	def minJumps(self, arr):
	    n=len(arr)
	    if n<=1:
	        return 0
	    if arr[0]==0:
	        return -1
	        
	    jump=0
	    maxreach=0
	    end=0
	    
	    for i in range(n-1):
	        maxreach=max(maxreach,i+arr[i])
	        if i>=maxreach:
	            return -1
	            
	        if i==end:
	            jump+=1
	            end=maxreach
	            if end>=n-1:
	                return jump
