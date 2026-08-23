class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        left = 0
        right = len(s) - 1

        while left < right:
            front = s[left]
            back = s[right]

            s[left] = back
            s[right] = front

            
            left +=1
            right -=1