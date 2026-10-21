class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
            dup=-1
            missing=-1
            n=len(nums)
            for i in range(n):
                if nums[abs(nums[i]) - 1] <0:
                    dup=abs(nums[i])
                else:
                    nums[abs(nums[i])-1]*=(-1)
            for i in range(n):
                if nums[i] > 0:
                    missing=i+1
                    break
            return [dup,missing]
        