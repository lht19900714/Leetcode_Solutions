
# Space: O(1)
# Time: O(n^2)

class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) <= 1: return s

        cur_index = 0

        while cur_index < len(s):
            if s[cur_index].isnumeric():
                number_end_index = cur_index

                # extract number
                while number_end_index < len(s) and s[number_end_index].isnumeric():
                    number_end_index += 1
                number = s[cur_index:number_end_index]

                # extract string in the bracket
                bracket_count = 1
                bracket_end_index = number_end_index + 1
                while bracket_end_index < len(s) and bracket_count:
                    if s[bracket_end_index] == '[':
                        bracket_count += 1
                    elif s[bracket_end_index] == ']':
                        bracket_count -= 1
                    bracket_end_index += 1
                temp_res = s[number_end_index + 1:bracket_end_index - 1]

                # re-construct s
                s = s[:cur_index] + temp_res * int(number) + s[bracket_end_index:]
                cur_index = 0
            else:
                cur_index += 1
        return s




