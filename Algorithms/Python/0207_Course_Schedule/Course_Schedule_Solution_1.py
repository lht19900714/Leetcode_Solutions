
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
    def canFinish(self, numCourses, prerequisites) -> bool:
        if not len(prerequisites):
            return True
        source_data = collections.defaultdict(list)

        for i, j in prerequisites:
            source_data[i].append(j)
        count = 0
        ready_course = [i for i in range(numCourses) if i not in source_data]

        while ready_course:
            cur = ready_course.pop()
            count += 1
            for i in source_data:
                if cur in source_data[i]:
                    source_data[i].remove(cur)
                    if len(source_data[i]) == 0:
                        ready_course.append(i)

        return True if count == numCourses else False




