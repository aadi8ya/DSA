class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        lar=float('-inf')
        second_lar=float('-inf')
        small=float('inf')
        second_small=float('inf')
        for i in nums:
            if i>lar:
                second_lar=lar
                lar=i
            elif i > second_lar:
                second_lar=i
            if i < small:
                second_small = small
                small=i
            elif i<second_small:
                second_small=i
        return (lar * second_lar) - (small * second_small)
