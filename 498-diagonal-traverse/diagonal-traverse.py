class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m=len(mat)
        n=len(mat[0])
        output={}
        for i in range(m):
            for j in range(n):
                key=i+j
                if key not in output:
                    output[key]=[]
                output[key].append(mat[i][j])
        result=[]
        for key in output:
            if key %2==0:
              output[key].reverse()
            result.extend(output[key])
        return result

        