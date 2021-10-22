
# Space: O(n)
# Time: O(n)

class Solution:
    def frequencySort(self, s: str) -> str:
        temp = list(s)
        temp = sorted(temp, key=lambda x: (-temp.count(x), x))
        return ''.join(temp)




