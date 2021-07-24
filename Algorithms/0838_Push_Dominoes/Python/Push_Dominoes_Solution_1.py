
# Space: O(n)
# Time: O(n)

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        length = len(dominoes)
        cache = [0 for _ in range(length)]

        force = 0
        for i in range(length):
            if dominoes[i] == 'R': force = length
            elif dominoes[i] == 'L': force = 0
            else: force = max(force - 1, 0)
            cache[i] += force

        force = 0
        for i in range(len(cache) - 1, -1, -1):
            if dominoes[i] == 'L': force = length
            elif dominoes[i] == 'R': force = 0
            else: force = max(force - 1, 0)
            cache[i] -= force

        res = ''
        for i in cache:
            if i > 0: res += 'R'
            elif i < 0: res += 'L'
            else: res += '.'

        return res




