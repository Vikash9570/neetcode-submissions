class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # flag=0
        i=0
        j=0
        # while(flag==0):
        while(j<len(s) and i<len(t)):

            if t[i] == s[j]:
                i+=1
                # j+=1 accidently increasing j twice
            j+=1
        # if j==len(s) and i<len(t)-1:
        #     flag=1
        #     return len(t)+1-i 
            
        return len(t)-i