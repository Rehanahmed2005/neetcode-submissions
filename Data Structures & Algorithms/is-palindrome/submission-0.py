class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s) - 1

        while left < right:          
            if not self.isalphnum(s[left]):
                left += 1
                continue
            elif not self.isalphnum(s[right]):
                right -= 1 
                continue
            if s[left].lower() != s[right].lower():
                return False 

            left += 1
            right -= 1

        return True

    def isalphnum(self, n):
        val = ord(n)
        return(65 <= val <= 90) or (97 <= val <= 122) or (48 <= val <= 57)
