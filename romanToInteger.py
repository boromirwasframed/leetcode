class Solution:
    def romanToInt(self, s: str) -> int:
        numeralDict = {
            'I'  : 1,
            'IV' : 4,
            'V'  : 5,
            'IX' : 9,
            'X'  : 10,
            'XL' : 40,
            'L'  : 50,
            'XC' : 90,
            'C'  : 100,
            'CD' : 400,
            'D'  : 500,
            'CM' : 900,
            'M'  : 1000
        }
        
        value = 0
        i = 0
        
        while i < len(s):
            if i + 1 < len(s):
                if s[i] + s[i + 1] in numeralDict:
                    value += numeralDict[s[i] + s[i + 1]]
                    i += 2
                else:
                    value += numeralDict[s[i]]
                    i += 1
            else:
                value += numeralDict[s[i]]
                i += 1
            
        return value
