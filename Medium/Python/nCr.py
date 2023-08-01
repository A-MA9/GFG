#User function Template for python3

class Solution:
    def nCr(self, n, r):
        # code here
        if n-r==0:
            return 1
        elif r>n:
            return 0
        else:
            if n-r<r:
                r=n-r
            s=1;e=1
            for i in range(n-r+1,n+1):
                s*=i
            for j in range(1,r+1):
                e*=j
            d=s//e
            return d%(10**9+7)
