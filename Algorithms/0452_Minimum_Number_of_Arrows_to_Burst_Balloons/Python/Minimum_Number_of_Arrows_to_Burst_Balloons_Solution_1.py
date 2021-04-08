
# Space: O(n)
# Time: O(n)

class Solution:
    def findMinArrowShots(self, points):
        if len(points) == 1: return 1

        points.sort(key=lambda x: (x[0], x[1]))
        temp_point = []

        # remove duplicates
        for i in points:
            if not temp_point or i != temp_point[-1]:
                temp_point.append(i)

        if len(temp_point) == 1: return 1

        stack = []

        for each in temp_point:

            if not stack or stack[-1][1] < each[0]:
                stack.append(each)

            elif stack[-1][1] >= each[0]:
                temp = [max(stack[-1][0], each[0]), min(stack[-1][1], each[1])]
                stack.pop()
                stack.append(temp)

        return len(stack)





