class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total=0
        arr=[]
        for x in nums:
            total+=x
            arr.append(total)
        return arr

        