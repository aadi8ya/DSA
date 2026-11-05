class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count=0
        n=len(arr1)
        m=len(arr2)
        for i in range(n):
            valid=True
            for j in range(m):
                if (abs(arr1[i] -arr2[j])<=d):
                    valid=False
                    break
            if valid:
                count+=1
        return count
