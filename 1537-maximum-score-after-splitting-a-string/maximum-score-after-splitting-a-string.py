class Solution:
    def maxScore(self, s: str) -> int:
        n=len(s)
        res=float('-inf')
        total_one=s.count('1')
        zero_left=0
        one_left=0
        for i in range(n-1):
            if s[i]=='0':
                zero_left+=1
            else:
                one_left+=1
            res=max(res,zero_left-one_left)
        return res+total_one
            



