
# Space: O(n)
# Time: O(n)

class Solution:
    def numUniqueEmails(self, emails):
        length = len(emails)
        if length == 1: return 1
        temp = set()
        for each in emails:
            temp.add(self.get_real_name(each))
        return len(temp)

    def get_real_name(self, string: str):
        temp = string.split('@')
        temp[0] = temp[0].replace('.', '')
        if '+' in temp[0]:
            temp[0] = temp[0][:temp[0].index('+')]
        res = temp[0] + '@' + temp[1]
        return res




