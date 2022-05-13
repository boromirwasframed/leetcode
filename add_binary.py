class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0' and b == '0':
            return '0'
        
        sum_str = ''
        i = -1
        cur = 0
        
        while abs(i) <= max(len(a), len(b)) + 1:
            if abs(i) <= len(a) and a[i] == '1':
                cur += 1
            if abs(i) <= len(b) and b[i] == '1':
                cur += 1
            sum_str = '1' + sum_str if cur % 2 == 1 else '0' + sum_str
            cur = 1 if cur > 1 else 0
            i -= 1
        
        if len(sum_str) > 1 and sum_str[0] == '0':
            sum_str = sum_str.lstrip('0')
            
        return sum_str
