class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        m=len(mat)  #rows
        n=len(mat[0]) # columns
        output={}
        for i in range(m):
            for j in range(n):
                key = i- j
                if key not in output:
                    output[key]=[]
                output[key].append(mat[i][j])
        for key in output:
            output[key].sort(reverse=True)

        for i in range(m):
            for j in range(n):
                mat[i][j]=output[i-j].pop()
        return mat
            