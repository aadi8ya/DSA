class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = 0
#here we count the vowels in first window
        for i in range(k):
            if s[i] in vowels:
                count += 1
               
        max_count = count

        #here we sliding the window 
        for i in range(k,len(s)):
            if s[i-k] in vowels:
                count-=1
            
            if s[i] in vowels:
                count+=1
            
            max_count=max(count,max_count)

                    
        return max_count