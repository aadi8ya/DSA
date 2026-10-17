class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
            n=len(changed)
            if n%2!=0:
                return []
            changed.sort()
            freq={}
            for i in changed:
                if i in freq:
                    freq[i]+=1
                else:
                    freq[i]=1
            original=[]
            for i in changed:
                if freq[i]==0:
                    continue
                double=2*i
                if freq.get(double,0)==0:
                    return[]
                original.append(i)
                freq[i]-=1
                freq[double]-=1
            return original
                
             


        



        