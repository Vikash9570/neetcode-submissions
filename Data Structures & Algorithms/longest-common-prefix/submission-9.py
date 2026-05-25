class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first=strs[0]
        for i in range(len(first)):
            ch=first[i]
            for item in strs:
                if i>=len(item) or item[i]!=ch  :
                    return first[:i]
                # elif item[i]!=ch and i==0:
                    # return ''
        
        return first

            





