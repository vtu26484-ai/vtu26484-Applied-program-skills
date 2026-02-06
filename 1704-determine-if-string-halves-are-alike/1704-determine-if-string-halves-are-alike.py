class Solution:
    def halvesAreAlike(self, s):
        vowels = set("aeiouAEIOU")
        mid = len(s) // 2

        count_a = 0
        count_b = 0

        for i in range(mid):
            if s[i] in vowels:
                count_a += 1

        for i in range(mid, len(s)):
            if s[i] in vowels:
                count_b += 1

        return count_a == count_b