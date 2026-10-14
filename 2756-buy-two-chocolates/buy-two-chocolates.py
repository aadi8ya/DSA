class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1=float('inf')
        min2=float('inf')
        for i in prices:
            if i < min1:
                min2=min1
                min1=i
            elif i < min2:
                min2=i
        total = money - (min1+min2)
        if total >= 0 :
            return total
        else:
            return money