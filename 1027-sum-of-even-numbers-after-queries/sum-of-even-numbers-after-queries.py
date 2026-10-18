class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
            n=len(nums)
            q=len(queries)
            even_sum=0
            for i in range(n):
                if nums[i]%2==0:
                    even_sum+=nums[i]
            result=[]
            for i in range(q):
                val=queries[i][0]
                idx=queries[i][1]
                if nums[idx]%2==0:
                    even_sum-=nums[idx]
                nums[idx]+=val
                if nums[idx]%2==0:
                    even_sum+=nums[idx]
                result.append(even_sum)
            return result

            