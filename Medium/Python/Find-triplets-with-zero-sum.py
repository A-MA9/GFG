#User function Template for python3

class Solution:
    def findTriplets(self, arr, n):
        #code here
        arr.sort()
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                t=arr[i]+arr[l]+arr[r]
                if t==0:
                    return 1 
                elif t<0:
                    l+=1
                else:
                    r-=1
        return 0
        