class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n=len(nums)
        sum=0
        for i in nums:
            sum+=i
        cs=0
        for i in range(n):
            ls=cs
            rs=sum-nums[i]-cs
            if ls == rs:
                return i
            cs+=nums[i]

        return -1
