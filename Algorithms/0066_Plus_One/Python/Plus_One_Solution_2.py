
# Space: O(1)
# Time: O(n)


class Solution:
    def plusOne(self, digits):
        digits[-1] += 1
        index = len(digits) - 1
        forward = 0

        while index >= 0:
            digits[index] += forward

            if digits[index] < 10:
                forward = 0
                break
            else:
                digits[index] = 0
                forward = 1

            index -= 1

        return digits if forward == 0 else [1] + digits



