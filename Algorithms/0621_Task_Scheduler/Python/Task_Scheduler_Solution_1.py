
# Space: O(n)
# Time: O(n)

# Explanation:
#             formula to solve this question:
#             total number full groups (k) * total number of items in each full groups (m) + total number of items in the unfull group (p)
#             k * m + p

#             edge case: if the above result is less than the number of total tasks, it means there is no "idle" needed to complete all tasks,
#                        so return the number of total tasks as result.

import collections


class Solution:
    def leastInterval(self, tasks, n):
        total_task = len(tasks)
        if n == 0: return total_task

        count_of_task = collections.Counter(tasks)
        max_task = max(count_of_task, key=lambda x: count_of_task[x])
        count_of_max_task = count_of_task[max_task]

        # total full groups that need to complete all tasks (k)
        k = count_of_max_task - 1

        # total number of items(tasks) in each full groups (m)
        m = n + 1

        # total number of items(tasks) in the unfull group (p)
        p = 1
        for i, j in count_of_task.items():
            if i != max_task and j == count_of_max_task:
                p += 1

        res = k * m + p

        return max(res, total_task)







