#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code her
        s=N//2
        A.sort()
        if A.count(A[s])>s:
            return A[s]
        return -1
