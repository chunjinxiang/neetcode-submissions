class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.replace(" ", "")

        left = 0
        right = len(s) - 1

        while left < right:

            current_left = s[left]
            current_right = s[right]

            if not current_left.isalnum():
                left += 1
                current_left = s[left]
                continue
            
            if not current_right.isalnum():
                right -= 1
                current_right = s[right]
                continue  
                
            if current_left.lower() == current_right.lower():
                left += 1
                right -= 1
                print(f"same {current_left}, {current_right}")
            else:
                print(f"not same {current_left}, {current_right}")
                return False
        return True
