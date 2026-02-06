class Solution:
    def firstUniqChar(self, s):
        # Count each character
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Find the first unique character
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1
