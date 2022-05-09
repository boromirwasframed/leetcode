class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x != 0 and (x < 0 or x % 10 == 0):
            return False
        
        reversed_num = 0
        
        while reversed_num < x:
            reversed_num =  reversed_num * 10 + x % 10
            x = x // 10
        
        if x == reversed_num or x == reversed_num // 10:
            return True
        
        return False
