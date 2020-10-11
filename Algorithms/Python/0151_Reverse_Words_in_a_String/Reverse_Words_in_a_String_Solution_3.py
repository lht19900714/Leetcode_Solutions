
# Space: O(n)
# Time: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        temp = s.split()
        return ' '.join(temp[::-1])



