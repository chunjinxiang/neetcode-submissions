class Solution:
    def validPalindrome(self, s: str) -> bool:

        def normPalindrome(s, left, right, count):
            while left < right:

                if not s[left].isalnum():
                    left += 1
                    continue
                if not s[right].isalnum():
                    right -=1
                    continue

                if s[left].lower() != s[right].lower():
                    if count == 1:
                        count = 0
                        return normPalindrome(s, left+1, right, count) or normPalindrome(s, left, right-1, count)
                    return False

                left += 1
                right -= 1
                    
            return True

        left = 0
        right = len(s) - 1
        count = 1

        return normPalindrome(s, left, right, count)