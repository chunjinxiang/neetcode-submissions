class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = {}
        
        for word in strs:
            # grouped_anagrams = []
            signature = tuple(sorted(word))

            if signature in final:
                # grouped_anagrams.append(word)
                final[signature] = final.get(signature) + [word]
            else:
                # grouped_anagrams.append(word)
                final[signature] = [word]

        return list(final.values())