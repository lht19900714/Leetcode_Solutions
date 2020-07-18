
# V: the number of vertices(numCourses);
# E: the number of edges(number of prerequisites for each course)
# Space: O(V+E)
# Time: O(V+E)

# Explanation:
# Topological Ordering

# 1. create a dictionary to record each course and it's prerequisites
# 2. add courses that do not have prerequisites into a list, and popping the list.
#    during the popping, continually update each course's prerequisites status in the dictionary.
#    if any course do not have prerequisites anymore, add it to list.
# 3. verify result and return


import collections


class Solution:
    def findOrder(self, numCourses, prerequisites):
        source_data = collections.defaultdict(list)
        for i, j in prerequisites:
            source_data[i].append(j)
        alist = [x for x in range(numCourses) if x not in source_data]
        res = []

        while alist:
            cur = alist.pop()
            res.append(cur)
            clean_record = []
            for i, j in source_data.items():
                if cur in j:
                    source_data[i].remove(cur)
                    if len(source_data[i]) == 0:
                        alist.append(i)
                        clean_record.append(i)
            if len(clean_record) > 0:
                for i in clean_record:
                    source_data.pop(i)

        return res if len(res) == numCourses else []




