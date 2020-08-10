
# Space: O(n)
# Time: O(n)

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        temp = []
        # convert int to list of int
        while n:
            temp.insert(0, n % 10)
            n //= 10
        length = len(temp)

        # loop through the list from right to left
        for i in range(length - 1, 0, -1):
            # when we find a number is greater then the number on the left, then this is the place we want to switch numbers.
            if temp[i] > temp[i - 1]:

                # looking for the minimum number that greater than changing number(temp[i - 1]) from right hand side.
                index = length - 1
                while temp[index] <= temp[i - 1]:
                    index -= 1

                temp[index], temp[i - 1] = temp[i - 1], temp[index]

                # concat result
                res_left = temp[:i]
                res_right = sorted(temp[i:])
                res = res_left + res_right

                res_num = 0
                for i in res:
                    res_num = res_num * 10 + i

                return res_num if res_num < pow(2, 31) - 1 else -1  # need to verify if the result is greater than  32-bit integer

        return -1



