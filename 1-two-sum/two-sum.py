class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
       a={}
       for i , data in enumerate(nums):
        rem=target-data
        if rem in a:
            return [a[rem],i]
        a[data]=i
       return []

