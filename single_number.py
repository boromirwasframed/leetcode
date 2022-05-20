# Complexity:
#   Time: O(n), because python3 get and pop and O(1) average case
#   Space: O(n), because the dictionary can get up to size n/2 --> n

# To Improve:
#   Use bitwise operation with XOR to keep O(n) time complexity but use only O(1) space complexity

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict = {}
        for i in range(0, len(nums)):
            val = nums[i]
            if num_dict.get(val):
                num_dict.pop(val)
            else:
                num_dict[val] = val
            
        return num_dict.popitem()[0]
