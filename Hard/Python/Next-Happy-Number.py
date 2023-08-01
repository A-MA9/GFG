class Solution:
    def c(self, n):
        s=0
        while n>0:
            d=n%10
            s+=d**2
            n//=10
        return s

    def h(self, n):
        a=set()
        while n!=1 and n not in a:
            a.add(n)
            n=self.c(n)
        return n==1

    def nextHappy(self, N):
        next=N+1
        while not self.h(next):
            next+=1
        return next

