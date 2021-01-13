
# Space: O(1)
# Time: O(n)

class Solution:
    def numRescueBoats(self, people, limit):
        count = 0
        people.sort()
        left, right = 0, len(people) - 1

        while left <= right:
            if left == right:
                count += 1
                break

            if people[right] == limit:
                count += 1
                right -= 1
            else:
                if people[left] + people[right] <= limit:
                    left += 1
                    right -= 1
                    count += 1
                else:
                    right -= 1
                    count += 1

        return count




