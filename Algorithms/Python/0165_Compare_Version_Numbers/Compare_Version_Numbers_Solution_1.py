
# Space: O(n)
# Time: O(n)

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = version1.split('.')
        version2_list = version2.split('.')
        length1, length2 = len(version1_list), len(version2_list)
        pointer1, pointer2 = 0, 0

        while pointer1 < length1 and pointer2 < length2:
            if int(version1_list[pointer1]) > int(version2_list[pointer2]): return 1
            if int(version1_list[pointer1]) < int(version2_list[pointer2]): return -1
            pointer1 += 1
            pointer2 += 1

        if pointer1 < length1:
            while pointer1 < length1:
                if int(version1_list[pointer1]) > 0: return 1
                pointer1 += 1

        if pointer2 < length2:
            while pointer2 < length2:
                if int(version2_list[pointer2]) > 0: return -1
                pointer2 += 1

        return 0





