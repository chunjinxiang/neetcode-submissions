class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = {}
        
        for word in strs:
            grouped_anagrams = []
            signature = tuple(sorted(word))

            if signature in final:
                grouped_anagrams.append(word)
                final[signature] = final.get(signature) + grouped_anagrams
            else:
                grouped_anagrams.append(word)
                final[signature] = grouped_anagrams

        return list(final.values())