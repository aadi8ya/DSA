class Solution:
    def kidsWithCandies(self, candies: list[int], exetraCandis: int) -> list[bool]:
            res=[]
            max_candies=max(candies)
            for i in candies:
                total=exetraCandis+i
                if total>=max_candies:
                    res.append(True)
                else:
                     res.append(False)
            return res