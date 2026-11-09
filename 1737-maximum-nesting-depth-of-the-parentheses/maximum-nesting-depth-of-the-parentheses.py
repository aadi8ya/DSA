class Solution:
    def maxDepth(self, s: str) -> int:
        cnt=0
        max_depth=0
        for i in s:
            if i == '(':
                cnt+=1
                max_depth=max(max_depth,cnt)
            elif i == ')':
                cnt-=1
        return max_depth


        