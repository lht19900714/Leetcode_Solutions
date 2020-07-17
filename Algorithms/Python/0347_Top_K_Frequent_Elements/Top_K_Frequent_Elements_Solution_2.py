
# Space: O(n)
# Time: O(nlogk)

import collections


class Solution:
    def topKFrequent(self, nums, k):
        counts = collections.Counter(nums)

        # Following code can be replaced by a method nlargest from heapq library.
        # return heapq.nlargest(k, counts.keys(), key=counts.get)

        def heapify(index, length, source_list):
            left = 2 * index + 1
            right = 2 * index + 2
            max_index = index
            if left < length and source_list[max_index][1] < source_list[left][1]:
                max_index = left
            if right < length and source_list[max_index][1] < source_list[right][1]:
                max_index = right
            if max_index != index:
                source_list[max_index], source_list[index] = source_list[index], source_list[max_index]
                heapify(max_index, length, source_list)

        def build_heap(alist):
            length = len(alist)
            start_point = length // 2
            for i in range(start_point, -1, -1):
                heapify(i, length, alist)
            return alist

        def generate_result(alist, k):
            res = []
            temp = build_heap(alist)

            for i in range(len(temp) - 1, -1, -1):
                if k == 0: break
                res.append(temp[0][0])
                temp[0], temp[i] = temp[i], temp[0]
                heapify(0, i, temp)
                k -= 1
            return res

        return generate_result(counts, k)
