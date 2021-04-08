
# Space: O(1)
# Time: O(n)

class Solution:
    def intToRoman(self, num):
        cache = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        res = ''
        thousands = num // 1000
        num = num % 1000
        hundreds = num // 100
        num = num % 100
        tens = num // 10
        num = num % 10

        if thousands > 0:
            res += cache[1000] * thousands

        if hundreds > 0:
            if hundreds == 4:
                res += 'CD'
            elif hundreds == 9:
                res += 'CM'
            elif hundreds == 5:
                res += 'D'
            elif hundreds > 5:
                res += 'D' + cache[100] * (hundreds - 5)
            else:
                res += cache[100] * hundreds

        if tens > 0:
            if tens == 4:
                res += 'XL'
            elif tens == 9:
                res += 'XC'
            elif tens == 5:
                res += 'L'
            elif tens > 5:
                res += 'L' + cache[10] * (tens - 5)
            else:
                res += cache[10] * tens

        if num > 0:
            if num == 4:
                res += 'IV'
            elif num == 9:
                res += 'IX'
            elif num == 5:
                res += 'V'
            elif num > 5:
                res += 'V' + cache[1] * (num - 5)
            else:
                res += cache[1] * num

        return res





