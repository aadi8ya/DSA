class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
            n=len(nums)
            freq = {0: -1}
            sum=0
            for i in range(n):
                sum+=nums[i]
                rem=sum%k
                if rem in freq:
                    if i-freq[rem]>=2:
                        return True
                else:
                    freq[rem]=i
            return False