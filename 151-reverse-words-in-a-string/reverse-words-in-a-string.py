class Solution:
    def reverseWords(self, s: str) -> str:
        words=[]
        i=len(s)-1
        while i>=0:
            while i>=0 and s[i]==" ": #we skip the spaces
                i-=1
            if i<0:
                break
            end=i
            while i>=0 and s[i]!=" ": #find word boundary
                i-=1
            words.append(s[i+1 : end+1])
        return " ".join(words)