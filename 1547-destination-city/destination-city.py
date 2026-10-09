class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        c_map={}
        for source,dest in paths:
            c_map[source]=dest
        curr = paths[0][0]

        while curr in c_map:
            curr=c_map[curr]

        return curr