class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0
        total_sum = 0
        answer = float('inf')

        while right < len(nums):

            total_sum += nums[right]

            while total_sum >= target:

                answer = min(answer, right - left + 1)

                total_sum -= nums[left]
                left += 1

            right += 1

        if answer == float('inf'):
            return 0

        return answer
        