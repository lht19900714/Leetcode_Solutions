
# Space: O(n)
# Time: O(n)

class Solution:
    def carPooling(self, trips, capacity):
        if len(trips) == 1 and trips[0][0] >= capacity: return True

        data = []

        for each in trips:
            data.append([each[1], each[0]])
            data.append([each[2], -each[0]])

        data.sort(key=lambda x: (x[0], x[1]))
        temp_capacity = 0

        for i in data:
            temp_capacity+=i[1]
            if temp_capacity>capacity:
                return False

        return True





