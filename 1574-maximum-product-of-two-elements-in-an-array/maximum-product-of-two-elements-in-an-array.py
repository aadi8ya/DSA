class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        first_lr = 0
        second_lr = 0
        for num in nums:
            if num > first_lr:
                second_lr=first_lr
                first_lr=num
            elif num>second_lr:
                second_lr=num
                
        return (first_lr - 1) * (second_lr - 1)

                