
# Space: O(n)
# Time: O(n)

class Solution:
    def sequentialDigits(self, low, high):
        sequence = '123456789'
        res = []
        start_length = len(str(low))
        end_length = len(str(high))

        for length in range(start_length, end_length + 1):

            for i in range(len(sequence)):

                end_index = i + length
                if end_index > len(sequence): break

                temp_res = sequence[i: i + length]
                if low <= int(temp_res) <= high: res.append(int(temp_res))

        return res




