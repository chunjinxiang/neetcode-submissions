class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        final = {}

        for word in strs:
            seen = {}
            grouped_anagrams = []

            for char in word:
                seen[char] = seen.get(char,0) + 1

            sorted_seen = sorted(seen.items())
            signature_list = []
            for i in range(len(sorted_seen)):
                letter = sorted_seen[i][0]
                count = seen[letter]
                signature_list.append(letter + str(count))
            signature = tuple(signature_list)

            if signature in final:
                grouped_anagrams.append(word)
                final[signature] = final.get(signature) + grouped_anagrams
            else:
                grouped_anagrams.append(word)
                final[signature] = grouped_anagrams

        return(list(final.values()))