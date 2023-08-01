

class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        #code here
        s=arr1+arr2
        s.sort()
        # arr1=s[:m]
        # arr2=s[m:]
        for i in range(n):
            arr1[i]=s[i]
        for j in range(m):
            arr2[j]=s[n+j]




