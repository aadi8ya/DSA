class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)
        for i in trust:
            u=i[0]
            v=i[1]
            outdegree[u]+=1
            indegree[v]+=1
        for i in range(1, n + 1):
            if indegree[i]==n-1 and outdegree[i]==0:
                return i
        return -1
