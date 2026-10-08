class Solution:
    def numberOfMatches(self, n: int) -> int:
        total=0
        while n!=1:
            even=n // 2
            total+=even
            odd=n%2
            n=even+odd
        return total