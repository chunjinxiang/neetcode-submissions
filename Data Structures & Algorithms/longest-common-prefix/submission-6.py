class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # prefix = ""
        # strs.sort(key=len)
        # for i in range(len(strs[0])):
        #     n = 0
        #     char = strs[0][i]
        #     for word in strs:
        #         if char != word[i]:
        #             return prefix
        #         else:
        #             n += 1
        #         if n == len(strs):    
        #             prefix += char

        # return prefix

        prefix = ""
        strs.sort(key=len)
        for i in range(len(strs[0])):
            char = strs[0][i]
            for word in strs:
                if char != word[i]:
                    return prefix

                # better method without using sort    
                # if i >= len(word) or word[i] != strs[0][i]:
                #     return prefix
  
            prefix += char

        return prefix