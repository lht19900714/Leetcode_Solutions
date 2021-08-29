
# Space: O(n)
# Time: O(n^2)

import collections


class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        cache = [0 for _ in range(max(endTime) + 1)]

        # end_time : [[start_time, profit],[start_time, profit]]
        cache_dict = collections.defaultdict(list)
        for i in range(len(endTime)):
            cache_dict[endTime[i]].append([startTime[i], profit[i]])

        for i in range(1, len(cache)):

            if i not in cache_dict:
                cache[i] = cache[i - 1]
            else:
                temp_list = cache_dict[i]
                for start_time, profit in temp_list:
                    cache[i] = max(cache[i], profit + cache[start_time])
                cache[i] = max(cache[i], cache[i - 1])
        return cache[-1]





