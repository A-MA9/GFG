class Solution:
    def missingNumber(self, arr, n):
        x=0
        for i in range(n):
            if arr[i]==1:
                x=1
                break
        if x==0:
            return 1
        for i in range(n):
            if arr[i]<=0 or arr[i]>n:
                arr[i]=1
        for i in range(n):
            arr[(arr[i]-1)%n]+=n
        for i in range(n):
            if arr[i]<=n:
                return(i+1)
        return n+1