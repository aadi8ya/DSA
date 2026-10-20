class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
            freq={}
            n=len(nums)
            for i in range(n):
                if nums[i] in freq and abs(freq[nums[i]]-i)<=k:
                    return True
                freq[nums[i]]=i

            return False
                
                